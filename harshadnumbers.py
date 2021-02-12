for num in range(int(input()),1000000001):
    harshad = 0
    for digit in str(num):
        harshad += int(digit)
    if num % harshad == 0:
        print(num)
        break
