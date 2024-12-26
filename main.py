def char_count(text):
    chardict = {}
    text = text.lower()
    for i in text:
        if not i.isalpha():
            pass
        elif i in chardict:
            chardict[i] += 1
        else:
            chardict[i] = 1
    return chardict

def word_count(text):
    count = 0
    word_list = text.split()
    for i in word_list:
        count += 1
    return count

def report(text):
    chardict = char_count(text)
    sorteddict = {}

    for i in sorted(chardict, key=chardict.get, reverse=True):
        sorteddict[i] = chardict[i]

    print(f"\n--- Begin report of books/frankenstein.txt ---\n{word_count(text)} words found in document\n")

    for i in sorteddict:
        print(f"the '{i}' character was found {sorteddict[i]} times.")

    print("--- End report ---")

def main():

    with open("books/frankenstein.txt") as f:
        content = f.read()

    report(content)

main()