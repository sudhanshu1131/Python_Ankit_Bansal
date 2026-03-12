#data structure
a = 2
b = 'CSK'
c = 'MI'
#data structure
#list
ipl = ['CSK', 'MI', 'RCB', 'LSG']
print(type(ipl))
#indexing
print(ipl[1])

#slicing
print(ipl[1:])

ipl[1] = 'KKR'
ipl.append('KKR') #add element at the end
ipl.insert(2,'MI') #insert element at particular index
ipl.extend([1,2]) # extent list with another list

ipl_string = "CSK,MI,KKR,LSG"
ipl_list= ipl_string.split(",")

# method 2 to create list
ipl_string = "CSK MI KKR LSG 1"
ipl_list= ipl_string.split(" ")

ipl_string = "CSK,|MI,|KKR,|.LSG"
ipl_list= ipl_string.split(",|")

#method 3

python_list = list('python ')

# to remove element at any index use pop..by default it removes last value
 ipl.pop(2)

num = [1,2,3,5,4]
print(sum(num))
print(min(num))

#tuple
#dictionary
# sort a list
num.sort()

# to get the index of particular value
num_str.index()

#list of list
list_of_list = [[1,2],[2,4],['Ankit','Rahul']]

ipl_new=ipl

ipl_copy=ipl.copy()

ipl=[[1,2],[3,4]]

#shallow copy
ipl_copy=ipl.copy()

# from python console:
>>> 1+2.0
3.0
>>> type(1+2.0)
<class 'float'>
>>> 5/2
2.5
>>> 5//2
2
>>> 5.5//2.2
2.0
>>> round(2.67)
3
>>> round(2.67,1)
2.7
>>> round(2.672,2)
2.67
>>> round(2.12,1)
2.1
>>> 3%2
1
>>> 7%3
1
>>> 12%2
0
>>> abs(-2)
2
>>> abs(2)
2
>>> abs(-2.0)
2.0
>>> abs(2.0)
2.0
>>> 2**3
8
>>> pow(2,3)
8
>>> pow(2,4)
16
>>> pow(2,-2)
0.25
>>> pow(2,4,2)
0
>>> 16%2
0
>>> pow(2,4,3)
1
>>> pow(2,10,3)
1
>>> 'aa'.upper()
'AA'
>>> a=2.0
>>> a.is_integer()
True
>>> a=2.1
>>> a.is_integer()
False
>>>











