# EX1

# def factorail() :
#   num = input("Enter a number: ")
#   while (not num.isnumeric()):
#     num = input("invalid input!, please enter a positive numeric grade here:")
#   num = int(num)
#   if num == 0:
#     print("1")
#   else:
#     res = 1
#     s = ""
#     for i in range (1,num+1):
#      res = res * i
#      s += str(i) + "*"
#     print(res,'(',s[0:len(s)-1],')')
# while(True):
#   factorail()

# EX 2

#   def check_divisors(num):
#   num = abs(num)
#   list_divisors = []
#   for i in range(1, num + 1):
#     if num % i == 0:
#       list_divisors.append(i)
#   print(list_divisors)
# check_divisors(-16)

# EX 3

# def reverse(s):
#   string_to_reversed = " "
#   for x in range(len(s)-1,-1,-1):
#     string_to_reversed += s[x]
#   print(string_to_reversed)
# reverse("Hello World")
# reverse("oneword")

# EX 4 

# def check_even(): 
#   numbers = input("Enter a list of numbers ")
#   list_of_even = []
#   numbers = numbers.split()
#   for num in numbers : 
#     if int(num) % 2 == 0:
#       list_of_even.append(num)
#   return list_of_even
# evenList = check_even()
# print(evenList)

# EX 5

# def check_password():
#     password = input('Enter your password')
#     lower_case_flag = False
#     upper_case_flag = False
#     length_flag = False
#     token_flag = False
#     for elem in password:
#         if elem.isupper():
#             upper_case_flag = True
#             break
#     for elem in password:
#         if elem.islower():
#             lower_case_flag = True
#             break
#     if len(password) >= 8:
#         length_Flag = True
#     for elem in password:
#         if elem == '#' or elem == '?' or elem == '!' or elem == '$':
#             token_flag = True
#     if(upper_case_flag == lower_case_flag == length_Flag == token_flag == True):
#         print("Strong password")
#     else:
#         print('Weak password')

# check_password()

# EX 6 

# def ipv4():
#   ip = input("Enter an IPv4 address: ")
#   ip = ip.split(".")
#   if len(ip) != 4:
#     print("Invalid IPv4 address.")
#     return False
#   for i in ip:
#     if not i.isdigit():
#       print("Invalid IPv4 address.")
#       return False
#     i = int(i)
#     if i < 0 or i > 255:
#         return False
#   return True
# print(ipv4())


















def check_password():
    password = input('Enter your password')
    lower_case_flag = False
    upper_case_flag = False
    length_flag = False
    token_flag = False
    for elem in password:
        if elem.isupper():
            upper_case_flag = True
            break
    for elem in password:
        if elem.islower():
            lower_case_flag = True
            break
    if len(password) >= 8:
        length_Flag = True
    for elem in password:
        if elem == '#' or elem == '?' or elem == '!' or elem == '$':
            token_flag = True
    if(upper_case_flag == lower_case_flag == length_Flag == token_flag == True):
        print("Strong password")
    else:
        print('Weak password')

check_password()