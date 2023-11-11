tabs = []
# add tab to a list
def validate_url(url):
  if url.startswith("http://") or url.startswith("https://"):
    return True
  else:
    return False

def open_tab(web_title,web_url):
  # Validate the Protocol of any URL
  # if
  tabs.append({"title":web_title,"url":web_url})
  print(tabs)
  # else:
  #   print("The URL doesn't met the protocol")


def close_tab(index):
  if (index is not None and index >= 0):
    try:
      tabs.pop(index)
      print(tabs)
    except Exception as error:
      print("Error :",error)
  else:
    tabs.pop()
    print(tabs)

# check if index not include in the list 
# check if the index is not for the child
def open_nested_tap(web_title,web_url,parentIndex):
    for i in range (len(tabs)):
      if "index" in tabs[i]:
        if tabs[i]["index"] == parentIndex:
          print('This index refers to a 1st level nested tab not to a parent')
          return 
      tabs.append({"index":parentIndex,"title":web_title,"url":web_url})
      print(tabs)



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
  
  user_choice = input("please enter your choice :")
  if user_choice == '1':
    title = input("What is the title of your website :")
    url = input("Enter the url of your website :")
    open_tab(title,url)
  elif user_choice == '2':
    user_index = input("Enter the index of tab you want to remove :")
    # check if index is a number and not negative
    if(user_index.isnumeric()):
      user_index = int(user_index)
      close_tab(user_index)
    #  check if user didn't insert index
    elif (not user_index):
      close_tab(None)
    # user doesn't enter number(string or token)
    else:
      print("Please select a valid index ")
  elif user_choice == '5':
    parent_index = input("Enter the parent index")
    if parent_index.isnumeric() and 0 <= int(parent_index) <= len(tabs)-1 and len(tabs) >= 0:
      parent_index = int(parent_index)
      title = input("What is the title of your website :")
      url = input("Enter the url of your website :")
      open_nested_tap(title,url,parent_index)
    else:
      print('Invalid index/tabs is empty')

    
  else:
    print("Please select a valid choice.")



while True:
  main()

