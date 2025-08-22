import argparse
from duplicatedcontentchecker import ContentDuplicateChecker


def main():
    parser = argparse.ArgumentParser(
        description="Crawl un site et détecte le contenu dupliqué."
    )
    parser.add_argument(
        "url", help="URL de base du site à analyser (ex: http://127.0.0.1:31337/)"
    )
    parser.add_argument(
        "-d",
        "--max-depth",
        type=int,
        default=5,
        help="Profondeur maximale du crawl (défaut: 5)",
    )
    parser.add_argument(
        "-o",
        "--output-path",
        type=str,
        default="/opt/haryon/duplicatedcontentchecker/duplicate_report.csv",
        help="Chemin du fichier CSV généré",
    )

    args = parser.parse_args()

    checker = ContentDuplicateChecker(
        base_url=args.url, output_path=args.output_path, max_depth=args.max_depth
    )
    checker.run()


if __name__ == "__main__":
    main()
