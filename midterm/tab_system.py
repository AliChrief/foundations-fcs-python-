tabs = []
def open_tab(web_title,web_url):
  tabs.append({"title":web_title,"url":web_url})
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
  user_choice = int(input("please enter your choice :"))
  if user_choice == 1:
    title = input("What is the title of your website :")
    url = input("Enter the url of your website :")
    open_tab(title,url)

while True:
  main()