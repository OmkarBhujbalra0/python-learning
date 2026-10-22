# for loop

for i in range(0,5):
    print("Print it 5 times.")

# for loop with steps

for i in range(1,11,4):
    print(i)

for i in range(121,22,-10):
    print(i)

# while loop

# while True:
#     print("*") # Keeps printing * without stopping.

a = 1

while a < 6:
    print(a)
    a+=1

# for loop with if-else

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is Even.")
    else:
        print(f"{i} is Odd.")

# while with if-else

a = 1

while a < 11:
    if a % 2 == 0:
        print(f"{a} is Even.")
    else:
        print(f"{a} is Odd.")
    a+=1

# break

a = 1

while True:
    if a > 10:
        break
    else:
        print(a)
    a+=1

# continue

for i in range(1,25):
    if i % 4 == 0:
        continue
    else:
        print(i)