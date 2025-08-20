import argparse
from duplicatedcontentchecker import ContentDuplicateChecker

def main():
    parser = argparse.ArgumentParser(
        description="Crawl un site et détecte le contenu dupliqué."
    )
    parser.add_argument(
        "url",
        help="URL de base du site à analyser (ex: http://127.0.0.1:31337/)"
    )
    parser.add_argument(
        "-d", "--max-depth",
        type=int,
        default=5,
        help="Profondeur maximale du crawl (défaut: 5)"
    )

    args = parser.parse_args()

    checker = ContentDuplicateChecker(base_url=args.url, max_depth=args.max_depth)
    checker.run()

if __name__ == "__main__":
    main()
