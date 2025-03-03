#3
numbers = iter(list(range(1, 101)))
for i in numbers:
    try:
        next(numbers)
        next(numbers)
        print(i)
    except StopIteration:
        break

#4

from itertools import combinations

def find_combinations_for_100(wallet):

    combinations_for_100 = []
    unique_combinations = set()

    bills = []
    for bill, count in wallet.items():
        bills.extend([bill] * count)

    for i in range(1, len(bills) + 1):
        for combo in combinations(bills, i):
            if sum(combo) == 100:

                sorted_combo = tuple(sorted(combo))
                if sorted_combo not in unique_combinations:
                    unique_combinations.add(sorted_combo)
                    combinations_for_100.append(list(combo))

    return combinations_for_100
wallet = {
    20: 3,
    10: 5,
    5: 2,
    1: 5
}

combinations = find_combinations_for_100(wallet)

if combinations:
    print("קומבינציות שיוצרות מאה דולר:")
    for combo in combinations:
        print(combo)
else:
    print("לא נמצאו קומבינציות שיוצרות מאה דולר.")



#5
class library:
    def __init__(self):
        self.books_list = []
        self.index = -1

    def add_book(self, new_book):
        self.books_list.append(new_book)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.books_list) - 1:
            raise StopIteration()
        self.index += 1
        return self.books_list[self.index]

booksi=library()
booksi.add_book("bbbbb")
booksi.add_book("cccccc")
booksi.add_book("nnnnn")
for b in booksi:
 print(b)