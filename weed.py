
DAILY_TARGET_WORD_COUNT = 10

def main():
    target_wc = DAILY_TARGET_WORD_COUNT
    session_words = []
    while len(session_words) < target_wc:
        current_wc = len(session_words)
        words_remaining = target_wc - current_wc
        print(" ".join(session_words))
        print(f"Current word count: {current_wc}. {words_remaining} words remaining.")
        current_input = prompt("Type more words: ")
        if current_input[0].lower() in ["quit", "exit"]:
            break
        else:
            session_words += current_input
        #split_input = current_input.split()
        #filtered_input = list(filter(not_empty_or_whitespace, split_input))
        #for word in split_input:
        #    if not_empty_or_whitespace(word):
        #        session_words.append(word)
    print(" ".join(session_words))
    return len(session_words)

def prompt(message) -> list:
    raw_input = input(message)
    splitted = raw_input.split()
    filtered = list(filter(no_whitespace, splitted))
    return filtered

def no_whitespace(text) -> bool:
    if text not in [" ", "\t", "\n", "\r", "\f", "\v", ""]:
        return True
    else:
        return False

#def not_empty_or_whitespace(word: str) -> bool:
#    assert type(word) == str
#    if len(word) == 0 or word in [" ", "\n"]:
#        return False
#    else:
#        return True


#def enstring_list(L: list) -> str:
    #result = ""
    #for word in L:
    #    result += word
    #return result

main()
