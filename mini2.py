"""def calculate_grade(marks):
    if marks>=90:
        grade= 'A'
    elif marks>=80:
        grade='B'
    elif marks>=70:
        grade='C'
    elif marks>=60:
        grade='D'
    else:
        grade='F'
    return grade

print(calculate_grade(77))
print(calculate_grade(90))
print(calculate_grade(30))"""

"""def check(password):
    if len(password)>8:
        strength='strong'
    else :
         strength='weak'
    return strength

print(check('pty'))
print(check('thutwsf42631567'))"""

def countvowels(text):
    count=0
    for char in text:
        if char in "aeiou":
            count=count+1
    return count

print(countvowels('hello'))
print(countvowels('engineering'))
