# It requires to install clang bindings and have libclang.dll on path:
#
# pip install clang
#
# To print all C function provided by the header:
#
#   parse_header.py --libclang C:\path\to\libclang.dll <header>
#
# And to check which builtins are missing from msvc_builtins dict:
#
#   parse_header.py --libclang C:\path\to\libclang.dll --compare-builtin-header <header> 

import argparse
import json
import clang.cindex
import os
import re

# Import the MSVC built-ins dictionary
try:
    from msvc_builtins import MSVC_BUILTINS
except ImportError:
    # Fallback just in case the file doesn't exist yet
    MSVC_BUILTINS = {}


def clean_type_string(type_str):
    """Removes const, volatile, and restrict qualifiers for clean variable declarations."""
    return re.sub(r"\b(const|volatile|restrict)\b", "", type_str).strip()


def analyze_header(header_path):
    index = clang.cindex.Index.create()
    translation_unit = index.parse(header_path, args=["-x", "c"])
    functions_dict = {}

    for node in translation_unit.cursor.get_children():
        if node.location.file and os.path.abspath(
            node.location.file.name
        ) == os.path.abspath(header_path):
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                func_name = node.spelling

                # 1. Extract the exact prototype
                proto_tokens = []
                for t in node.get_tokens():
                    if t.spelling in [";", "{"]:
                        break
                    proto_tokens.append(t.spelling)
                proto = " ".join(proto_tokens)

                # 2. Generate temporary variables and call arguments
                arg_names = []
                declarations = []

                for i, arg in enumerate(node.get_arguments()):
                    var_name = arg.spelling if arg.spelling else f"arg_{i}"
                    arg_type = arg.type

                    if arg_type.kind == clang.cindex.TypeKind.POINTER:
                        pointee_type = arg_type.get_pointee().spelling
                        clean_type = clean_type_string(pointee_type)

                        if clean_type == "void":
                            declarations.append(f"void* {var_name} = 0;")
                            arg_names.append(var_name)
                        else:
                            declarations.append(f"{clean_type} {var_name} = 0;")
                            arg_names.append(f"&{var_name}")

                    elif arg_type.kind in [
                        clang.cindex.TypeKind.INCOMPLETEARRAY,
                        clang.cindex.TypeKind.CONSTANTARRAY,
                    ]:
                        element_type = clean_type_string(arg_type.element_type.spelling)
                        declarations.append(f"{element_type} {var_name}[1] = {{0}};")
                        arg_names.append(var_name)

                    else:
                        clean_type = clean_type_string(arg_type.spelling)
                        if not clean_type:
                            clean_type = "int"
                        declarations.append(f"{clean_type} {var_name} = 0;")
                        arg_names.append(var_name)

                if node.type.is_function_variadic():
                    arg_names.append("...")

                # 3. Assemble the final multi-line call snippet
                decl_snippet = "\n".join(declarations)
                call_stmt = f"{func_name}({', '.join(arg_names)});"

                if decl_snippet:
                    call_snippet = f"{decl_snippet}\n{call_stmt}"
                else:
                    call_snippet = call_stmt

                functions_dict[func_name] = {"proto": proto, "call": call_snippet}

    return {"header": functions_dict}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse a C header and optionally compare it against all MSVC built-ins."
    )
    parser.add_argument("header_file", help="Path to the C header file to analyze")
    parser.add_argument(
        "--libclang", help="Explicit path to libclang.dll", default=None
    )
    parser.add_argument(
        "--compare-builtin-header",
        action="store_true",
        help="Compare parsed header against all functions in MSVC_BUILTINS and output only the extra ones.",
    )
    args = parser.parse_args()

    if args.libclang:
        clang.cindex.Config.set_library_file(args.libclang)

    if not os.path.exists(args.header_file):
        print(f"Error: File '{args.header_file}' not found.")
        exit(1)

    # Run the base parsing
    result_dict = analyze_header(args.header_file)

    # Run the comparison if requested
    if args.compare_builtin_header:
        # Flatten all known MSVC built-ins into a single set for fast lookup
        all_msvc_funcs = set()
        for header_funcs in MSVC_BUILTINS.values():
            all_msvc_funcs.update(header_funcs.keys())

        parsed_funcs = result_dict["header"]
        extra_funcs = {}

        # Find functions in the parsed header that do not exist anywhere in MSVC_BUILTINS
        for func_name, func_data in parsed_funcs.items():
            if func_name not in all_msvc_funcs:
                extra_funcs[func_name] = func_data

        # Overwrite the result dictionary so ONLY extra_builtins are printed
        result_dict = {"extra_builtins": extra_funcs}

    # Output the final JSON
    print(json.dumps(result_dict, indent=2))
