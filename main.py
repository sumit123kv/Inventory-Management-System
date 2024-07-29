import Button
import Rent
import Return
print("-------------------------------------------------------------")
print("| | ** Hello!!!Welcome to An Event Equipment Rental shop!!! **  | | ")
print("------------------------------------------------------------")
user_name=input("Enter your fullname:")
print("\nHello Mr/Miss "+user_name+", please follow the given instructions properly.")

iteration=True
while iteration==True:    
    try:
        Button.input_()         #calling function 
        user_input=int(input("\nEnter a number:"))
        success=False
        while success==False:
            if user_input==1:
                Button.read()   #calling function 
                success=True
                
            elif user_input==2:
                contents2=Button.read2()#calling function 
                cart=[]
                check="y"
                while check=="y":
                    id=input("\nEnter a  ID:")
                    Id=id.upper()
                    value=Rent.Rent(Id,contents2)#calling function 
                    tCart=Rent.temp_cart(Id,value)#function calling
                    if len(tCart)>0:
                        cart.append(tCart[0])
                        print("Equipment Rented Successfully!! Thank you for Renting Equipment from us.\n")
                    contents2=Button.read2()#calling function in this line   
                    check=input("\nDo you want to Rent another equipment? Press y for Yes and n for No (y/n):")                 
                print("\nThe cart is")
                print(cart)
                Rent.rent_note("Rent Note.txt","w",cart,user_name)#calling function 
                print("\nRent note has been generated Successfully.")
                success=True

            elif user_input==3:
                contents2=Button.read2()#calling function 
                cart2=[]
                check2="y"
                while check2=="y":
                    id=input("\nEnter a  ID:")
                    Id=id.upper()
                    value=Return.Return(Id,contents2)#function calling
                    tCart2=Return.temp_cart2(Id,value)#function calling
                    if len(tCart2)>0:
                        cart2.append(tCart2)
                        print("Equipment Returned Successfully!!\n")
                    contents2=Button.read2()    
                    check2=input("\nIs there another equipment to return? Press y for Yes and n for No (y/n):")    
                print("\nThe cart is")
                print(cart2)
                sum_=0
                grand_total=Return.total(cart2,sum_)#function calling 
                Return.return_note("Return Note.txt","w",cart2,user_name,grand_total)#caling function
                print("\nReturn note has been generated")
                success=True
                    
            elif user_input==4:
                success=True
                iteration=False
                exit()
                   
            else:
                print("\nInvalid input!!! Please enter a number from 1 to 4.")
                success=True
    except:
        print("Thank you for using An Event Equipment Rental shop")
        
        
