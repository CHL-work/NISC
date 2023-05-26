def count_occurrences(text):
    count_dict = {}
    for char in text:
        if ord(char) in range(128):  # only ASCII characters
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1

    # Convert dictionary to list of tuples and sort it by ASCII value
    sorted_tuples = sorted(count_dict.items(), key=lambda x: ord(x[0]))
    return sorted_tuples

def main():
    print(count_occurrences("Typical Sentence"))

if __name__ == "__main__":
    main()