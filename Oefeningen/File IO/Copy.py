
def copy(old_file, new_file):

    with open(old_file, "r") as old_f:
        data = old_f.read()

    with open(new_file, "w") as new_f:
        new_f.write(data)


copy("story.txt", "story_copy.txt")