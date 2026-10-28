import datetime

DAILY_TARGET_WORD_COUNT = 10

start = datetime.datetime.now()
print(start)

def main():
    target_wc = DAILY_TARGET_WORD_COUNT
    session_words = []
    elapsed_seconds = 0
    time_started = datetime.datetime.now()
    while len(session_words) < target_wc:
        #current_wc = len(session_words)
        print(" ".join(session_words))
        report_session(len(session_words), target_wc, elapsed_seconds)
        current_input = prompt("Type more words: ")
        if current_input[0].lower() in ["quit", "exit"]:
            break
        else:
            session_words += current_input
    print(" ".join(session_words))
    time_finished = datetime.datetime.now()
    session_timedelta = time_finished - time_started
    elapsed_seconds += round(session_timedelta.total_seconds(), 0)
    report_session(len(session_words), target_wc, elapsed_seconds)
    return len(session_words)

def prompt(message) -> list:
    raw_input = input(message)
    splitted = raw_input.split()
    filtered = list(filter(no_whitespace, splitted))
    return filtered

def report_session(wc: int, target_wc: int, elapsed_seconds: int) -> None:
    words_remaining = target_wc - wc if wc < target_wc else 0
    result = f"Current word count: {wc}. "
    if words_remaining > 0:
        result += f"{words_remaining} words remaining. "
    if elapsed_seconds > 0:
        result += f"Duration: {round(elapsed_seconds / 60, 1)} minutes."
    print(result)

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
