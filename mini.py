maths=int(input("enter the maths score:"))
physics=int(input("enter the physics score:"))
chemistry=int(input("enter the chemistry score:"))
score=[maths,physics,chemistry]
total=sum(score)
print(total)
average=total/len(score)
print(average)
highest=max(score)
lowest=min(score)
print(highest)
print(lowest)
if average>=90:
    grade="A+"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
elif average>=50:
    grade="D"
else:
    grade="F"

print(grade)
print("total:",total)
print("average:",average)
print("highest score:",highest)
print("lowest score:",lowest)
print("grade:",grade)