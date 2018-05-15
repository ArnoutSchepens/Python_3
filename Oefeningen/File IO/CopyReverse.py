
def copy_and_reverse(old_file, new_file):
    with open(old_file, "r") as old_f:
        text = old_f.read()

    with open(new_file, "w") as new_f:
        new_f.write(text[::-1])

    

copy_and_reverse('story.txt', 'story_reversed.txt')