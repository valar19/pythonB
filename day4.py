#evaluate
'''
a='8 plus 2 minus 4 div 2 mul 2'
a=a.replace('plus','+').replace('minus','-').replace('div','/').replace('mul','*')
eval(a)
print(eval(a))
'''
#for loop
'''
a=[10,20,30,40,50]
b=10
for i in range(0,b):
    print(i,end='')
print('')
for i in range(b-3,-1,-1):
    print(i,end='')
'''
'''
a=[10,20,30,40,50]
for i in a:
    print(i,end='')

for i in range(2):
    print(a[i],end='')
'''
'''
a=[10,20,30,40,50,60,70,80,90,100]
for i in range(len(a)):
    print(a[i])
'''
    
#nested for loop
'''
for i in range(5):
    for j in range(5):
        print(i,j,end='|', sep=',')

'''
#find length
'''
a=[2,3,2,9,3,3,1,6]
count=0
for i in a:
    count=count+1
print(count)
'''
#sum
'''
a=[2,3,2,9,3,3,1,6]
sum=0
for i in a:
    sum=sum+i
print(sum)
'''
#count
'''
a=[2,3,2,9,3,3,1,6]
count=0
b=int(input('enter the value '))
for i in a:
    if i==b:
        count+=1
        print(count)
'''
#sum wit string
'''
a=[2,'string',9,3,3,1,6]
sum=0
for i in a:
    if type(i)==int:
        sum=sum+i
print(sum)
'''     
#max value
a=[2,'string',9,3,3,1,6]
