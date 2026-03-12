#loops dict
#continue, break
#list comprehentions
#exception handling
#working with files
#ipl= ["CSK","MI"]
# ipl = {
# "CSK" : "Chennai Super Kings",
# "MI" : "Mumbai Indians"
# }
# print(ipl.items())
# for team in ipl:
#     print(team)
#     print(ipl[team])
#
# for team,name in ipl.items():
#     print(team)
#     print(name)
#
# ipl= ("CSK","MI")
# team1=ipl[0]
# team2=ipl[1]
#
# team1,team2= ("CSK","MI")

#ipl= ["CSK","MI","KKR"]

# for team in ipl:
#     if team == "MI":
#         break
#     print(team)

# for team in ipl:
#     if team == "MI":
#         continue
#     print(team)

#list comprehention
# ipl= ["CSK","MI","KKR"]
# ipl_len=[]
# for team in ipl:
#     if len(team)>2:
#         ipl_len.append(len(team))

#ipl_len_com = [len(team) for team in ipl]
#ipl_len_com = [len(team) for team in ipl if len(team)>2]

# error handling / exception handling
# print(1)
# a = 1/0
# print(2)

try :
    print("this is try block")
    a = 1/0
    print(a)
except Exception as e:
    print("this is exception block")
    print(e)
else :
    print("this is else block")
finally:
    print("this is finally block")

#working with files
f = open("test.txt",'r')
#f.read()
for a in f:
    print(a)
f.close()

with open("test.txt",'r') as f:
    for line in f:
        print(line)


line="1,ankit".split()
2,rahul

f = open("test.txt",'w')
f.write("this is first line in write mode")
f.close()


f = open("test.txt",'a')
f.write("this is first line in write mode \n")
f.write("this is first line in write mode 1")
f.close()
f = open("test.txt",'r')
f_list=f.readlines()
f.close()









