from pathlib import Path


def count_words(file_path):
    text = Path(file_path).read_text(encoding="utf-8")
    return len(text.split())


def file_size(file_path):
    return Path(file_path).stat().st_size


def replace_word(file_path, old_word, new_word):
    content = Path(file_path).read_text(encoding="utf-8")
    updated = content.replace(old_word, new_word)
    Path(file_path).write_text(updated, encoding="utf-8")
    print(f"Replaced '{old_word}' with '{new_word}' in the file.")


def menu():
    print("\nUtility Tools")
    print("1. Count words in a file")
    print("2. Show file size")
    print("3. Replace one word with another")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            path = input("Enter file path: ")
            try:
                count = count_words(path)
                print(f"Word count: {count}")
            except FileNotFoundError:
                print("File not found. Please check the path.")

        elif choice == "2":
            path = input("Enter file path: ")
            try:
                size = file_size(path)
                print(f"File size: {size} bytes")
            except FileNotFoundError:
                print("File not found. Please check the path.")

        elif choice == "3":
            path = input("Enter file path: ")
            old_word = input("Enter word to replace: ")
            new_word = input("Enter new word: ")
            try:
                replace_word(path, old_word, new_word)
            except FileNotFoundError:
                print("File not found. Please check the path.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
