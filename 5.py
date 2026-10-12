"""numbers=[3,4,5,6,8]
rev=numbers[::-1]
print(rev)"""

"""numbers=[3,8,8,6,5,3,4,9,2,2,4,4,8]
unique=[]
for n in numbers:
    if n not in unique:
        unique.append(n)
        print(unique) """

"""numbers = [12, 45, 23, 45, 67, 67, 34]

unique=[]

# Remove duplicates
for n in numbers:
    if n not in unique:
        unique.append(n)

# Find the largest and second-largest
largest = float('-inf')
second_largest = float('-inf')

for n in unique:
    if n > largest:
        second_largest = largest
        largest = n

    elif n > second_largest and n != largest:
        second_largest = n

print("Unique numbers:", unique)
print("Second-largest number:", second_largest)"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even=[]
for n in numbers :
    if n%2==0:
        even.append(n)

print(even)
squares=[n*n for n in even]
print(squares)