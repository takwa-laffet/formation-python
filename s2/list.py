count = 0
num = 2
while count < 20:
    is_prime = True
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
