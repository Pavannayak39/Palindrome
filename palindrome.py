flag=1
i=0
x=input('enter something: ')
n=int(len(x))

while (i<=(n/2)):
    if (x[i]==x[n-i-1]):
        flag=1
        # print("palindrome")
    else:
        flag=0
        # print("Not palindrome")
        break
    i=i+1


if (flag==1):
    print('palindrome')
else:
    print('not palindrome')                

