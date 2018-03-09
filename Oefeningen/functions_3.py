
def speak(animal='dog'):
    noises = {
        'dog': 'woof',
        'pig': 'oink',
        'duck': 'quack',
        'cat': 'meow'
    }
    noise = noises.get(animal)
    if noise:
        return noise
    return '?'

# print(speak('pig'))



global_int = 10

def hello():
    # local_int = 0
    # print(f"global_int = {global_int}")
    # print(f"local_int = {local_int}")

    global global_int
    global_int += 1
    print(f"global_int = {global_int}")

hello()
print(global_int)