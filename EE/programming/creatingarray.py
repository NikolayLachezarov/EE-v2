import random


lst = []

with open("arrays.txt", "w") as f:
    for i in range(100):
        new_lst = []

        for j in range(10):
            new_lst2 = []
            for n in range(10):
                new_lst2.append(random.randrange(0, 1000))
            if n == 0:
                f.writelines(f"{new_lst2},", end=" ")
            elif n == 9:
                f.writelines(f"{new_lst2},")
        print("\n")


counter = 0
