
def main():
    with open('books/Frankenstein.txt', 'r') as f:
        data = f.read()
    print(data)

if __name__ == "__main__":
    main()