#3
def most_frequency(list_args):
    max_count=0
    most_repeated=None

    for i in list_args:
        if list_args.count(i)>max_count:
            max_count = list_args.count(i)
            most_repeated=i
    return max_count , most_repeated


user_nums=[]
while True:
    num=input("enter numbers(use end to finish): ")
    if num=="end":
        break
    user_nums.append(int(num))

print(most_frequency(user_nums))

    