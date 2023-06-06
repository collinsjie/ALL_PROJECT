# # # # try:
# # # #     age = int(input('Enter your age.'))
# # # # except ValueError:
# # # #     print('you entered an alphabet, but you can enter a number')
# # # # else:
# # # #     #print('you are [age] year old')
    
# # # #finally:
# # #     #print('You are done')
# # # #while True:
# # #     #age = input('')
# # #     #if type(age)== int:
# # #         #print('you are [age] years old')
# # #     #else:q
# # #         #print('wrong input')
        
# # # age = input()
# # # try:
# # #     age=int(age)
# # # except valueerror:
# # #     print('wrong input type')
# # # else:
# # #     print(age)
# # #for i in range(1,10,2):
# #     #print(i)
#for row in range(1, 13,):
    #for col in range(1, 13,):
        #print(f'{row} X {col} =  {row*col}', end="")
#print('\n')

# num =1
# while num <= 12:
#     for i in range(1,13):
#         print(f'{i}x{num} = {i*num}', end="\t")
#     print('\n')
#     num += 1

    
    
        
       
# # Age = 3
# # print(f'You are {Age} years old')
# # print('You are {}of age'.format(Age))
# # print('You are %s at %d' %('fool', Age))


# Num = int(input("Enter the number you want to generate a multiplication table: "))
# if 1<=Num<=3:
#     MyRange = range(1,13)
#     for x in MyRange:
#         result = Num * x
#         print(Num," * ",x," = ",result)

# import random

# customers = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
# dict_discount={customer:random.randint(1,100 ) for customer in customers}
# print(dict_discount)

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
print(size, 'characters copied.')
fhand.close()
even_numbers = list(range(2, 27, 2))

# create a list of alphabets
alphabets = list('abcdefghijklmnopqrstuvwxyz')

# create a dictionary that pairs alphabets with even numbers
pair_dict = {alphabet: number for alphabet, number in zip(alphabets, even_numbers)}

print(pair_dict)


