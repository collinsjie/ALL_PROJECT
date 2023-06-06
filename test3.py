
# # Victor = 'short'
# # Age= 0
# # while Age<=12:
# #     Age += 1
# #     if Age>12:
# #         Victor= 'tall'
# #         print(f'Victor is {Victor} at age {Age}' )

# # print('it\'s alright')
# # print('My mother\'s son')
# # print('my monther\\son')
# # print('Hello\nworld')
# # print('Hello \bworld')

# # my_list= list((1,2,3))
# #my_list= list('1,2,3')
# #print(my_list)
# #my_list= [1,2,3]
# #print(my_list)
# #print(len(my_list))

# # print(list(range(1,21)))
# # #range(1,21)
# # my_list = [1,(1,2,3,), 'ogo', {'2':'Boy'}]
# # #print(my_list[-1])
# # for item_index, item in enumerate(my_list):
# #     print(item_index, item)
# # num = 0
# # for item in my_list:
# #     print(item, num)
# #     num += 1
# # my_list.extend([-3,4])
# # print(my_list)
# def item(count):
    

# A = [1, 2, 3, 4, 5, 6, 7, 8, 2, 5]
# # lst= dict.fromkeys(my_list)
# # lst=list(lst)
# # print(lst)
# # for item in my_list:
# #     if my_list.count(item) > 1:
# #         my_list.remove(item)
# # print(my_list)
# B = list(filter(item, A))
# print(my_list)

# # my_list = ['mr', 'victor']
# # ' '.join(my_list)
# # print(my_list)

# mylist = [1, 2, 3, 4, 5, 6, 7,]
# #for index, item in enumerate(mylist):
#     #print(index, item)
# mydict=dict(enumerate(mylist))
# print(mydict)

# def evenodd(number):
#     evenlist = []
#     oddlist =[]
#     for number in range(int(1,50)):
#         for i in number:
#             if i %2==0:
#                 evenlist.append(i)
#             else:
#                 oddlist.append(i)
#     print('Even list', evenlist)
#     print('Qdd list', oddlist)  
# evenodd(number) 
# def evenodd():
#     evenodd = int(input('Enter number:'))
#     if evenodd %2 ==0:
#         evenlist = []
#         evenlist.append(evenodd)
#         print('This is evenlist:', evenlist)
#     elif evenodd %2 !=0:
#         oddlist = []
#         oddlist.append(evenodd)
#         print('This is oddlist:', oddlist)
#     else:
#         print('None')
# evenodd()
    
#     Account_balance ={'victor':10000, 'david':19, 'frank':30000}
# for key in Account_balance:
#         Account_balance[key ]+=20000
# print(Account_balance) 


# mydict = {"brand": "Ford", "electric": False, "year": 1964,"colors": ["red", "white", "blue"]}
# mydict['country']='norway'
# x=mydict.items()
# print(x)

# myfamily = {"child1" : {"name" : "Emil", "year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus",
#     "year" : 2011
# }}     
# print(myfamily)       
            
# family = {'agbadu':{'children':['ofure', 'osose', 'omeg']}, 'parent':{'father':'collins', 'mother': 'racheal'}}
# print(family)


# mydict = {'a':100,'b':200}
# for key in mydict.keys():
#     mydict[key]+=200
#     #print(mydict)
# newdict = {mydict[key+=200 for key in mydict.keys()]}
# newdict = {key:mydict[key]+200}
# print(mydict)

# def reverselist(A,start, end):
#     while start <end:
#         A[start], A[end] = A[end], A[start]
#         start +=1
#         end -=1
# A=[1,2,3,4,5,6,7,8]
# print(A)
# reverselist(A,0,7)
# print('The Reversel is:', A)


# def reverseList(A):
#   print( A[::-1])
     
# # Driver function to test above function
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# print("Reversed list is")
# reverseList(A) 
    
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)




      




        
    
    