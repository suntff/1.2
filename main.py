a,b,c = int(input()),int(input()),int(input())
counter = 0
if a==b and b==c and a==c:
    counter=3
elif b==a or a==c or b==c:
    counter=2
else:
    counter = 0
print(counter)