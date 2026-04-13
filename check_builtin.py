import sys
import subprocess
import tempfile
import os
import argparse

from msvc_builtins import MSVC_BUILTINS, MSVC_BUILTINS_DEFAULT


def check_builtin(compiler_bin, func_name, config, target_arch):
    """
    Creates a temporary C file, compiles it, and checks if it links correctly.
    Handles both Clang and MSVC (cl.exe).
    """
    c_code = f"""
    #include <stdint.h>
    
    {config["proto"]}
    
    int main(void) {{
        {config["call"]}
        return 0;
    }}
    """

    with tempfile.NamedTemporaryFile(
        suffix=".c", delete=False, mode="w", encoding="utf-8"
    ) as tmp_c:
        tmp_c.write(c_code)
        tmp_c_name = tmp_c.name

    tmp_exe_name = tmp_c_name[:-2] + ".exe"
    tmp_obj_name = tmp_c_name[:-2] + ".obj"

    # Check if the user passed 'cl' or 'cl.exe'
    compiler_base = os.path.basename(compiler_bin).lower()
    is_msvc = compiler_base in ["cl", "cl.exe"]

    cmd = [compiler_bin]

    if is_msvc:
        # MSVC relies on the environment for the target architecture
        cmd.extend(["/nologo", tmp_c_name, f"/Fe{tmp_exe_name}", f"/Fo{tmp_obj_name}"])
    else:
        # Clang requires explicit target definition
        clang_target = f"{target_arch}-pc-windows-msvc"
        cmd.extend([f"--target={clang_target}", tmp_c_name, "-o", tmp_exe_name])

    try:
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        is_success = result.returncode == 0

        # MSVC often prints errors to stdout instead of stderr depending on the phase
        error_output = (
            result.stdout + "\n" + result.stderr if is_msvc else result.stderr
        )
        return is_success, error_output
    finally:
        # Clean up all possible temporary files
        files_to_remove = [
            tmp_c_name,
            tmp_exe_name,
            tmp_obj_name,
            tmp_c_name[:-2] + ".lib",
            tmp_c_name[:-2] + ".exp",
        ]

        for file_path in files_to_remove:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError:
                    pass


def main():
    parser = argparse.ArgumentParser(
        description="Check compiler builtin support for Windows/Clang parity."
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print compiler errors for unsupported builtins",
    )
    parser.add_argument(
        "--only-results", "-r", action="store_true", help="Print only the results"
    )
    parser.add_argument(
        "--set",
        type=str,
        choices=list(MSVC_BUILTINS.keys()),
        default=MSVC_BUILTINS_DEFAULT,
        required=False,
        help="Select which set to check. (default: %(default)s)",
    )
    parser.add_argument(
        "--builtins",
        "-b",
        nargs="+",
        help="Specific built-ins to check (e.g., -b __dmb __isb). If omitted, checks all.",
    )
    parser.add_argument(
        "--compiler",
        type=str,
        required=True,
        help="Path to the compiler binary (e.g., clang or C:\\path\\to\\clang.exe)",
    )
    parser.add_argument(
        "--arch",
        choices=["aarch64", "x86_64"],
        default="aarch64",
        help="Target architecture (default: aarch64)",
    )
    args = parser.parse_args()

    set_builtins = MSVC_BUILTINS[args.set]

    # Determine which built-ins to check
    if args.builtins:
        target_builtins = args.builtins
    else:
        target_builtins = set_builtins.keys()

    # Notify user regarding MSVC environment expectation
    if os.path.basename(args.compiler).lower() in ["cl", "cl.exe"]:
        print(
            f"⚠️ Note: cl.exe uses the active shell environment. Ensure you ran vcvarsall.bat {args.arch}!"
        )
    else:
        print(f"Target Architecture: {args.arch}")

    print(f"Using compiler {args.compiler} | targetting Vscode: {args.set}")
    if args.only_results:
        print(f"{'Status':<15}")
    else:
        print(f"{'Built-in':<35} | {'Status':<15}")
    print("-" * 48)

    supported_count = 0
    total_count = 0

    for func_name in target_builtins:
        if func_name not in set_builtins:
            print(f"{func_name:<35} | ⚠️ Not in dictionary")
            continue

        total_count += 1
        config = set_builtins[func_name]
        is_supported, stderr_output = check_builtin(
            args.compiler, func_name, config, args.arch
        )

        if is_supported:
            status = "✅ Supported"
            supported_count += 1
        else:
            status = "❌ Missing"

        if args.only_results:
            print(f"{status:<15}")
        else:
            print(f"{func_name:<35} {status:<15}")

        if not is_supported and args.verbose:
            print(f"\n--- Compiler Error for {func_name} ---")
            print(stderr_output.strip())
            print("-" * 48 + "\n")

    print("-" * 48)
    print(
        f"Summary: {total_count - supported_count}/{total_count} targeted built-ins missing."
    )


if __name__ == "__main__":
    main()
