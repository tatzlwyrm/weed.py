# Write Every Effing Day
# Write Each & Every Day
# Make your words grow like weeds

# Weed.py is a simple, single-file Python editor to encourage and gamify
# a daily writing practice. 

# Prompts: what do you need to do this day/week? Write a to-do list. 
# What are you angry about?
# What can't you let go of.
# Imagine a new world. 
# Imagine a new life for yourself. 
# Tell me about the song that's stuck in your head. 

DAILY_TARGET_WORD_COUNT = 10 
SIGNIFICANCE_THRESHOLD = 400
# 600 is:
# * 15 minutes at 40 words per minute. 
# * 2.4 manuscript pages
# * 2 pages of a trade paperback novel. 
# * 1.5% of a short novel: novel in 67 days.
# * ~3 pages of a screenplay (3 minutes of screen time).
# 750 is:
# * 18.75 minutes at 40 words per minute. 
# * 3 manuscript pages
# * 3 pages of a mass-market paperback novel. 
# * 1.875% of a short novel: novel in 54 days. 

# In literary and academic publishing, a manuscript page is 250 words of 
# 12-point Courier or Times New Roman on letter paper with 1-inch margins. 

def main():
    target_wc = DAILY_TARGET_WORD_COUNT
    session_words = []
    while len(session_words) < target_wc:
        current_wc = len(session_words)
        words_remaining = target_wc - current_wc
        print(" ".join(session_words))
        print(f"Current word count: {current_wc}. {words_remaining} words remaining.")
        current_input = input("Type more words: ")
        split_input = current_input.split()
        #filtered_input = list(filter(not_empty_or_whitespace, split_input))
        for word in split_input:
            if not_empty_or_whitespace(word):
                session_words.append(word)
    print(" ".join(session_words))
    return len(session_words)

def not_empty_or_whitespace(word: str) -> bool:
    assert type(word) == str
    if len(word) == 0 or word in [" ", "\n"]:
        return False
    else:
        return True

main()
