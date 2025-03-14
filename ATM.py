print("************************")
print("WELCOME TO ATM")
print("************************")

Accounts = {
    2000 : ["user1","1-1-2025",10000,2002],
    2001 : ["user2","1-2-2025",20000,2002],
    2002 : ["user3","1-2-2025",30000,None],
    2003 : ["user4","1-3-2025",40000,None],
    2004 : ["user5","1-4-2025",20000,2004],
    2005 : ["user6","1-4-2025",30000,2004]}
dobm = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose your option")
    print("1.Withdrawl")
    print("2.Deposit")
    print("3.Pin generation")
    print("4.Mini statement")
    print("5.Transfer Funds")
    print("6.Exit")
    option = int(input())
    print()
    if option == 1:
        print("************************")
        Accno = int(input("Enter Your Account Number "))
        if Accno not in Accounts:
            print("**Account doesnot exist**")
        else:
            pin = int(input("Please enter your pin: "))
            if Accounts[Accno][-1]!=pin:
                print("**Invalid pin**")
            else:
                if Accounts[Accno]==None:
                    print("**Generate pin**")
                else:
                    amount = int(input("Please enter amount: "))
                    if amount<= Accounts[Accno][-2]:
                        print("Withdrawl successfully")
                        Accounts[Accno][-2]-=amount
                    else:
                        print("************************")

                        print("Insufficient funds")
                        print("************************")
    elif option == 2:
        print("************************")
        accno=int(input("Enter your account number: "))
        if accno not in Accounts:
            print("**Account does not exist**")
        else:
            amt = int(input("Enter the amount: "))
            Accounts[accno][-2]+=amt
            print("************************")
            print("**Deposit successfull**")
            print("************************")
    elif option == 3:
        Acc1=int(input("Enter your account number "))
        if Acc1 not in Accounts:
            print("**Account does not exist**")
        else:
            pin=int(input("Enter your pin: "))
            cpin = int(input("Confirm pin: "))
            if cpin!= pin:
                print("**Pin Doesnt Match**")
            else:
                Accounts[Acc1][-1]=pin
                print("************************")

                print("Pin Generated Successfully")
                print("************************")
    elif option ==4:
        accno2 = int(input("Enter your account number: "))
        if accno2 not in Accounts:
            print("Account doesnt exist")
        else:
            pin =int(input("Enter Your Pin: "))
            if pin!=Accounts[accno2][-1]:
                print("**Invalid pin**")
            else:
                print(f"Name: {Accounts[accno2][0]} ")
                print(f"Account Number: {accno2}")
                dob = Accounts[accno2][1].split("-")
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dob[2]
                dob = date + "-"+month+"-"+year
                
                print(f"Date Of Birth:{dob}")
                print(f"Account Balance: {Accounts[accno2][-2]}")
            print("************************")
            print("************************")
    elif option == 5:
        Accno3 =int(input("Enter Your Account Number: "))
        if Accno3 not in Accounts:
            print("************************")
            print("**Account doesnt Exist**")
            print("************************")
        else:
            accno3 = int(input("Please enter the account number which you need to Transfer the funds: "))
            if accno3>9999:
                print("**Account number should be exact 4 digits**")
            else:
                amt2 = int(input("Please enter the amount to Transfer Funds: "))
                if amt2<= Accounts[Accno3][-2]:
                    print("************************")

                    print("**Amount Had Been Transferred**")
                    print("************************")

                    Accounts[accno3][-2]-=amt2
                else:
                    print("************************")
                    print("**Insuffcient Funds in Your Account!**")
                  
                    print("************************")
    else:
        break
    
    
    

    
      
                
            
    
                
                
                    
            
    

                

                                     

                    
    
    
    
