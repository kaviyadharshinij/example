#array declare
import array
s=array.array('i',[1,2,3])
print(s)
print(type(s))
#import *
'''from array import *
s=array('f',[10.20,23.4,56.34])
print(s)
#import using alis name
import array as ar
s=ar.array('d',[32.54,23.9,23.0])
print(s)
#unicode charecer
from array import *
s1=array('u','c c++')
print(s1)
#for loop
from array import *
s=array('u',['C','b','p'])
for x in s:
    print(x,end='')
#append
x=array.array('l',[17,24,56,67])
x.append(19)
print(x)
#extend
x.extend([11,33,74])
print(x)
#insert
x.insert(5,77)
print(x)
#remove
x.remove(11)
print(x)
#pop
x.pop()
print(x)
#pop
x.pop(2)
print(x)
#sort not available
#percentage of mark using array
from array import  *
lst=[int(i)for i in input('Enter the mark:').split(',')]
marks=array('i',lst)
sum=0
for x in marks:
    sum+=x
print('Total mark:s',sum)
n=len(marks)
percentage=sum/n
print("percentage of a mark:",percentage)'''
#find the position
from array import *
x=array('I',[])
print('How many elements:',end='')
n=int(input())
for i in range(n):
    print('Enter the elements:',end='')
    x.append(int(input()))
print("Original array",x)
print('Enter the elements to search',end='')
s=int(input())
try:
    pos=x.index(s)
    print("Found at position:",pos)
except ValueError:
    print('Not found in the array')


    



