import re
import json
import argparse
import sys


def parse_header(file_path, target_arch):
    intrinsics = {"x86_64": {}, "arm64": {}, "arm64_x86_64": {}}

    # Match the MSVC macro wrapper, e.g., __MACHINEARM64(unsigned __int64 __getReg(int _Reg))
    macro_pattern = re.compile(r"^[\s]*__MACHINE([A-Z0-9_]*)\s*\(\s*(.+)\s*\)[\s;]*$")

    # Common type keywords used to differentiate between a type and a parameter name
    type_keywords = {
        "int",
        "char",
        "short",
        "long",
        "__int64",
        "float",
        "double",
        "void",
        "__m128",
        "__m128i",
        "__m128d",
        "__m256",
        "__m256i",
        "__m256d",
        "__m512",
        "__m512i",
        "__m512d",
        "size_t",
        "uint8_t",
        "uint16_t",
        "uint32_t",
        "uint64_t",
        "int8_t",
        "int16_t",
        "int32_t",
        "int64_t",
    }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    for line in lines:
        match = macro_pattern.match(line)
        if not match:
            continue

        arch_suffix = match.group(1)
        proto = match.group(2)

        # Categorize by architecture
        category = None
        if arch_suffix in ["X64", "X86_X64"]:
            category = "x86_64"
        elif arch_suffix in ["ARM64", "ARM_ARM64"]:
            category = "arm64"
        elif arch_suffix in ["", "W64"]:
            category = "arm64_x86_64"

        if not category:
            continue

        if target_arch == "arm64" and category == "x86_64":
            continue
        if target_arch == "x86_64" and category == "arm64":
            continue

        # Extract function name and return type
        name_match = re.search(r"([a-zA-Z0-9_]+)\s*\(", proto)
        if not name_match:
            continue

        name = name_match.group(1)
        ret_type = proto[: name_match.start()].strip()

        # Parse arguments to generate variable setups
        args_match = re.search(r"\((.*)\)", proto)
        setup_stmts = []
        call_args = []

        if args_match:
            args_str = args_match.group(1).strip()
            if args_str and args_str != "void":
                raw_args = args_str.split(",")
                for i, raw_arg in enumerate(raw_args):
                    raw_arg = raw_arg.strip()

                    # Determine type and variable name
                    if raw_arg.endswith("*") or raw_arg.endswith("&"):
                        t_str, v_name = raw_arg, f"arg{i}"
                    else:
                        word_match = re.search(r"\b([a-zA-Z_][a-zA-Z0-9_]*)$", raw_arg)
                        if word_match:
                            last_word = word_match.group(1)
                            if last_word in type_keywords:
                                # The whole string is just a type (e.g. "unsigned int")
                                t_str, v_name = raw_arg, f"arg{i}"
                            else:
                                # The last word is a parameter name (e.g. "_Mask")
                                t_str = raw_arg[: word_match.start()].strip()
                                v_name = last_word
                                if not t_str:
                                    t_str = "int"  # Fallback if parsing fails
                        else:
                            t_str, v_name = raw_arg, f"arg{i}"

                    # Create the variable declaration statement
                    setup_stmts.append(f"{t_str} {v_name};")
                    call_args.append(v_name)

        # Assemble the final call string
        call_pieces = []
        if setup_stmts:
            call_pieces.append(" ".join(setup_stmts))

        assignment = ""
        if ret_type and ret_type != "void":
            assignment = f"{ret_type} result = "

        call_pieces.append(f"{assignment}{name}({', '.join(call_args)});")

        # Add to dictionary
        intrinsics[category][name] = {"proto": proto, "call": " ".join(call_pieces)}

    # Clean empty dictionaries to keep output tidy
    if target_arch == "arm64":
        intrinsics.pop("x86_64", None)
    elif target_arch == "x86_64":
        intrinsics.pop("arm64", None)

    return intrinsics


def main():
    parser = argparse.ArgumentParser(
        description="Parse MSVC headers and generate test calls."
    )
    parser.add_argument("file", help="Path to the header file (e.g., intrin0.h)")
    parser.add_argument(
        "--arch",
        choices=["arm64", "x86_64", "both"],
        default="both",
        help="Specify which architectures to dump. Default is 'both'.",
    )

    args = parser.parse_args()
    parsed_data = parse_header(args.file, args.arch)
    print(json.dumps(parsed_data, indent=2))


if __name__ == "__main__":
    main()
