# prime number check
num=int(input('enter number' ))
fiag=0
for i in range(2, num):
    if num% i== 0:
        flag=1
        break
if fiag==0 and num> 1:
    print('prime')
else:
    print('not prime')
