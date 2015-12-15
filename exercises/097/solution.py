bob = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
alice = ['IV', 'III', 'II', 'XX', 'II', 'XX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']


def love_meet(bob, alice):
    for i in set(bob):
        for j in set(alice):
            if i == j:
                print(i)


love_meet(bob, alice)


banane = []


def affair_meet(bob, alice, silvester):
    for i in set(bob):
        for j in set(alice):
            for k in set(silvester):
                if k == i:
                    if k != j:
                        if k not in banane:
                            banane.append(k)
                            print(k)


affair_meet(bob, alice, silvester)
