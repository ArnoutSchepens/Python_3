
def statistics(file_name):
    with open(file_name, "r") as f:
        text = f.read()

        return {"lines": text.count("\n") + 1,
                "words": len(text.split()),
                "characters": len(text)}


print(statistics('story.txt'))
