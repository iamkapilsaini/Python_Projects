import function

pin = 1234

for i in range(0,3):
    cpin = int(input("Enter your 4 Digit PIN : "))
    if cpin == pin:
        print("Login Successfully!")


        no = 0
        while(no!= 1 and no!=2 and no!=3 and no!=4):
            print("\nWhat you want to do : \n1. Balance_check      2. Deposite_Money \n3. Withdraw_money     4. Exit ")
            
            check = int(input("Enter the no. from 1, 2, 3, 4 :-  "))
            
            if(check != 1 and check!= 2 and check!=3 and check!=4):
                print("Choose valid no.")

            elif(check == 1):
                # function.getbalance()
                print(f"Current balance: {function.getbalance()} Rs")
                

            elif(check == 2):
                function.deposite()


            elif(check == 3):
                function.withdraw()


            elif(check == 4):
                break

        no = check
        break

    else:
        print("Incorrect PIN")
        print(f"{2-i} attempt left\n")
        if i == 2:
            print("login failed!")
        
