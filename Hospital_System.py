import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.sgu.edu/blog/medical/ultimate-list-of-medical-specialties/').text
soup = BeautifulSoup(site,'html.parser')

class Person:
    def __init__(self,spec,name,stat) -> None:
        self.spec = spec
        self.name = name
        self.stat = stat
    specializations = [i.string[3:].strip() for i in soup.find_all('h3')][:-2]
    status = ['Normal','Urgent','Super Urgent']
    def __str__(self) -> str:
        return "Patient " + self.name + " Specialization " + self.specializations[self.spec - 1] + " Status " + self.status[self.stat]
    def __repr__(self) -> str:
        return 'Person('+self.spec+','+self.name+','+self.stat+')'
    def __lt__(self,person):
        return self.stat < person.stat
class Functionality:
    def __init__(self) -> None:
        self.queues = [[] for _ in range(20)]
    def add(self,person):
        if len(self.queues[person.spec - 1]) < 10:
            for i , v in enumerate(self.queues[person.spec - 1]):
                if v < person:
                    self.queues[person.spec - 1].insert(i,person)
                    break
            else:
                self.queues[person.spec - 1].append(person)
            print("Patient added successfully!")
        else:
            print("The Queue is full!")
    def print_spec(self):
        for i , v in enumerate(self.queues):
            print("Specialization " + Person.specializations[i] + ": There are " + str(len(v)) + " Patients.")
            for p in v:
                print("\tPatient: " + p.name + " is " + Person.status[p.stat])
    def get_next(self,spec):
        if len(self.queues[spec - 1]):
            print("Next patient is " + self.queues[spec - 1][0].name)
            self.queues[spec - 1].pop(0)
        else:
            print("There is no patients.")
    def remove_patient(self,spec,name):
        if len(self.queues[spec - 1]):
            for p in self.queues[spec - 1]:
                if p.name == name:
                    print("Patient " + name + " leaved without seeing a doctor!")
                    self.queues[spec - 1].remove(p)
                    break
            else:
                print("There is no such patient.")
        else:
            print("There is no patients in this specialization.")
    def validate_int(self,inp):
        inp = str(inp)
        inp = inp.strip()
        if inp.isdecimal():
            return True
        return False
class Menu:
    def __init__(self) -> None:
        pass
    def show_menu(self):
        func = Functionality()
        while 1:
            print("\nHello in our hospital system!")
            print("Enter 1 to add a new patient.")
            print("Enter 2 to get the next patient.")
            print("Enter 3 to remove a patient without seeing a doctor.")
            print("Enter 4 to show all patients in all specializations.")
            print("Enter 5 to exit the program.\n")
            main_choice = input("Enter your choice: ")
            if main_choice == '1':
                while 1:
                    name = input("Enter patient name: ").strip()
                    spec = input("Enter patient specialization: ").strip()
                    status = input("Enter patient status: ").strip()
                    if func.validate_int(spec) and func.validate_int(status):
                        spec = int(spec)
                        status = int(status)
                        break
                    else:
                        print("Please make sure that specialization and status must be integer!")
                valid = True
                if spec < 1 or spec > 20:
                    print("Invalid specialization!\tPlease enter valid specialization")
                    valid = False
                if status < 0 or status > 2:
                    print("Invalid status!\tPlease enter valid status.")
                    valid = False
                if not valid:
                    continue
                person = Person(spec,name,status)
                func.add(person)
            elif main_choice == '2':
                while 1:
                    spec = input("Enter specialization: ")
                    if func.validate_int(spec):
                        spec = int(spec)
                        break
                    print("Please make sure that specialization must be integer!")
                if spec < 1 or spec > 20:
                    print("Invalid specialization!\tPlease enter valid specialization")
                    continue
                func.get_next(spec)
            elif main_choice == '3':
                while 1:
                    name = input("Enter patiet name: ")
                    spec = input("Enter specialization: ")
                    if func.validate_int(spec):
                        spec = int(spec)
                        break
                    print("Please make sure that specialization must be integer")
                if spec < 1 or spec > 20:
                    print("Invalid specialization!\tPlease enter valid specialization")
                    continue
                func.remove_patient(spec,name)
            elif main_choice == '4':
                print("\n\tPatients list\n")
                func.print_spec()
            elif main_choice == '5':
                break
            else:
                print("Invalid choice!")
if __name__ == '__main__':
    menu = Menu()
    menu.show_menu()