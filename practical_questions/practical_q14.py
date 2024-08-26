# import random as r
#
# rec1 = []
# rec2 = []
#
# def dice_roll():
#     for i in range(10):
#         rec1.append(r.randint(1, 6))
#         rec2.append(r.randint(1, 6))
#
# def outcome_sum():
#     print("1st dice o/p sum: ", sum(rec1))
#     print("2nd dice o/p sum: ", sum(rec2))
#     print("Both dice o/p sum: ", sum(rec1)+sum(rec2))
#
# dice_roll()
# outcome_sum()


# LOGIC -2

import random as r
for i in range(1, 11):
    total = r.randint(1, 6) + r.randint(1, 6)
    print(f"Roll {i}: Total = {total}")
