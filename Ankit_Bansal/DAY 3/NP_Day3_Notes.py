#tuple
a = (1,2,3)
# tuples are immutable
#a[1] = 5
a=('CSK','MI')

#dictionaries

#ipl = ['CSK','MI','RCB']

#ipl = [['CSK','Chennai Super Kings'],['MI','Mumbai indians']]

ipl = {
"CSK" : "Chennai Super Kings",
"MI" : "Mumbai Indians"
}

ipl["CSK"]

ipl["GT"] ="Gujrat Titans"
ipl["CSK"]="Chennai"

del ipl["CSK"]

ipl = {
"CSK" : {"Name":"Chennai Super Kings","captain":"MSD"},
"MI" : {"Name":"Mumbai Indians","captain":"Rohit"},
"RCB" : {"Name":"Royal Challengers bangalore"}
}

ipl1 = {
"CSK" : {"Name":"Chennai Super Kings","captain":["MSD","Jadeja"]},
"MI" : {"Name":"Mumbai Indians","captain":"Rohit"},
"RCB" : {"Name":"Royal Challengers bangalore"}
}
############################
list=[1,2]
tuple=(1,2)
dictionaries={"key":"value"}
############################
#strings #numbers #boolean
#control flow using if else
# less than 30 -> fail , else pass
marks=-20
if marks < 30 :
    print("fail")
    print(f"marks are {marks}")
elif marks >=30 and marks < 60:
    print("pass with second division")
elif marks >=60 and marks < 75:
    print("pass with first division")
else:
    print("pass with distinction")
print("this is outside if")

if "CSK" in ipl :
    print("CSK is there")
else:
    print("CSk is not there")
print("this is outside if")

# loops
num_square=[]
num=[1,2,3]
num_square.append(num[0]**2)
num_square.append(num[1]**2)

#while
num_square=[]
n=0
while n < len(num) :
    print(f"it is still less than 5 iteration number {n}")
    num_square.append(pow(num[n],2))
    n=n+1
# for loops

num_square=[]
for n in num :
    num_square.append(pow(n, 2))
    print(n)

#[1,2,3]
num_square=[]
for n in range(len(num)):
    print(f"it is still less than 5 iteration number {n}")
    num_square.append(pow(num[n], 2))

#range -> [0,1,2]
name1=["CSK","MI_SUPER","RCB"]
len_team = []
for i in name1:
    print(i)
    len_team.append(len(i))









