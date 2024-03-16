tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total


if __name__ == "__main__":
    print("Tom's total expense", calculate_total(tom_exp_list), sep=" ")
    print("Joe's total expense", calculate_total(joe_exp_list), sep=" ")
