"""Command-line entry point for the assessment project."""

from dotenv import load_dotenv


def main() -> None:
    """Load local configuration and confirm that the project is ready."""
    load_dotenv()
    print("Apart assessment environment is ready.")


if __name__ == "__main__":
    main()
