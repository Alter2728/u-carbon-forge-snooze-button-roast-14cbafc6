from pathlib import Path

TEXT = "It's 6 AM on a Saturday — even my responsibilities are still asleep, so why are you screaming?"


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")
    assert output_path.read_text(encoding="utf-8") == TEXT


if __name__ == "__main__":
    main()
