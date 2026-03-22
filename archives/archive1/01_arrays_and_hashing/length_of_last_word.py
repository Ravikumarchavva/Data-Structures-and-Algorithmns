def length_of_last_word(s: str) -> int:
        last_word = s.strip().split(' ')[-1]
        return len(last_word)

if __name__ == "__main__":
    print(length_of_last_word("Hello World"))
    print(length_of_last_word("   fly me   to   the moon  "))
    print(length_of_last_word("luffy is still joyboy"))