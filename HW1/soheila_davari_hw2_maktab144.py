#2
def divisors(number):
    num_divisors=[]
    for i in range(1,number+1):
        if number%i==0:
            num_divisors.append(i)
    return(num_divisors)


nums=[]
for i in range(3):
    user_num=(int(input(f"num{i+1}= ")))
    nums.append(user_num)

prime_sum=0
for num in nums:
    counter=0
    if num>2:
        for i in range(2, num):
            if num% i==0:
                counter+=1
            else:
                continue
    if counter==2:
        prime_sum+=num
print(divisors(prime_sum))
