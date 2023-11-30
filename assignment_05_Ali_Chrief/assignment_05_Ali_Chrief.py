import graphviz
class Person:
    def __init__(self, name, family_name, birthdate):
        self.children = []
        self._name = name
        self._family_name = family_name
        self._birthdate = birthdate

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_family_name(self):
        return self._family_name

    def set_family_name(self, family_name):
        self._family_name = family_name

    def get_birthdate(self):
        return self._birthdate

    def set_birthdate(self, birthdate):
        self._birthdate = birthdate

class Family : 
    def __init__(self, name, family_name, birthdate):
        self.root = None 
        self.root = Person(name, family_name, birthdate)

    def add_child(self, parent, name, family_name, birthdate):
        new_child = Node(name, family_name, birthdate)
        parent.children.append(new_child)

    def visualize_tree(self):
        dot = graphviz.Digraph(comment='Tree')

        def add_nodes_edges(dot, node):
            dot.node(str(node), label=str(node.data))
            for child in node.children:
                add_nodes_edges(dot, child)
                dot.edge(str(node), str(child))

        add_nodes_edges(dot, self.root)
        dot.render('tree', format='png', cleanup=True)

    def search(self, start_node, name):
        count = 0
        for child in start_node.children:
            result = self.search(child, name)
            if result.name == name :
                count += 1
    def exit(self):
        print('exit')


def menu():
    family = Family("Ali","Chrief","19-3-1997")
    print("""
            1. Add Family Member
            2. Display Sorted Birthdays
            3. Find Relationship
            4. Visualize Family Tree
            5. Count Same First Names
            6. Exit
          
          """)
    choice = input("Enter your choice ")
    if choice == '1':
        name = input('Enter the name :')
        family_name = input('Enter the name :')
        birthdate = input('Enter the name :')
        family.add_child(name, family_name,birthdate)
    if choice == '4':
        family.visualize_tree()
    if choice == '5':
        name = input("Enter the name to search")
        family.search(family.root,name)
    if choice == '6':
        family.exit()

    

while True :
    menu()

