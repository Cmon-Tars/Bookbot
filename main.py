
def sort_on(dict):
    return dict["number"]

def main():
    with open('books/Frankenstein.txt', 'r') as f:
        data = f.read()
        data = data.lower()
    words = data.split()
    chars = [c for c in data]
    countsForReport = []
    for char in set(chars):
        if char.isalpha():
            counts = {}
            matches = [x for x in chars if x == char]
            counts["char"] = char
            counts["number"] = len(matches)
            countsForReport.append(counts)
    countsForReport.sort(reverse=True, key = sort_on)

    message = f"--- Begin report of books/frankenstein.txt --- \n{len(words)} words found in the document \n"
    for i in countsForReport:
        message += f"\nThe '{i["char"]}' character was found {i["number"]} times"
    message += "\n--- End report ---"
    print(message)


if __name__ == "__main__":
    main()