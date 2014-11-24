num = raw_input("Enter a number:")

num = int(num)

for i in range(2, num):
    if num%i == 0:
        print("not prime.")
        exit(0)
        

print("prime.")