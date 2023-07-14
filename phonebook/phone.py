import time
class use :
    
    def __init__(self,names,phone_numbers,num,email_id):
        self.phone_numbers=phone_numbers
        self.names=names
        self.num=num
        self.email_id=email_id

###############################################################################################################################

    def add(self,names,phone_numbers,num,email_id): 
        num=int(input("Enter how many numbers you want to add in the book :\t"))
        if num<=0:
            print("Please enter valid number\t")
            
        else :

           for i in range(num):
            name = input("Enter Name:\t")
            names.append(name)
            names.sort()
            index=names.index(name)
            email=str(input("Enter Email id:\t"))
            email_id.insert(index,email)
            phone_number = input("Enter Phone Number:\t") 
           
            phone_numbers.insert(index,phone_number)
            time.sleep(2)
            print("Contact saved sucessfully !\n\n")   

        
        

#################################################################################################################################
                        
    def search(self,names,phone_numbers,num,email_id):


        search_term = input("\nEnter search term:\t")
        print("\n")
        res = [i for i in names if search_term in i]
        if len(res) == 0:
            print("Contact not found, please try again\n")
        else :
            print("Contact found !\n")

        for i in range(len(res)):
            index = names.index(res[i])
            phone_number = phone_numbers[index]
            email=email_id[index]
            print("Name: {}, Phone Number: {}, Email-ID {}\n\n".format(res[i], phone_number,email))    

##################################################################################################################           

    def modify(self,names,phone_numbers,num,email_id):
            search_t= input("\nEnter the name for modifying: ")
            ind=0
    
            if search_t in names: 
                ind = names.index(search_t)
                loc=ind
                print("Enter the following options")
                print("1.Update name\n2.Update Number\n3.Update email\n4.All the options")
                c=int(input("Enter your choice :"))
                if c==1 :
                    str1=str(input("Enter Name :"))
                    names[loc]=str1
                    time.sleep(1)
                    print("Modified sucessfully !")
                elif c==2 :
                    str2=int(input("Enter number :"))
                    phone_numbers[loc]=str2
                    time.sleep(1)
                    print("Modified sucessfully !")

                    
                elif c==3:
                    str3=str(input("Enter Email ID:"))
                    email_id[loc]=str3
                    time.sleep(1)
                    print("Modified sucessfully !")

                elif c==4 :
                    str1=str(input("Enter Name :"))
                    names[loc]=str1
                    str2=int(input("Enter number :"))
                    phone_numbers[loc]=str2
                    str3=str(input("Enter Email ID:"))
                    email_id[loc]=str3
                    time.sleep(1)
                    print("Modified sucessfully !")

                else :
                    print("Invalid option")


            else :  
                print("Contact not found, Please try again")    

#####################################################################################################################################################
    
    def delete(self,names,phone_numbers,num,email_id):
        delete_term = input("\nEnter delete term: ")
        print("\n")
        if delete_term in names:
            index = names.index(delete_term)
            names.remove(delete_term)
            phone_number = phone_numbers[index]
            phone_numbers.remove(phone_number)
            email=email_id[index]
            email_id.remove(email)
            time.sleep(1)
            print("Contact Deleted sucessfully !!\n")
        else:
            print("Name Not Found, Try again\n") 

#####################################################################################################################################################
        
    def display(self,names,phone_numbers,num,email_id):
        
        f=open('phone.txt','a+')
        
    

        if len(names)==0:
            print("No Contacts Found\n")
        else :
            time.sleep(1)
            print("\nHere is the result\n")
            print("\nName\t\t\tPhone Number\t\t\tEmail ID\n")
        for i in range(len(names)):
            f.write(str(names[i])+" "+str(phone_numbers[i])+" "+str(email_id[i])+"\n")
            print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i],email_id[i]))
            print("\n")

            

##################################################################################################################################################################   

print("\n")
time.sleep(1)
print("\t************************* Welcome to Contact Book Management System ***********************\n\n")
names = []
phone_numbers = []
email_id=[]
num=0
u=use(names,phone_numbers,num,email_id)
a=1
while a:
    time.sleep(1)
    print("\t\tSelect the following operations")
    print("\t\t1.Add a number\n\t\t2.Search a number\n\t\t3.Modify a number\n\t\t4.Delete a number\n\t\t5.Display contacts\n\t\t6.Exit\n")
    option=int(input("Enter your choice :\t"))
    
    
    if(option==1):
        u.add(names,phone_numbers,num,email_id)
    elif(option==2):
        u.search(names,phone_numbers,num,email_id)
    elif(option==3):
        u.modify(names,phone_numbers,num,email_id)
    elif (option==4):
        u.delete(names,phone_numbers,num,email_id)
    elif(option==5):
        u.display(names,phone_numbers,num,email_id)
    elif(option==6):
        break             
    else :
        print("Invalid Option, Please choose the correct option again")
    a=int(input("Do want to continue ?, If yes press 1 or else press 0 :")) 
    print("\n") 

print("\n\n*********************** Thank You *****************************\n\n")          


        