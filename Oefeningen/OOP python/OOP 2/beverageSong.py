 
def make_song(amount = 99, beverage = "soda"):
    for num in range(amount, -1, -1):
        if num == 0:
            yield f"No more {beverage}"
        elif num == 1:
            yield f"Only {num} bottle of {beverage} left!"
        else:
            yield f"{num} bottles of {beverage} on the wall"
        

kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
# print(next(kombucha_song)) # StopIteration

default_song = make_song()
print(next(default_song)) # '99 bottles of soda on the wall.'
