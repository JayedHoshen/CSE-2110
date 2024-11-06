#write a python code that takes a user input N. Then create a dictionary named prime_status where the keys are odd 
#numbers within the range from 1 to N, and the values are Boolen values indicating whether each number is prime or not. 
#Now print the data of that dictionary. To solve the above task, you have to define a function is_prime(n) that checks if 
#a given number n is prime or not.


def is_prime(n):
    flag = True
    for i in range(2, n):
        if(n%i == 0): 
            flag = False
            break
        else:
            flag = True
    return flag

n = int(input("Enter a number, N: "))
print(is_prime(n))

prime_status = {}
for i in range(1, n):
    if(i%2): prime_status
