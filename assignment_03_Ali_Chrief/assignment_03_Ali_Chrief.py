student_data = [
    {
        "ID": 1,
        "Name": "Alice",
        "Age": 20,
        "Major": "Computer Science",
        "GPA": 3.7
    },
    {
        "ID": 2,
        "Name": "Bob",
        "Age": 21,
        "Major": "Engineering",
        "GPA": 3.9
    }
]

def get_student_by_id(listOfStudent,id):
  for i in range (len(student_data)):
    if id == student_data[i]['ID']:
      return student_data[i]


def student_info(student_data):
  for i in range (len(student_data)):
    print(student_data[i])

def get_students_by_major(student_data,major):
  for i in range (len(student_data)):
    if major == student_data[i]['Major']:
      print(student_data[i])

def main():
  print("1. Get Student by ID")
  print("2. Get All Students")
  print("3. Get Students by Major")
  print("4. Add Student")
  print("5. Find Common Majors")
  print("6. Delete Student")
  print("7. Calculate Average GPA")
  print("8. Get Top Performers")
  print("9. Exit")
  print("- - - - - - - - - - - - - - -")

  choice = int(input("Enter your choice from 1 to 9:"))
  if choice == 1:
    id = int(input("Please Enter the target student id:"))
    print(get_student_by_id(student_data,id))
  if choice == 2:
    student_info(student_data)
  if choice == 3:
    major = input("Enter the major:")
    get_students_by_major(student_data,major)

while True :
  main()