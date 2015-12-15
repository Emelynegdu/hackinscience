bob = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
alice = ['IV', 'III', 'II', 'XX', 'II', 'XX']
def love_meet(bob, alice):
    for i in set(bob):
        for j in set(alice):
            if i == j:
                print(i)



love_meet(bob, alice)
