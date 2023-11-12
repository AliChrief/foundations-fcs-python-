import requests
import os.path
import json

# list of tabs
tabs = []
terminate_system = False

# Vaildate the URL
#  O(1)
def validate_url(url):
  if url.startswith("http://") or url.startswith("https://"):
    return True
  else:
    return False
  
# Add Tab to the list
# O(1)
def open_tab(web_title,web_url):
  global tabs
  # Validate the Protocol of any URL
  if (validate_url(web_url)):
   tabs.append({"title":web_title,"url":web_url})
   print(tabs)
  else:
    print("The URL doesn't met the protocol")

# CLose tab
# O(1)
def close_tab(index):
  global tabs
  # Check index range and pop if user enter index
  if index is not None and index >= 0:
    try:
      tabs.pop(index)
      print(tabs)
    except Exception as error:
      print("Error :",error)
  # Pop if user did't insert index
  else:
    tabs.pop()
    print(tabs)

# Switch tab
# O(1)
def switch(switchIndex):
  global tabs 
  # Tab list is empty
  if (len(tabs) == 0):
    print('Empty tab list')
    return
  # User enter index => validate this index
  if switchIndex is not None and switchIndex >= 0:
    try:
      # Using the URL from the dictionary at switchIndex to make a GET request using the requests library.
      url = requests.get(tabs[switchIndex]["url"])
      # Extract the html text
      html_text = url.text
      print(html_text)
    except Exception as error:
      print("Error :",error)
  # User didn't pass any index
  else:
      # last tab
      url = requests.get(tabs[len(tabs)-1]["url"])
      # Extract the html text
      html_text = url.text
      print(html_text)

# Display all tabs
# O(n^2) 
def display_all_tab():
  global tabs
  if(len(tabs) == 0):
    print("Empty tab")
    return
  for i in range (len(tabs)):
   #  Print tab's title that aren't nested
   if(tabs[i].get("index") is None):
    print("Tab number :",i," ",tabs[i]["title"])
    # Print nested title tabs under parent tab
    for x in range (len(tabs)):
      if(tabs[x].get("index") is not None ):
        if i == tabs[x]['index']:
          print(" " * 4 ,"Nested tab related to parent tab whose index number:",i," ", tabs[x]["title"])

# Add nested tab to the list
def open_nested_tap(web_title,web_url,parentIndex):
    global tabs
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

# Delete all tabs
def clear_all_tab():
  global tabs
  # Check if tab list already empty
  if len(tabs) == 0:
    print('Already empty')
  # Clear all opened tabs.
  else:
    tabs = []
    print(tabs)

def save_tabs(path):
  global tabs 
  # Check if the list is empty
  if(len(tabs) == 0):
    print("Empty tab lsit")
    return
  # Convert every element into string in list that have single quotes to double since json doesn't accept single quote
  tabs_str = str(tabs).replace("'", '"')
  with open(path, 'w') as file:
      # Write the contents to the file
      file.write(tabs_str)
      # Close the file
      file.close()

# Import tabs
def import_tab(path):
  global tabs
  try :
    with open(path, 'r') as file:
      tab = file.read()
    # Convert from string type into dictionary type
    tab = json.loads(tab)
    # Append the contents to tab list
    for i in range (len(tab)):
      tabs.append(tab[i])
  except Exception as error: # Handle the existence of file
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
    switch_index = input("Enter the tab's index you want to switch :")
    if switch_index.isnumeric() :
      switch_index = int(switch_index)
      switch(switch_index)
    elif (not switch_index):
      switch(None)
    else:
      print('Invalid index')

  elif user_choice == '4':
    display_all_tab()

  elif user_choice == '5':
    parent_index = input("Enter the parent index :")
    # Validate user parent index
    if parent_index.isnumeric() and 0 <= int(parent_index) <= len(tabs)-1 and len(tabs) >= 0 :
      parent_index = int(parent_index)
      title = input("What is the title of your website :")
      url = input("Enter the url of your website :")
      open_nested_tap(title,url,parent_index)
    else:
      print('Invalid index/tabs is empty')

  elif user_choice == '6':
    clear_all_tab()

  elif user_choice == '7':
    path = os.path.abspath("save_tab.json")
    save_tabs(path)

  elif user_choice == '8':
    path = os.path.abspath("save_tab.json")
    import_tab(path)

  elif user_choice == '9':
    global terminate_system
    terminate_system = True
  else:
    print("Please select a valid choice.")



while terminate_system == False:
   main()

