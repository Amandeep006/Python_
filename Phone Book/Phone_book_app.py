
class PhoneBook:
    phone_directory=[] # Class Variable 

    def __init__(self,name, phone_number):
        self.name=name
        self.phone=phone_number

        PhoneBook.phone_directory.append(self)


    def show_contact(self): # Instances methods
        return f"Name: {self.name} \nContact Number : {self.phone}"
    

    @classmethod  # Class Methods 
    def show_all_contact(cls):
        if len(cls.phone_directory)==0:
            print("No contact found in the directory!")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())
    

    @classmethod 
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name==search_name:
                return f"{contact.name.upper()}\n{contact.phone}"
            
        return f"No contact found for {search_name}"
    

    @staticmethod
    def validate_phone_number(number):
        if len(number)<=8 and number.isdigit() :
            return True
        
        else:
            return False




"""Just Print the values """
# c1=PhoneBook("John",365478913) # c1 is the objects 
# c2=PhoneBook("Alex",79164892663) 
# c3=PhoneBook("Peter",432326494663)
# print(PhoneBook.phone_directory)
# PhoneBook.show_all_contact()

"""Searching the Contact Number """
# print(PhoneBook.search_contact("Peter"))

n_contacts=int(input("How many contacts do you want to add ?"))

for i in range(n_contacts):
    name=input("Enter your name here :")
    phone_number=input("Enter your number:")

    if PhoneBook.validate_phone_number(phone_number):
        PhoneBook(name,phone_number)

PhoneBook.show_all_contact()


# c1.show_all_contact()