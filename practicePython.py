# # # # # # firstName = "Sam"
# # # # # # #if we want to change the S for a P, We cant do that. we cant do the following
# # # # # # #firstName[0]= "P" This will not work so what we can do is the following
# # # # # # lastLetters = firstName[1:]
# # # # # # # #we need to concatinate with Plus Sign by doing the following
# # # # # # # print('P' + lastLetters)

# # # # # # # letter='hi'
# # # # # # # print(letter * 10)
# # # # # # # name = "Orlando"
# # # # # # # age = 32.657
# # # # # # # print(f'{name} is {age:1.2f} years old')

# # # # # # my_list = [1,2,3]
# # # # # # my_list = ['String',100,3,2]
# # # # # # my_list = ['one','two','three']
# # # # # # another_list = ['four','five']
# # # # # # new_list = my_list + another_list
# # # # # # new_list[0] = 'ONE IN ALL CAPS'
# # # # # # new_list.pop()
# # # # # # new_list.pop(0)
# # # # # # a_new_list = ['a','e','x', 'b','c']
# # # # # # num_list = [4,1,2,8,3]
# # # # # # a_new_list.sort()
# # # # # # num_list.sort()
# # # # # # num_list.reverse()
# # # # # # print(a_new_list, num_list)
# # # # # # myset = set()

# # # # # # myset.add(1)
# # # # # # myset.add(2)
# # # # # # mylist = [1,1,1,1,1,1,2,2,2,3,3,3]
# # # # # # print("This is a set " , set(mylist))
# # # # # # print(set([1,1,2,3]))
# # # # # # hungry = False
# # # # # # if hungry:
# # # # # #     print('Feed Me!')
# # # # # # else:
# # # # # #     print('Im not hungry')


# # # # # # loc ='Bank'

# # # # # # if loc == 'Auto Shop':
# # # # # #     print("Cars are cool!")
# # # # # # elif loc == 'Bank':
# # # # # #     print('Money is Cool!')
# # # # # # elif loc == 'Store':
# # # # # #     print('Welcome to the store!')
# # # # # # else:
# # # # # #     print('I do not know much.')
# # # # # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # # # # for whateveryouwant in mylist:
# # # # # #     print('Hello!')
# # # # # mylist = [1,2,3,4,5,6,7,8,9,10]
# # # # # for num in mylist:
# # # # #     if num % 2 ==0:
# # # # #         print(num)
# # # # #     else:
# # # # #         print(f'Odd Number: {num}')

# # # # # d= {'k1':1,'k2':2,'k3':3}
# # # # # for key,value in d.items():
# # # # #     print(value)
# # # # # x= [1,2,3]

# # # # # for item in x:
# # # # #     if item ==2:
# # # # #         pass
# # # # #     else:
# # # # #         print(item)

# # # # # mystring = 'Sammy'
# # # # # print(list(range(0,11,2)))
# # # # index_count = 0
# # # # for letter in 'abcde':
# # # #     print('At index {} the letter is {}'.format(index_count,letter))
# # # #     index_count += 1

# # # # index_count = 0
# # # # word = 'abcde'
# # # # for letter in word:
# # # #     print(word[index_count])
# # # #     index_count +=1

# # # # for item in enumerate(word):
# # # #     print(item)
# # # # for keys,values in enumerate(word):
# # # #     print(keys)
# # # #     print(values)
# # # #     print('\n')

# # # # mylist1 = [1,2,3]
# # # # mylist2 = ['a','b','c']
# # # # mylist3 = [100,200,300]

# # # # for item in zip(mylist1,mylist2):
# # # #     print(item)


# # # # mylist = [10,20,30,40,100,69]
# # # # print(min(mylist))
# # # # print(max(mylist))
# # # # this will print the minimum of a list and max of a list

# # # # from random import shuffle
# # # # myNewList = [1,2,3,4,5,6,7,8,9,20]
# # # # shuffle(myNewList)
# # # # print(myNewList)

# # # # from random import randint
# # # # randint(0,100)

# # # # input('Enter a number: ')

# # # # so, how is this useful?
# # # # Imagine we ask user his name. so we save the users name and we can save it and reuse it in a variable
# # # # Example below:
# # # # result = input('What is your Name? ')
# # # # print(f"Hello {result}, How are you doing today? ")

# # # # mystring = 'hello'

# # # # mylist =[]
# # # # for letter in mystring:
# # # #     mylist.append(letter)
# # # # print(mylist)

# # # # fahrenheit = [((9/5)*temp +32) for temp in celcius]
# # # # celcius = [0, 10, 20, 34.5]
# # # # fahrenheit = []
# # # # for temp in celcius:
# # # #     fahrenheit.append(((9/5)*temp + 32))
# # # # print(fahrenheit)


# # # # mylist= []
# # # # for x in [2,4,6]:
# # # #     for y in [100,200,300]:
# # # #         mylist.append(x*y)
# # # # print(mylist)

# # # # st = 'Print only the words that start with s in this sentence'
# # # # for word in st.split():
# # # #     if word[0] == 's':
# # # #         print(word)


# # # # for nums in range(0,11,2):
# # # #     print(nums)


# # # # st = 'Print every word in this sentence that has an even number of letters'
# # # # for x in st.split():
# # # #     if len(x) % 2 ==0:
# # # #         print(x)

# # # # for letters in st.split():
# # # #     counter

# # # # for x in range(1,101):
# # # #     if x % 3==1:
# # # #         print('Fizz')
# # # #     elif x % 5 == 1:
# # # #         print('Buzz')
# # # #     elif x % 3==1 and x%5==1:
# # # #         print('FizzBuzz')
# # # #     else:
# # # #         print(x)
# # # # for num in range(1,101):
# # # #     if num % 3 == 0 and num % 5 == 0:
# # # #         print("FizzBuzz")
# # # #     elif num % 3 == 0:
# # # #         print("Fizz")
# # # #     elif num % 5 == 0:
# # # #         print("Buzz")
# # # #     else:
# # # #         print(num)

# # # # mylist = [1, 2, 3]
# # # # mylist.pop()
# # # # help(mylist.insert)
# # # def myfunc(string):
# # #     new_string = []
# # #     for letter in string:
# # #         if letter % 2 ==0:
           
# # #             new_string.append(letter.upper())
# # #         else:
# # #             new_string.append(letter)
# # #     return new_string
    
# # # print(myfunc('Anthropomorphism'))

# # def square(num):
# #     return num **2

# # my_nums = [1,2,3,4,5]

# # for item in map(square,my_nums):
# #     print(item)

# # print(list(map(square,my_nums)))

# # def splicer(myString):
# #     if len(myString)%2 == 0:
# #         return 'EVEN'
# #     else:
# #         return myString[0]
    
    
# # print(list(map(splicer,names)))


# # def check_even(num):
# #     return num %2==0


# # for n in filter(check_even,mynums):
# #     print(n)

# # print(list(filter(check_even,mynums)))
# # mynums = [1,2,3,4,5,6]

# # def square(num):
# #     result = num ** 2
# #     return result

# # print(square(3))
# # lambda num: num ** 2
# # ## or we can do the following:
# # print(list(map(lambda num:num**2, mynums)))

# # print(list(filter(lambda num: num %2 ==0, mynums)))

# # names = ['Andy','Eve','Sally']
# # print(list(map(lambda name: name[::-1],names)))

# # name = 'THIS IS A GLOBAL STRING'
# # def greet():
# #     name ='Sammy'
# #     def hello():
# #         print('Hello' + name)
# #     hello()
# # print(greet)
# # def ran_check(num,low,high):
# #     for numberLow, numberHigh in(low,high):
# #         if num <numberLow and num >numberHigh:
# #             return (f'{num} is in range of {low} and {high}')
# #         else:
# #             return False

    

# # print(ran_check(5,2,7))

# def up_low(s):
#     upperCount=0
#     lowerCount=0
#     for letter in s:
#         if letter.isupper():
#            upperCount +=1
#         if letter.islower():
#             lowerCount +=1
#     return (f'No of Upper ase Characters: {upperCount} \n No of Lower case Characters: {lowerCount}')
# print(up_low( 'Hello Mr. Rogers, how are you this fine Tuesday?'))
# def user_choice():
# 	choice = 'Wrong'
# 	acceptable_range = range(0,10)
# 	within_range = False
# 	#Two conditions to check
# 	while choice.isdigit()== False or within_range==False:
# 		choice = input("please enter a number (0-10): ") 
# 		#DigitCheck
# 		if choice.isdigit() == False:
# 			print('Sorry that is  not a digit!')
# 		#Range Check
# 		if choice.isdigit()==True:
# 			if int(choice) in acceptable_range:
# 				within_range = True
# 			else:
# 				print("Sorry, you are out of acceptable range (0-0)")
# 				within_range = False
		
			
# 	return int(choice)
# user_choice()