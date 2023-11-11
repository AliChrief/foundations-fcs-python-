# list of tabs
tabs = []
terminate_system = False
# Vaildate the URL 
def validate_url(url):
  if url.startswith("http://") or url.startswith("https://"):
    return True
  else:
    return False
# Add Tab to the list
def open_tab(web_title,web_url):
  # Validate the Protocol of any URL
  if (validate_url(web_url)):
   tabs.append({"title":web_title,"url":web_url})
   print(tabs)
  else:
    print("The URL doesn't met the protocol")

# CLose tab
def close_tab(index):
  # Check index range and pop if user enter index
  if (index is not None and index >= 0):
    try:
      tabs.pop(index)
      print(tabs)
    except Exception as error:
      print("Error :",error)
  # Pop is user did't insert index
  else:
    tabs.pop()
    print(tabs)

# Add nested tab to the list
def open_nested_tap(web_title,web_url,parentIndex):
    if(tabs[parentIndex].get("index") is None): #Prevent the user to made nested tab inside another nested tab (1 level nesting allowed as charbel said)
      # Check if user pass the same parentIndex previously (Deny repetitive nested tabs for same parentIndex)
      for i in range (len(tabs)):
        if "index" in tabs[i]:
          if tabs[i]["index"] == parentIndex:
            print('This index refers to a 1st level nested tab not to a parent')
            print(tabs)
            return None
      # If not, add nested list with specified index to the list and validate the URL
      if (validate_url(web_url)):
        tabs.append({"index":parentIndex,"title":web_title,"url":web_url})
        print(tabs)
      else:
        print("The URL doesn't met the protocol")
    else:
      print("This index refers to a nested tab, you can't made nested tab inside another nested tab")
# Display all tabs 
def display_all_tab():
  if(len(tabs) == 0):
    print("Empty tab")
    return
  for i in range (len(tabs)):
   #  Print tab's title that aren't nested
   if(tabs[i].get("index") is None):
    print(tabs[i]["title"])
    # Print nested title tabs under parent tab
    for x in range (len(tabs)):
      if(tabs[x].get("index") is not None ):
        if i == tabs[x]['index']:
          print(" " * 4 , tabs[x]["title"])
    
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
    # Check if index is number and > 0
    if(user_index.isnumeric()):
      user_index = int(user_index)
      close_tab(user_index)
    # Check if user didn't insert index
    elif (not user_index):
      close_tab(None)
    # User enter thing other than number (string or token)
    else:
      print("Please select a valid index ")
  elif user_choice == '3':
    switch()
  elif user_choice == '4':
    display_all_tab()
  elif user_choice == '5':
    parent_index = input("Enter the parent index")
    # Validate user parent index
    if parent_index.isnumeric() and 0 <= int(parent_index) <= len(tabs)-1 and len(tabs) >= 0 :
      parent_index = int(parent_index)
      title = input("What is the title of your website :")
      url = input("Enter the url of your website :")
      open_nested_tap(title,url,parent_index)
    else:
      print('Invalid index/tabs is empty')

  elif user_choice == '9':
    global terminate_system
    terminate_system = True
  else:
    print("Please select a valid choice.")



while terminate_system == False:
   main()

