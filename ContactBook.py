def Add_Contact(Contact_Book):
    name=input("Enter Name Of Contact:")
    P_No=input("Enter Number:")
    Contact_Book[name]=P_No
    print(f"Contact {name} with {P_No} Added Successfully!")

def Search_Contact():
    pass

def Delete_Contact():
    pass

def View_All_Contacts():
    pass

Contact_Book={
    "Suresh":+123,
    "Siraj":+789,
    "Sooraj":+909,
    "Sumeet":+778
}

# Add_Contact(Contact_Book)
# Contact_Book["Neeraj"]=+899
# print(Contact_Book)
# print("Suresh" in Contact_Book)
# del Contact_Book["Suresh"]
# print(Contact_Book)