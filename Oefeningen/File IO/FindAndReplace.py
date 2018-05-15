
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as f:
        old_text = f.read()
        new_text = old_text.replace(old_word, new_word)
        f.seek(0)
        f.write(new_text)
        f.truncate()



find_and_replace('story_copy.txt', 'Alice', 'Colt') 