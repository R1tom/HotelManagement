import random
class hotel:
 

    def rooms(s):

            global count,ac_room,non_ac_room,avail_room
            print(" ________   _______  ________  ____         __    ")
            print("||       |||       |||       ||| | |||||||||  ||||")
            print("|| ||||| ||| ||||| ||| ||||| ||| || ||||||| | ||||")
            print("|| ||||| ||| ||||| ||| ||||| ||| ||| ||||| || ||||")
            print("|| ||||| ||| ||||| ||| ||||| ||| |||| ||| ||| ||||")
            print("|| |   | ||| ||||| ||| ||||| ||| ||||| | |||| ||||")
            print("|| |  |||||| ||||| ||| ||||| ||| |||||| ||||| ||||")
            print("|| ||  ||||| ||||| ||| ||||| ||| |||||||||||| ||||")
            print("|| |||  |||| ||||| ||| ||||| ||| |||||||||||| ||||")
            print("|| ||||  |||       |||       ||| |||||||||||| ||||")
            print("  --   ---  --------  -------  ---          ---   ")
            print("..................................................")
            print("Price for AC room /per night     : 750/-")
            print("Price for non-AC room /per night : 500/-")
            print("..................................................")
            print("..................................................")
            print("Total rooms available  : ",avail_room)
            print("non-AC rooms available : ",non_ac_room)
            print("AC rooms avilable      : ",ac_room)
            print("..................................................")
            print("Total guest staying    :  ")
            total_staying=int(input())
            print("How many days the guests will be staying :  ")
            days_staying.append(int(input()))
            room_id.append(random.randint(1,101))
            if(total_staying<=2):
                room_occupy.append(1)
                print("2 people are staying : So two 1 single room : with two bed is required ")
                print("..................................................")
                print("..................................................")
                print("Select 1 for AC room \nSelect 2 for non-AC room :")
                roomChoose=int(input())
                if(roomChoose==1):
                    ac_room-=1
                    print("AC room selected")
                    room_price.append(750)
                elif(roomChoose==2):
                    non_ac_room-=1
                    print("non_AC room selected")
                    room_price.append(500)
                else:
                    print ("Please select either 1 or 2")
                    print("..................................................")
                    print("..................................................")
                    print("Select 1 for AC room \nSelect 2 for non-AC room : ")
                    roomChoose=int(input())
                    if(roomChoose==1):
                        ac_room-=1
                        print("AC room selected")
                        room_price.append(750)
                    elif(roomChoose==2):
                        non_ac_room-=1
                        print("non_AC room selected")
                        room_price.append(500)
                    else:
                        print ("Please select either 1 or 2")

            elif(total_staying>2 and total_staying<=4):
                room_occupy.append(2)
                print("Since",total_staying," people are staying :  So 2 single room : with two bed each is required ")
                print("..................................................")
                print("..................................................")
                print("..................................................")
                print("Select 1 for AC room \nSelect 2 for non-AC room")
                roomChoose=int(input())
                if(roomChoose==1):
                    ac_room-=2
                    print("AC room selected")
                    room_price.append(750)
                elif(roomChoose==2):
                    non_ac_room-=2
                    print("non_AC room selected")
                    room_price.append(500)
                else:
                    print ("Please select either 1 or 2")
                    print("Select 1 for AC room \nSelect 2 for non-AC room")
                    roomChoose=int(input())
                    if(roomChoose==1):
                        ac_room-=2
                        print("AC room selected")
                        room_price.append(750)
                    elif(roomChoose==2):
                        non_ac_room-=2
                        print("non_AC room selected")
                        room_price.append(500)
                    else:
                        print ("Please select either 1 or 2")
                

            else:
                room_occupy.append(3)
                print("Since",total_staying," people are staying : so 3 single room : with two bed each is required ")
                print("..................................................")
                print("..................................................")
                print("..................................................")
                print("Select 1 for AC room \n Select 2 for non-AC room")
                roomChoose=int(input())
                if(roomChoose==1):
                    ac_room-=3
                    print("AC room selected")
                    room_price.append(750)
                elif(roomChoose==2):
                    non_ac_room-=3
                    print("non_AC room selected")
                    room_price.append(500)
                else:
                    print ("Please select either 1 or 2")
                    print("Select 1 for AC room \n Select 2 for non-AC room")
                    roomChoose=int(input())
                    if(roomChoose==1):
                        ac_room-=3
                        print("AC room selected")
                        room_price.append(750)
                    elif(roomChoose==2):
                        non_ac_room-=3
                        print("non_AC room selected")
                        room_price.append(500)
                    else:
                        print ("Please select either 1 or 2")
                
            print(".........................................................")
            print(".........................................................")
            print("Your Room no is", room_id)
            print("THANK YOU FOR VISITING OUR HOTEL SIR/MADAM : HAVE A GREAT DAY : THANK YOU ")
            print(".........................................................")
            print(".........................................................")
            print(".........................................................")

            total_price.append(room_price[count]*room_occupy[count]*days_staying[count])

            s.starting()
            count+=1

            
            
    
    def starting(s):
        global g_Id 
        print("\n")
        print(".........................................................")
        print("1 . CHECKIN")
        print("2 . SHOW GUEST LIST")
        print("3 . CHECKOUT")
        print("4 . GET INFO OF ANY GUEST")
        print("5 . EXIT")

        choose= int(input(" \n Enter your choice - "))
        print(".........................................................")
        print(".........................................................")

        if(choose==1):
            s.checkin()
        elif(choose==2):
            s.guestList()
        elif(choose==3):
            s.checkout()
        elif(choose==4):
            s.query()
        elif(choose==5):
            s.exit()
        else:
            print("\n Please choose from the list ","\n")
            starting()


    def checkin(s):
        global g_Id,count,id_count,n
        
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ")
        print("|      || |||| ||       ||      || |||||| ||| ||   |||||| ||||||||")
        print("| ||||||| |||| || |||||||| ||||||| ||||| |||| || | |||||| ||||||||")
        print("| ||||||| |||| || |||||||| ||||||| |||| ||||| || || ||||| ||||||||")
        print("| |||||||      ||       || ||||||| ||| |||||| || ||| |||| ||||||||")
        print("| ||||||| |||| || |||||||| ||||||| || ||||||| || |||| ||| ||||||||")
        print("| ||||||| |||| || |||||||| ||||||| | |||||||| || ||||| || ||||||||")
        print("| ||||||| |||| || |||||||| ||||||| | |||||||| || |||||| | ||||||||")
        print("|      || |||| ||       ||      || || ||||||| || |||||||  ||||||||")
        print("|||||||||||||||||||||||||||||||||| ||| |||||||||||||||||||||||||||") 
        try:
            print(".........................................................")
            print(".........................................................")
            g_name.append(input("Enter the Guest name           : "))
            g_gender=input("Enter the Guest gender   : M\F : ")
            g_age=int(input("Enter the Guest age            : "))
            g_phone.append(int(input("Enter the Guest contact number : ")))
            g_Id.append(int(input("Enter the Guest ID             : ")))
            
            for n in range(id_count):
                if(g_Id[n]==g_Id[id_count]):
                    print("Guest ID already exist : Enter a new one")
                    del g_Id[n]
                    g_Id.append(int(input("Enter the Guest ID             : ")))
                    
            print(".........................................................")
            print(".........................................................")
        except:
            print("LOOKS LIKE SOMETHING IS WRONG : PLEASE ENTER VALID INPUTS")
            s.checkin()
        
        id_count+=1
        s.rooms()
        


    def checkout(s):
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||") 
        print("|      || |||| ||       ||      || |||||| ||      || ||| ||        ||")
        print("| ||||||| |||| || |||||||| ||||||| ||||| ||| |||| || ||| |||||| |||||")
        print("| ||||||| |||| || |||||||| ||||||| |||| |||| |||| || ||| |||||| |||||")
        print("| |||||||      ||       || ||||||| ||| ||||| |||| || ||| |||||| |||||")
        print("| ||||||| |||| || |||||||| ||||||| || |||||| |||| || ||| |||||| |||||")
        print("| ||||||| |||| || |||||||| ||||||| | ||||||| |||| || ||| |||||| |||||")
        print("| ||||||| |||| || |||||||| ||||||| | ||||||| |||| || ||| |||||| |||||")
        print("|      || |||| ||       ||      || || ||||||      ||     |||||| |||||")
        print("|||||||||||||||||||||||||||||||||| ||| ||||||||||||||||||||||||||||||")
        global i,ac_room,non_ac_room,total_price,room_price,room_occupy,days_staying
        print("Right now guest staying at our hotel   : ",g_name)
        print(".........................................................")
        print(".........................................................")
        print(".........................................................")
        print("For Checkout enter the Guest name      : ")
        checkout=str(input())
        count_g_name=int(len(g_name))
        print(count_g_name)
        for i in range(count_g_name):
            if(g_name[i]==checkout):
                print("Guest name : ",g_name[i]," And Guest ID is : ",g_Id[i])
                
                break
            
                  
        print("\n")
        print("Proceeding to the Bill section...........................")
        print(".........................................................")
        print(".........................................................")
        
        s.bill()



    def bill(s):
        global i,ac_room,non_ac_room,count
        print("Guest name : ",g_name[i])
        print("Guest ID   : ",g_Id[i])
        if(room_price[i]==500):
            room="non-AC"
        else:
            room="AC"
        
        print("Room type  : ",room,"room")
        print("Room ID    : ",room_id[i])
        print("Total days stayed : ",days_staying[i],)
        print(".........................................................")
        print(".........................................................")

        if(room=="AC"):
            GST=19/100
        else:
            GST=8/100

        print("GST applied for : ",g_name[i]," is : ",GST ,"per 100/-")
        
        total_price[i]=total_price[i]*GST+total_price[i]

        print("Total amount to be paid : ",total_price[i])

        if(room_occupy[i]==1 and room=="AC"):
            ac_room+=1
        elif(room_occupy[i]==1 and room=="non_AC"):
            non_ac_room+=1
        if(room_occupy[i]==2 and room=="AC"):
            ac_room+=2
        elif(room_occupy[i]==2 and room=="non_AC"):
            non_ac_room+=2
        if(room_occupy[i]==3 and room=="AC"):
            ac_room+=3
        elif(room_occupy[i]==1 and room=="non_AC"):
            non_ac_room+=3

        print(".........................................................")
        print(".........................................................")
        del g_name[i]
        del g_Id[i]
        del room_id[i]
        del days_staying[i]
        del total_price[i]
        del room_occupy[i]
        del g_phone[i]
        del room_price[i]
        
        
        s.starting()
        count-=1
        i-=1
        
        
    def query(s):
        global g_name,room_price,g_Id,g_phone,room_id
        if(room_price==500):
            roomType="non-AC"
        else:
            roomType="AC"
        print(".........................................................")
        print("1 .list of all guest staying at the hotel")
        print("2 .searching for a particular guest")
        print("3 .exit to the main menu")
        choose=int(input("please choose : "))
        if(choose==1):
            print("All the guest staying at our hotel : ")
            print(g_name)
            s.query()
        elif(choose==2):
            print("Enter the name of the guest you want to search : ")
            query_name=input()
            query_size=int(len(g_name))
            j=0
            for j in range(query_size):
                if(g_name[j] == query_name):
                    print("Search succesful : ")
                    print("Guest name : ",g_name[j]," Guest ID : ",g_Id[j])
                    print("Guest contact number : ",g_phone[j])
                    print("He is staying in a : ",roomType," room & the Room ID is : ",room_id[j])
                    break
            

        elif(choose==3):
            s.starting()
        else:
            print("Please choose either 1 or 2 ")
            s.query()
        
        s.starting()

    def exit(s):
        global goOn
        goOn=False
        exit()

    def guestList(s):
        print("List of all guest : ",g_name)
        print(".........................................................")
        print(".........................................................")
        
            
g_name=[]
g_Id=[]
g_age=0
g_gender=""
g_phone=[]

ac_room= 25
non_ac_room=15
occupied_room=60
avail_room=non_ac_room+ac_room
total_room=occupied_room+avail_room
room_price=[]
total_staying=0
room_occupy=[]
total_price=[]
days_staying=[]
room_id=[]

i=0
id_count=0
n=0

g_bill=0
g_list=[]

goOn=True
count=0


obj= hotel()
while(goOn):
    obj.starting()



