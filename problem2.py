def count_word_occurrences(line):
    word_count = {}
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    lines = [
        "Python Course",
        "Deep Learning Course"
    ]

    output_filename = 'output.txt'

    try:
        with open(output_filename, 'w') as output_file:
            for line in lines:
                print(line)
                word_count = count_word_occurrences(line)
                for word, count in word_count.items():
                    print(f"{word}: {count}")
                    output_file.write(f"{word}: {count}\n")
                print()

        print(f"Output has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error writing to {output_filename}")

if __name__ == "__main__":
    main()
