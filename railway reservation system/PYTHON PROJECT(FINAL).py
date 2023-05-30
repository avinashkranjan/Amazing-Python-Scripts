  import os
import platform
import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="railway")
mycursor=mydb.cursor()
CNo=0
TNo=0


#function for registering a customer

def RegisterCustomer():
    L=[]
    CName=input("Enter the name of the customer:")
    L.append(CName)
    CAge=int(input("Enter the age of the customer:"))
    L.append(CAge)
    CGender=input("Enter the gender:")
    L.append(CGender)
    CPhone=int(input("Enter phone number in digits:"))
    L.append(CPhone)
    CPwd=input("enter you new password:")
    L.append(CPwd)
    value=L
    try:
        sql="insert into customer_details(CName,CAge,CGender,CPhone,CPwd) values(%s,%s,%s,%s,%s)"
        mycursor.execute(sql,value)
        mydb.commit()
        print("Record registered")
    except Exception as e:
        print(e)
    s=CPhone
    rl=(s,)
    try:
        sql="select CNo from customer_details where CPhone=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for y in res:
            print(y[0]," is your customer number please remember it as your login ID")
        return res
    except Exception as e:
        print(e)



#function to display a customer
        
def DisplayCustomer():
    print("Select the search criteria:")
    print("1.customer No")
    print("2.Customr Name")
    print("3.customer phone")
    ch=int(input("Enter choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        s=int(input("Enter customer no:"))
        rl=(s,)
        try:
            sql="select * from customer_details where CNo=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for y in res:
                print(y)
        except Exception as e:
            print(e)
    elif ch==2:
        s=input("enter Cname:")
        rl=(s,)
        try:
            sql="select * from customer_details where CName=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for z in res:
                print(z)
        except Exception as e:
            print(e)
    elif ch==3:
        s=int(input("enter phone number:"))
        rl=(s,)
        try:
            sql="select * from customer_details where CPhone=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)
    else:
        print("wrong choice")



#function to register a train
def RegisterTrain():
    L=[]
    TNo=int(input("Enter the train number(max 5 digits):"))
    L.append(TNo)
    TName=input("Enter the name of the train:")
    L.append(TName)
    TSource=input("enter source:")
    L.append(TSource)
    TDestination=input("enter destination:")
    L.append(TDestination)
    Time_of_departure_from_source=input("enter time source:")
    L.append(Time_of_departure_from_source)
    Time_of_arrival_at_destination=input("enter time dest:")
    L.append(Time_of_arrival_at_destination)
    value=L
    try:
        sql="insert into train values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,value)
        mydb.commit()
        print("Record registered")
    except Exception as e:
        print(e)



#function to display a train

def DisplayTrain():
    print("Select the search criteria:")
    print("1.train Number")
    print("2.train name")
    print("3.train source")
    print("4.train destination")
    print("5.Time of departure from source")
    print("6.Time of arrival at destination")
    print("7.All")
    ch=int(input("Enter choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        TNo=int(input("Enter train no:"))
        rl=(TNo,)
        try:
            sql="select * from train where TNo=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for y in res:
                print(y)
        except Exception as e:
            print(e)
    elif ch==2:
        TName=input("enter train name:")
        rl=(TName,)
        try:
            sql="select * from train where TName=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for z in res:
                print(z)
        except Exception as e:
            print(e)
    elif ch==3:
        TSource=input("enter source of train:")
        rl=(TSource,)
        try:
            sql="select * from train where TSource=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)
    elif ch==4:
        TDestination=input("enter destination of train:")
        rl=(TDestination,)
        try:
            sql="select * from train where TDestination=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)
    elif ch==5:
        Time_of_departure_from_source=input("enter time of departure from source of train:")
        rl=(Time_of_departure_from_source,)
        try:
            sql="select * from train where Time_of_departure_from_source=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)
    elif ch==6:
        Time_of_arrival_at_destination=input("enter time of arrival at destination of train:")
        rl=(Time_of_arrival_at_destination,)
        try:
            sql="select * from train where Time_of_arrival_at_destination=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)
    elif ch==7:
        try:
            sql="select * from train"
            mycursor.execute(sql)
            res=mycursor.fetchall()
            print("The details of trains are as follows:")
            for x in res:
                print(x)
        except Exception as e:
            print(e)




#function for searching a train

def SearchTrain(source,destination):
    k=[]
    k.append(source)
    k.append(destination)
    values=k
    try:
        sql="select * from train where TSource=%s and TDestination=%s"
        mycursor.execute(sql,values)
        res=mycursor.fetchall()
        print("(train no,train name,source,destination,Time of departure from source,Time of arrival at destination)")
        for k in res:
                print(k)
        return res
    except Exception as e:
        print(e)
    


#function for booking a ticket

def bookTicket(cno,tno,src,dest,date):
    a=[]
    a.append(cno)
    a.append(tno)
    a.append(src)
    a.append(dest)
    a.append(date)
    value=a
    try:
        sql="insert into bookings (CNo,TNo,Source,Destination,Date)values(%s,%s,%s,%s,%s)"
        mycursor.execute(sql,value)
        mydb.commit()
    except Exception as e:
        print(e)
    s=cno
    rl=(s,)
    try:
        sql="select PNR from bookings where CNo=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for y in res:
            print(y[0]," is your PNR number please remember it for any further query")
    except Exception as e:
        print(e)



#function for cancelling a ticket        

def RemoveBooking():
    PNR=int(input("Enter the PNR number of the customer whose ticket is to be cancelled:"))
    rl=(PNR,)
    try:
        sql="Delete from bookings where PNR=%s"
        mycursor.execute(sql,rl)
        print("Record deleted")
        mydb.commit()
    except Exception as e:
        print(e)



#function for removing a train

def RemoveTrain():
    TNo=int(input("Enter the train number of the train to be deleted:"))
    rl=(TNo,)
    try:
        sql="Delete from train where TNo=%s"
        mycursor.execute(sql,rl)
        print("Record deleted")
        mydb.commit()
    except Exception as e:
        print(e)



#function for displaying a customer

def DisplayBooking():
    print("Select the search criteria:")
    print("1.customer Number")
    print("2.train number")
    print("3.PNR number")
    ch=int(input("Enter choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        s=CNo
        rl=(s,)
        try:
            sql="select * from bookings where CNo=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for y in res:
                print(y)
        except Exception as e:
            print(e)
    elif ch==2:
        cno=CNo
        s=int(input("enter train number:"))
        rl=(cno,s)
        try:
            sql="select * from bookings where CNo=%s and TNo=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            print("(PNR,customer number,train number,source,destination,date)")
            for z in res:
                print(z)
        except Exception as e:
            print(e)
    elif ch==3:
        s=int(input("enter PNR number:"))
        rl=(s,)
        try:
            sql="select * from bookings where PNR=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)
    else:
        print("wrong choice")



#function for removing a customer

def RemoveCustomer():
    CNo=int(input("Enter the customer number of the customer to be deleted:"))
    rl=(CNo,)
    try:
        sql="Delete from customer_details where CNo=%s"
        mycursor.execute(sql,rl)
        mydb.commit()
        print("Record deleted")
    except Exception as e:
        print(e)



#function for updating a customer

def UpdateCustomer():
    print("Select what to update:")
    print("1.customer no")
    print("2.customer name")
    print("3.customer age")
    print("4.customer gender")
    print("5.customer phone")
    ch=int(input("Enter your choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        CName=int(input("enter the name of the customer whose customer number is changed:"))
        CNo=int(input("Enter the new customer number:"))
        rl=(CName,CNo)
        try:
            sql="update customer_details set CNo=%s where CName=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==2:
        CNo=int(input("enter the customer number of the customer:"))
        CName=input("enter the new name of the customer:")
        rl=(CName,CNo)
        try:
            sql="update customer_details set CName=%s where CNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==3:
        CNo=int(input("enter the customer number of the customer:"))
        CAge=int(input("enter the new age of the customer:"))
        rl=(CAge,CNo)
        try:
            sql="update customer_details set CAge=%s where CNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==4:
        CNo=int(input("enter the customer number of the customer:"))        
        CGender=input("enter the new gender of the customer:")
        rl=(CGender,CNo)
        try:
            sql="update customer_details set CGender=%s where CNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==5:
        CNo=int(input("enter the customer number of the customer:"))
        CPhone=input("enter the new phone number of the customer:")
        rl=(CPhone,CNo)
        try:
            sql="update customer_details set CPhone=%s where CNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    else:
        print("wrong choice")



#function for updating a train


def UpdateTrain():
    print("Select what to update:")
    print("1.train no")
    print("2.train name")
    print("3.train source")
    print("4.train destination")
    print("5.Time of departure from source")
    print("6.Time of arrival at destination")
    ch=int(input("Enter your choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        TName=input("enter the name of the train whose train number is to be changed:")
        TNo=int(input("Enter the new train number:"))
        rl=(TName,TNo)
        try:
            sql="update train set TNo=%s where TName=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==2:
        TNo=int(input("enter the train number of the train:"))
        TName=input("enter the new name of the train:")
        rl=(TName,TNo)
        try:
            sql="update train set TName=%s where TNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==3:
        TNo=int(input("enter the train number of the train:"))
        TSource=input("enter the new source of the train:")
        rl=(TSource,TNo)
        try:
            sql="update train set TSource=%s where TNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==4:
        TNo=int(input("enter the train number of the train:"))        
        TDestination=input("enter the new destination of the train:")
        rl=(TDestination,TNo)
        try:
            sql="update train set TDestination=%s where TNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==5:
        TNo=int(input("enter the train number of the train:"))
        Time_of_departure_from_source=input("enter the new departure time of the train:")
        rl=(Time_of_departure_from_source,TNo)
        try:
            sql="update train set Time_of_departure_from_source=%s where TNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    elif ch==6:
        TNo=int(input("enter the train number of the train:"))
        Time_of_arrival_at_destination=input("enter the new arrival time of the train:")
        rl=(Time_of_arrival_at_destination,TNo)
        try:
            sql="update train set Time_of_arrival_at_destination=%s where TNo=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    else:
        print("wrong choice")



#function for updating a booking

def UpdateBooking():
    print("Select what to update:")
    print("1.date of journey")
    ch=int(input("Enter your choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        PNR=int(input("enter the PNR number of the customer:"))        
        Date=input("enter the new date of journey of the customer:")
        rl=(Date,PNR)
        try:
            sql="update bookings set Date=%s where PNR=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    else:
        print("wrong choice")




#function for registering a train manager

def RegisterTM():
    L=[]
    TMName=input("Enter the name of the train manager:")
    L.append(TMName)
    TMPhone=input("enter train manager phone number:")
    L.append(TMPhone)
    TMGender=input("enter gender of train manager:")
    L.append(TMGender)
    TMPwd=input("enter new password:")
    L.append(TMPwd)
    value=L
    try:
        sql="insert into train_manager(TMName,TMPhone,TMGender,TMPwd) values(%s,%s,%s,%s)"
        mycursor.execute(sql,value)
        mydb.commit()
        print("Record registered")
    except Exception as e:
        print(e)
    s=TMPhone
    rl=(s,)
    try:
        sql="select TMID from train_manager where TMPhone=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for y in res:
            print(y[0]," is your train manager ID please remember it as your login ID")
        return res
    except Exception as e:
        print(e)


#function for displaying a train manager


def DisplayTM():
    print("Select the search criteria:")
    print("1.train manager ID")
    print("2.train manager name")
    print("3.train manager phone number")
    ch=int(input("Enter choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        s=TMID
        rl=(s,)
        try:
            sql="select * from train_manager where TMID=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for y in res:
                print(y)
        except Exception as e:
            print(e)
    elif ch==2:
        TMName=input("enter train manager name:")
        rl=(TMName,)
        try:
            sql="select * from train_manager where TMName=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for z in res:
                print(z)
        except Exception as e:
            print(e)
    elif ch==3:
        TMPhone=int(input("enter phone number of train manager:"))
        rl=(TMPhone,)
        try:
            sql="select * from train_manager where TMPhone=%s"
            mycursor.execute(sql,rl)
            res=mycursor.fetchall()
            for a in res:
                print(a)
        except Exception as e:
            print(e)



#function for updating a train manager

def UpdateTM():
    print("Select what to update:")
    print("1.train manager phone number")
    print("2.train manager password")
    ch=int(input("Enter your choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if ch==1:
        tmid=TMID
        s=input("Enter the new phone number:")
        rl=(s,tmid)
        try:
            sql="update train_manager set TMPhone=%s where TMID=%s"
            mycursor.execute(sql,rl)
            mydb.commit()
            print("Record updated")
        except Exception as e:
            print(e)
    elif ch==2:
        tmid=TMID
        s=input("enter the new password of train manager:")
        rl=(s,tmid)
        try:
            sql="update train_manager set TMPwd=%s where TMID=%s"
            mycursor.execute(sql,rl)
            print("Record updated")
            mydb.commit()
        except Exception as e:
            print(e)
    else:
        print("wrong choice")



#function for removing a train manager

def RemoveTM():
    TMID=int(input("Enter the ID of the train manager to be deleted:"))
    rl=(TMID,)
    try:
        sql="Delete from train_manager where TMID=%s"
        mycursor.execute(sql,rl)
        mydb.commit()
        print("Record deleted")
    except Exception as e:
            print(e)



#function for login as train manager

def Tlogin():
    global TMID
    TMID=int(input("enter train manager ID:"))
    TMPwd=input("enter pass:")
    cred=(TMID,)
    sql="select TMPwd from train_manager where TMID=%s"
    mycursor.execute(sql,cred)
    dpwd=mycursor.fetchall()
    if(TMPwd==dpwd[0][0]):
        return True
    else:
        return False

#function for login as customer
 
def Clogin():
    global CNo
    global TNo
    CNo=int(input("enter CNo:"))
    pwd=input("enter pass:")
    cred=(CNo,)
    sql="select CPwd from customer_details where CNo=%s"
    mycursor.execute(sql,cred)
    dpwd=mycursor.fetchall()
    if( pwd==dpwd[0][0]):
        return True
    else :
        return False
    
#function for running a programme again

def runAgain():
    runAgn = input("\nwant To Run Again y/n: ")
    while(runAgn.lower() == 'y'):
        if (platform.system() == "Windows"):
            os.system('cls')
        else:
            print(os.system('clear'))
        MenuSet()
        runAgn = input("\nwant To Run Again Y/n: ")



#main


def MenuSet():
    print(" ")
    print("====================================================")
    print(" ")
    print("RAILWAY RESERVATION SYSTEM")
    print("Created by Sreyansh Baranwal")
    print(" ")
    print("====================================================")
    print(" ")
    print("press 1 to login as customer")
    print("press 2 to register customer")
    print("press 3 to login as train manager")
    print("press 4 to register train manager")
    x=int(input("enter choice:"))
    print(" ")
    print("====================================================")
    print(" ")
    if x==1:
        if(Clogin()):
            while True:
                print(" ")
                print("====================================================")
                print(" ")
                print("press 1 to book a ticket")
                print("press 2 to display existing ticket")
                print("press 3 to update existing ticket")
                print("press 4 to cancel ticket")
                print("press 5 to display customer")
                print("press 6 to update customer")
                print("press 7 to remove customer")
                print("press 8 to exit")
                ch=int(input("enter choice:"))
                print(" ")
                print("====================================================")
                print(" ")
                if ch==1:
                    src=input("enter source station:")
                    dest=input("enter destination station:")
                    trains=SearchTrain(src,dest)
                    date=input('enter date in yyyy-mm-dd format:')
                    TNo=trains[0][0]
                    bookTicket(CNo,TNo,src,dest,date)
                    print("Ticket booked successfully")
                elif(ch==2):
                    DisplayBooking()
                elif(ch==3):
                    UpdateBooking()
                elif(ch==4):
                    RemoveBooking()
                elif(ch==5):
                    DisplayCustomer()
                elif(ch==6):
                    UpdateCustomer()
                elif(ch==7):
                    RemoveCustomer()
                elif(ch==8):
                    print("exiting .................")
                    break
                else:
                    print("wrong choice")      
        else:
            print("wrong username/password")
    elif x==2:
        RegisterCustomer()
    elif x==3:
        if(Tlogin()):
            while True:
                print(" ")
                print("====================================================")
                print(" ")
                print("press 1 to register train")
                print("press 2 to display train")
                print("press 3 to update train")
                print("press 4 to remove train")
                print("press 5 to display train manager")
                print("press 6 to update train manager")
                print("press 7 to remove train manager")
                print("press 8 to exit")
                ch=int(input("enter choice:"))
                print(" ")
                print("====================================================")
                print(" ")
                if ch==1:
                    RegisterTrain()
                elif(ch==2):
                    DisplayTrain()
                elif(ch==3):
                    UpdateTrain()
                elif(ch==4):
                    RemoveTrain()
                elif(ch==5):
                    DisplayTM()
                elif(ch==6):
                    UpdateTM()
                elif(ch==7):
                    RemoveTM()
                elif(ch==8):
                        print("exiting .................")
                        break
            else:
                print("wrong choice")      
        else:
            print("wrong username/password")
    elif x==4:
        RegisterTM()
    else:
        print("wrong input!!!!")



MenuSet()


runAgain() 




