tabs = []
# add tab to a list
def open_tab(web_title,web_url):
  tabs.append({"title":web_title,"url":web_url})
  print(tabs)

def close_tab(index):
  if (index):
    try:
      tabs.pop(index)
      print(tabs)
    except Exception as error:
      print("Error :",error)
  



def main():
  print("""
           1. Open Tab
           2. Close Tab
           3. Switch Tab
           4. Display All Tabs
           5. Open Nested Tab
           6. Clear All Tabs
           7. Save Tabs
           8. Import Tabs
           9. Exit
        """)
  user_choice = int(input("please enter your choice :"))
  if user_choice == 1:
    title = input("What is the title of your website :")
    url = input("Enter the url of your website :")
    open_tab(title,url)
  if user_choice == 2:
    user_index = input("Enter the index of tab you want to remove :")
    if(user_index):
     user_index = int(user_index)
     close_tab(user_index)
    else:
      close_tab(None)


while True:
  main()