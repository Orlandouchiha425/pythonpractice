# # def say_hello(name ='Ace'):
# #     input('what is your name?')
# #     return(f'Hello {name}')
# # say_hello()

# # def add_num(num1,num2):
# #     return num1 + num2
# # result = add_num(10,20)

# # def print_result(a,b):
# #     print(a+b)

# # def return_result(a,b):
# #     return a+b

# # print_result(10,20)


# # def sum_numbers(num1, num2):
# #     return num1 + num2
# # print(sum_numbers('10','20'))
# # def even_check(numbers):
# #     result = numbers % 2 == 0
# #     return result


# # print(even_check(20))

# #what if we want it to return false? we cant put the (false instead of the pass)
# #so what we can do is put the indentation after we broke of the loop to return false. 
# #example: 
# # def check_even_list(num_list):
# #     for number in num_list:
# #         if number % 2 == 0:
# #             return True
# #         else:
# #             pass
# # print(check_even_list([1,3,5,4,2,11,1]))


# # def check_even_list2(num_list):
# #     for number in num_list:
# #         if number % 2 == 0:
# #             return True
# #         else:
# #             pass
# #     return False

# # print(check_even_list2([1,3,5,4,2,11,1]))

# # def return_even_numbers(num_list):
# #     even_numbers =[]
# #     for number in num_list:
# #         if number % 2== 0:
# #             even_numbers.append(number)
# #         else:
# #             pass
# #     return even_numbers
# # print(return_even_numbers([1,2,3,4,5]))

# stock_price = [('APPL', 200),('GOOG',400),('MSFT',100)]
# for item in stock_price:
#     print(item)



# stock_prices = [('APPL', 200),('GOOG',400),('MSFT',100)]
# for sticker,price in stock_prices:
#     print(sticker)

# #in this example: we want to check wich user in the tupple has worked the most hours.

# work_hours = [("Abby",100),("Billy",4000),('Cassie',800)]

# def employee_check(work_hours):
#     current_max=0
#     employee_of_month= ''

#     for employee,hours in work_hours:
#         if hours >current_max:
#             current_max = hours
#             employee_of_month = employee
#         else:
#             pass
#     return (employee_of_month,current_max)
    
# print(employee_check(work_hours))
    
    
# def myfunc(*codingIsHard):
#     #Returns 5% of the sum of a and b
#     return sum(codingIsHard) *0.05
# print(myfunc(40,60,70,80,90,100))


# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')

# myfunc(fruit='apple',veggie= 'lettuce')

def myfunc(*args, **kwargs):
    print(kwargs,args)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30, fruit= 'orange', food='eggs', animal='dog')