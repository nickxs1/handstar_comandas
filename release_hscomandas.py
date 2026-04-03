import subprocess
import argparse
import sys

def create_release(version: str, asset_path: str, title: str, notes: str):
    """Create a GitHub release using the gh CLI.

    Args:
        version: Release tag, e.g., 'HSComandas_Vxxxx'.
        asset_path: Path to the asset file to upload.
        title: Title of the release.
        notes: Release notes.
    """
    cmd = [
        "gh",
        "release",
        "create",
        version,
        asset_path,
        "--title",
        title,
        "--notes",
        notes,
    ]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Release created successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error creating release:", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        sys.exit(e.returncode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a GitHub release for HSComandas.")
    # Default values correspond to the original command parameters.
    Versao = "4.0"
    parser.add_argument("--version", default=f"HSComandas_V{Versao}", help=f"Release tag, e.g., HSComandas_V{Versao}")
    parser.add_argument(
        "--asset",
        default=rf"F:\Disco\Projetos\Site-Servidor\APPS Handstar\Impressor_Comandas\dist\HSComandas.exe",
        help="Path to the asset file to upload",
    )
    parser.add_argument("--title", default=f"Versão {Versao}", help="Release title")
    parser.add_argument("--notes", default=f"Versão {Versao}", help="Release notes")

    args = parser.parse_args()
    create_release(args.version, args.asset, args.title, args.notes)
