# def count_digits(n):
#   if n == 0:
#     return 0
#   else:
#     return 1 + count_digits(n // 10)


# def find_max(list):
#   if len(list) == 1:
#     return list[0]
#   else:
#     return max(list[0], find_max(list[1:]))

# def exit():
#   print("Exit")


# def main():
#   print("1. Count Digits")
#   print("2. Find Max")
#   print("3. Count Tags")
#   print("3. Count Normalized Columns")
#   print("4. Exit")

#   choice = int(input("Enter your choice: "))

#   if choice == 1:
#     n = int(input("Enter a number: "))
#     print(count_digits(n))
#   if choice == 2:
#     list = [int(x) for x in input("Enter a list of numbers: ").split()]
#     print(find_max(list))
#   if choice == 3:
#     print("Not Implemented")
#   if choice == 4:
#     exit()


# while True : 
#   main()


