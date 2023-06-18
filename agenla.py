# print('Day 1 - string manipulation')
# print("string concatenate is done with the '+' sign.")
# print('e.g print("Hello" + " " + "Collins")')
# print('New line can be created with backlash and n.')
# print('Hello. ' + input('What is your name?'))
# name = input('what is your name?')
# print('my is:', name)
# print(len(name))

# a = input('enter a number:' )
# b = input('enter second number:' )
# print('a:', a)
# print('b:', b)

# print('Welcone to band name generator')
# city= input('What  is the name of the city you grow up in?\n' )
# pet=input('what is the name of a pet?\n' )
# print('Your band name could be ' + city +" " +pet)

# two_digital_number = input('enter your age:')
# first_digital_number= two_digital_number[0]
# second_digital_number=two_digital[1]
# result= int(first_digital_number) + int(second_digital_number)
# print(result)

# height=input('enter your height:')
# weight=input('enter your weight:')
# BMI = int(weight)/(int(height)**2)
# print(BMI)

# age=input('enter your age:')
# maximum_age=90*365
# age= int(age) *365
# days_live=maximum_age-age
# remaining_years_live= days_live/365
# print(remaining_years_live)


# print(f'You have {days_remaining} days, {weeks_remainin} weeks,{months_remainin} Months,{years_remaining} years')
# print(maximum_age)

# year= int(input('enter the year you want to check: '))
# if year %4==0:
#     if year %100==0:
#         if year %400==0:
#             print('leap year.')
#         else:
#             print('not leap year.')
#     else:
#         print('leap year.')
# else:
#     print('not leap year.')    

# student_heights=[120, 150, 145, 167, 186, 137]
# total_heights=0
# for height in student_heights:
#     total_heights+=height
# number_of_student=0
# for number in student_heights:
#     number_of_student+=1
# average_height_of_student=round(total_heights/number_of_student)
# print(average_height_of_student)

# student_scores=[78,65,89,86,55,91, 89]
# highest_score=0
# for score in student_scores:
#     if score >highest_score:
#         highest_score=score
# print('the highest is:', highest_score)


# for number in range(1, 101):
#     if number %3==0 and number %5==0:
#         print('fizzbuzz')
#     elif number %3==0:
#         print('fizz')
#     elif number %5==0:
#         print('buzz')
#     else:
#         print(number)
    
import random
# word_list=['lagos', 'abuja', 'benin']
# chosen_letter=random.choice(word_list)
# user_guess_letter=input('enter a letter:').lower
# for letter in word_list:
#     if letter ==user_guess_letter:
#         print('right')
#     else:
#         print('wrong')

# random_select = int(input('enter any number to match computer selection: '))
# random_int = random.randint(1, 10)
# if random_select == random_int:
#     print('match')
# else:
#     print('unmatch')
# import math
# def wall_paint_calc(height,width, coverage):
#     area=height*width
#     num_of_can=math.ceil(area/coverage)
#     print(f'you need {num_of_can} to paint the wall')
# wall_paint_calc(height=3, width=9,coverage=5)

    
# def prime_number_checker(number):
#     is_prime=True
#     for i in range(2,number):
#         if number % i==0:
#             is_prime=False
#     if is_prime:
#         print('is prime number')
#     else:
#         print('Not a prime number')
# n=int(input('Check this number:\n'))
# prime_number_checker(number=n)

student_scores= {
    'Harry':81, 
    'Ron':78, 
    'Hermione':99, 
    'Draco':74, 
    'Neville':62,
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student] ='Outstanding'
    elif score>80:
        student_grades[student] = 'Exceeded Expections'
    elif score>70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
    
print(student_grades)
