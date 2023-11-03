student_data = [
    {
        "ID": 1,
        "Name": "Alice",
        "Age": 20,
        "Major": "Biology",
        "GPA": 3.7
    },
    {
        "ID": 2,
        "Name": "Bob",
        "Age": 21,
        "Major": "Engineering",
        "GPA": 10
    },
    {
        "ID": 3,
        "Name": "Bob",
        "Age": 21,
        "Major": "Engineering",
        "GPA": 3.9
    }
]

student_data_prime = [
    {
        "ID": 8,
        "Name": "Ali",
        "Age": 20,
        "Major": "Biology",
        "GPA": 3.7
    },
    {
        "ID": 2,
        "Name": "Mahdi",
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

def add_students(student_data,name,age,major,gpa):
  last_id = student_data[len(student_data)-1]["ID"]
  student_data.append({"ID":last_id+1,"Name":name,"Age":age,"Major":major,"GPA":gpa})
  print(student_data)

def  common_major(student_data1,student_data2):
  major_set1 = []
  major_set2 = []
  for i in range (len(student_data1)):
    major_set1.append(student_data1[i]["Major"])
  for i in range (len(student_data2)):
    major_set2.append(student_data2[i]["Major"])
  major_set1 = set(major_set1)
  major_set2 = set(major_set2)
  print(major_set1)
  print(major_set2)
  common_majors = major_set1.intersection(major_set2)
  print(common_majors)

def delete_student_by_id(list_of_student,id):
  for i in range (len(list_of_student)):
    if list_of_student[i]["ID"] == id:
      del list_of_student[i]
      break
  print(list_of_student)
def average(list_of_student):
  list_of_GPAs = []
  sum = 0
  count = len(list_of_student)
  for i in range (len(list_of_student)):
    sum += list_of_student[i]["GPA"]
  avg = sum/count
  print(avg)

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
  if choice == 4:
    new_name = input("Enter new name:")
    new_age = input("Enter new age:")
    new_major = input("Enter new major:")
    new_GPA = input("Enter new gpa:")
    add_students(student_data,new_name,new_age,new_major,new_GPA)
  if choice == 5:
    common_major(student_data,student_data_prime)
  if choice == 6:
    id_to_deltete = int(input("Enter the id of the student you want to delete :"))
    delete_student_by_id(student_data,id_to_deltete)
  if choice == 7:
    average(student_data)




# while True :
main()