# mylist=[1,2,3,4,5,6,7,8]
# newlist=[]
# for i in mylist:
#     if i**2%2==0:
#         newlist.append(i**2)
# print(newlist)

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blastoff!')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')
        
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')

# shipping = {1500: ['egbeda', 'ikotun', 'igando'], 
#             3000: ['ikate','osapa', 'Lekki'], 
#             2500: ['agidingbi', 'acme', 'awolowo'],
#             }
# # Location= input('Your location:')
# # Location.lower()
# # fee=0
# # for key, value in shipping.items():
# #     if Location in value:
# #         fee = key
# #         print(f' The fee for {Location} is {fee}')
# #     else:
# #         print(f"Sorry,we don't deliver in {Location}:")

# shipping.update({'E':'F'})
# print(shipping)



# Staff = ['Tunde', 'Frank', 'Dare']
# Salary=[1000, 2000, 3000]
# staff_salary = {Staff[i]:Salary[i] for i in range(len(Salary))}
# print(staff_salary)



# alphabets = input('>')
# even_numbers = list(range(2,len(alphabets)*2+1,2))
# pair = {alphabet: number for alphabet, number in zip(alphabets, even_numbers)}
# print(pair)

# string=input('>')



# even= list(range(2,len(string)*2 +1,2))
# mydict={string[i]:even[i] for i in range(len(string))}


# ndict={}
# {ndict.update({string[i]:even[i]}) for i in range(len(string))}
# print(ndict)

# print(mydict)

# Seq={'a','b','c','d','e','f','g'}
# list1=(2,3)
# result=dict.fromkeys(Seq, list1)
# print(result)

# def getInteger():
#     result = int(input("Enter integer: "))
#     return result
# getInteger()

# strings= input('>')
# pair={strings[i]:even for even in range(2,len(strings)*2+1,2), for i in range(len(strings))}
# print(pair)


# my_set={1,2,3,3,4,7,1,2}
# #if 7 in my_set:
# for num in my_set:
#     if num==7:
#         print(num)
# my_dict={'tude:30, collins:50, ojo:40'}
# 30 in my_dict
# print('present')
# Attendence=[('Ade',7),('Tolu',3),('Zle',7),('Zle',14),('Ade',5),('Ade',7),('Tolu',7)]
# Employees=set()
# for i in Attendence:
#     Employees.add(i[0])
# #print(Employees)
# total_hours=dict().fromkeys(Employees,0)
# for tup in Attendence:
#     for employee in total_hours:
#         if tup[0]==employee:
#             total_hours[employee]+=tup[1]
# print(total_hours)
# def biology():
#     print('biology is .......')
# def say_hi(name):
#     return 'Hi', name
# # say_hi('victor')
# A=say_hi('victor')
# print(A)
# print(A[1])

# import keyword
# print("The list of keywords is : ", keyword.kwlist)

# if 's' in 'geeksforgeeks':
#     print("s is part of geeksforgeeks")
# else:
#     print("s is not part of geeksforgeeks")
 
# using "in" to loop through
# for i in 'geeksforgeeks':
#     print(i)
 
#print("\r")
    
# loop 1 to 10
# loop from 1 to 10

    
# i=0
# while i < 10:
#     if i ==6:
#         break
#     print(i)
#     i+=1
#     #print(i)

# def fun():
#     S = 0
 
#     for i in range(10):
#         S += i
#     return S 
# print(fun())

# def fun():
#     S = 0
 
#     for i in range(10):
#         S += i
#         yield S
# for i in fun():
#     print(i)
# def inf_sequence():
#     num = 1
#     while True:
#         yield num
    
#         num += 1
         
# for i in inf_sequence():
#     if i ==1000:
#         break
#     print(i, end=' ')
    
# pi = 'global pi variable'
# def inner():
#     pi = 'inner pi variable'
#     print(pi)
  
# inner()
# #print(pi)

#a = 5
 
# printing value of a
# text = "X-DSPAM-Confidence:    0.8475"
# web =text.find(':')
# print(web)
# num=text[web+1:]
# print(num)
# col=float(num)
# print(col)

# x = [int(x) for x in input("Enter multiple value: ").split(",")]
# print("Number of list is: ", x)

# fname = input("Enter file name: ")
# try:
#    fh = open(fname)
# except:
#     print('file not found:error')
#     quit()
    
# text=fh.read()
# res=text.upper()
# print(res.rstrip())

# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# total = 0
# for line in fh:
#     if line.startswith("X-DSPAM-Confidence:"):
#         count += 1
#         num_pos = line.find('0')
#         num = float(line[num_pos:])
#         total += num
# average = total / count
# print("Average spam confidence:", average)

# def myFun(*argv):
#     for arg in argv:
#         print(arg, end=' ')
 
 
# myFun('Hello,', 'Welcome', 'to', 'GeeksforGeeks',)

# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
 
 
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     print(line.rstrip())

# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
    
    
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     word_split = line.split()
#     for word in word_split:
#         if word not in lst:
#             lst.append(word)
#         else:
#             continue

# print(sorted(lst))

# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# for line in fh:
#     line=line.rstrip()
#     if line.startswith('From:'):
#         print(line[5:])
#         count = count + 1
# print('There were', count, 'lines in the file with From as the first word')
        

# count = 0
# with open('mbox-short.txt') as f:
#     for line in f:
#         if line.startswith('From ') and not line.startswith('From:'):
#             words = line.split()
#             print(words[1])
#             count += 1

# print('There were', count, 'lines in the file with From as the first word')


# def show_election_result(scores):
# #         # for key, value in scores.items():
#     winner_value= max(scores.values())
#     winner_key=max(scores, key=scores.get)
#     print(f'winner_key:{winner_key}')
#         #if scores[key] == winner:
#             #winner_cad = key
#     return f"The winner of 2023 presidential election is {winner_key} with the total votes of  {winner_value}"
# scores = {"Atiku": 1000,"Tinubu": 900,"Obi": 1200,"Sowore": 500,"Kwankwaso": 800,
# }
# print(show_election_result(scores))
# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
 
# # Driver function to test above function
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# reverseList(A, 0, 5)
# print("Reversed list is", A)


# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# lst = list()

# for line in handle:
#     if not line.startswith("From:"): continue
#     line = line.split()
#     lst.append(line[1])

# counts = dict()
# for word in lst:
#     counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items(): 
#     if bigcount is None or count > bigcount:
#         bigcount = count
#         bigword = word

# print (bigword,bigcount)

    
 
    
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# d=dict()
# for line in handle:
#     if not line.startswith("From "): 
#         continue
#     else:    
#         line=line.split()
#         line=line[5]
#         line=line[0:2]
#         d[line]=d.get(line,0)+1

# lst=list()        
# for value,count in d.items():
#     lst.append((value,count))

# lst.sort()
# for value,count in lst:
#     print(value,count)

# competitors= {'Victor':[20.0], 'Tund':[30,0], 'Shalom':[10,0]}

# def is_winner(competitors):
#     winner_value=0
#     winner_key= ''
#     for key,value in competitors.items():
#         if value>winner_value:
#             winner_value=value
#             winner_key=key
#         return f'The winner is {winner_key}'
# print(is_winner('competitors'))


# def is_winner(competitors):
#     winner_value = 0
#     winner_key = ''
#     for key, value in competitors.items():
#         if value[0] > winner_value:
#             winner_value = value[0]
#             winner_key = key
#             return f'The winner is {winner_key}'
        
#     def top_up(winner):
#         competitors[winner][1] += 100000
#         return competitors[winner][1]
# competitors = {'Victor': [20.0], 'Tund': [30, 0], 'Shalom': [10, 0]}
#     print(top_up(winner))
# print(is_winner(competitors))


# def is_winner(competitors):
#     winner_value = 0
#     winner_key = ''
#     for key, value in competitors.items():
#         if value[0] > winner_value:
#             winner_value = value[0]
#             winner_key = key
#     return winner_key

# def top_up(fn, competitors):
#     # fn=is_winner
#     # fn()
#     winner=fn(competitors)
#     competitors[winner][1] += 100000
#     return competitors[winner][1]

# competitors = {'Victor': [20.0], 'Tund': [30, 0], 'Shalom': [10, 0]}
# prize=(top_up(is_winner, competitors))
# print(prize)

# def is_not_empty(lst):   
#     assert len(lst)!=0, 'lst is empty'
#     return True
# lst=[]
# lst1=[1,2,3]
# b=is_not_empty(lst1)
# print(b)
# A=is_not_empty(lst)
# total=1
# def func():
#     total=30
#     def func1():
#         nonlocal total
#         total+=1
#         return total
#     return func()
# print(func())

# class Solution:
#     def lovelyCards(self, n, cards):
#         sorted_cards = sorted(cards)
#         for i in range(n):
#             if sorted_cards[i] != i + 1:
#                 return 0
#         return 1
# solution = Solution()
# n = 3
# cards = {2, 1, 4}
# output = solution.lovelyCards(n, cards)
# print(output)

# import re
# import urllib.request

# # Read the file from the URL
# url = "http://py4e-data.dr-chuck.net/regex_sum_1786009.txt"
# response = urllib.request.urlopen(url)
# data = response.read().decode()

# # Find all numbers in the file using regular expression
# numbers = re.findall('[0-9]+', data)

# # Convert the extracted strings to integers and calculate the sum
# total_sum = sum(int(num) for num in numbers)

# print("Sum:", total_sum)

# a,b,c,d,e = (1,2,3,4,5,)
# print(a,b,c,d,e)
# def small(name, *nums): 
#     print('name:', name)
#     for number in nums:
#         print(number, end='')
# small('victor', 1,2,3,4)
# def median(*nums):
#     len_nums=len(nums)
#     nums=sorted(nums)
#     a,*b=nums
#     if len_nums%2==0:
#         if type(a) is str:
#             return nums[(len_nums//2)-1],nums[(len_nums//2)]
#         else:
#             result=(nums[(len_nums//2)-1]+nums[(len_nums//2)])/2
#             return (nums[(len_nums//2)-1]+nums[(len_nums//2)])/2
#     return nums[(len_nums//2)]
# print(median('a','b','c','t','d'))

# def fav(**kwargs):
#     for value in kwargs.values():
#         print(value)
# fav(victor=1, dan=2,bosun=17)
import urllib.request, urllib.parse, urllib.error



    
    