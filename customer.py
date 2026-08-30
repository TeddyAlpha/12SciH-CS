#############################################################-----Import Area-----#################################################################################
import pickle
import time as t
import csv
import random

############################################################------SQL Login-----###################################################################################

#UPDATE THE README FILE ELSE ULL FAIL

########################################################------ Function Definition ------############################################################################


def viewpastorder():
    import main

    kaun = main.username.lower()  # see i used the username thing here
    f = open("orders.csv", "r", newline="")
    r = csv.reader(f)
    next(r)

    print(f"Showing history for user {kaun}: ")        
    print("-" * 60)
    global hasorder
    hasorder = False

    for i in r:
        if i[1].lower() == kaun:
            clean = (
                [i[0]] + i[2:]
            )  # removes username as if rohan is asking for order he knows it he shouldnt see his name at beginning of every entry
            print(clean)
            hasorder = True

    if hasorder == False:
        print("You do not have any past orders")

    f.close()


def complaint():

    # uses a beautiful double fork topography

    print("Loading the complaints and suggestions tab")
    print("Please note that your suggestions are kept anonymous")

    for i in range(10):
        t.sleep(0.15)
        # writing a basic like loading screen
        print(">", end="", flush=True)
        #what is flush? flush just prints the 

    print("\n")

    f = open("suggestions.dat", "ab")
    g = open("complaints.dat", "ab")

    q = input("Do you want to submit a suggestion or a complaint")

    if q.lower() == "suggestion":

        n = int(input("How many suggestions do you wish to submit?"))

        l = []
        for i in range(n):
            q = eval(input(f"Please enter suggestion {i+1}: "))

            if type(q) != list:
                print(
                    "Kindly enter suggestion in form of a list only so we can process it easily"
                )
                break

            l.append(q)

        for suggestion in l:
            pickle.dump(suggestion, f)

        f.close()

    elif q.lower() == "complaint":

        n = int(input("How many complaints do you wish to submit?"))

        l = []
        for i in range(n):
            q = eval(input(f"Please enter complaint {i+1}: "))

            if type(q) != list:
                print(
                    "Kindly enter complaint in form of a list only so we can process it easily"
                )
                break

            l.append(q)

        for suggestion in l:
            pickle.dump(suggestion, g)

        print(" Thank you for your patience, we will respond to you shortly...")
        g.close()


ordermade = False


def ordergoods():
    global ordermade

    # Try to see if the file exists by opening it in read mode
    try:
        f_check = open("orders.csv", "r")
        f_check.close()
        file_exists = True
    except FileNotFoundError:
        file_exists = False

    # Open the file in append mode as usual
    f = open("orders.csv", "a", newline="")
    w = csv.writer(f)

    # ONLY write the header row if the file is brand new
    if not file_exists:
        head = [
            "Orderno",
            "Customer",
            "Sumita Arora",
            "HCV",
            "SL Loney",
            "Cengage",
            "Stone",
            "Tesla Car",
        ]
        w.writerow(head)

    import main

    userkaun = main.username

    print("Now we will be showing you the catalog of our items, Kindly wait")
    t.sleep(2)
    print("""
          
+-----------------------------------------------------------------------+
|                       📦 INVENTIFY CATALOG 📦                       |
+----------------------------------------------------------------------+
|                                                                      |
|  1. Sumita Arora (CS Class 12) ........................... Rs. 700   |
|  2. HC Verma (Concepts of Physics) ....................... Rs. 450   |
|  3. SL Loney ............................................. Rs. 150   |
|  4. Cengage  ............................................. Rs. 800   |
|  5. Stone ................................................ Rs. 900   |
|  6. Tesla car ............................................ Rs. 200   |
|                                                                      |
+-----------------------------------------------------------------------+

          
""")
    

    finalorder = []

    for i in range(1):

        orderid = random.randint(
            100000, 999999
        )  # gives random orderid everytime the order is taken so that when its like 2-3 orders it also works
        sumita = int(input("Enter number of Sumita Arora Class 12 books: "))
        hcv = int(input("Enter copies of HC Verma Concepts of Physics: "))
        loney = int(input("Enter number of SL Loney textbooks: "))
        cengage = int(input("Enter copies of Cengage Mathematics: "))
        stone = int(input("Enter number of stones: "))
        tsla = int(input("Enter number of Tesla Cars: "))

        initorder = [orderid, userkaun, sumita, hcv, loney, cengage, stone, tsla]

        finalorder.append(initorder)

    w.writerows(finalorder)

    ordermade = True

    totalcost = (
        (sumita * 700)
        + (hcv * 450)
        + (loney * 150)
        + (cengage * 800)
        + (stone * 900)
        + (tsla * 200)
    )
    print(f"Your total cost is {totalcost}")

    minus = 0

    global finalbill
    finalbill = totalcost

    havepromo = input("Do you have a promo code/discount coupon? ")

    discountgiven = False

    if havepromo == "yes":
        
        try:
            f_check = open("promos.txt", "r")
            f_check.close()
        except FileNotFoundError:
            f_create = open("promos.txt", "w")
            f_create.write("SAVE20\n")
            f_create.close()
        

        f = open("promos.txt", "r")
        z = f.read()
        f.close()
        q = z.splitlines()
        promo = input("Enter your promo code")
        if promo.upper() in q:

            print("Promo code successfully applied! ")

            minus = totalcost * 0.20  # default promo is always always always 20 percent
            finalbill = totalcost - minus

            print(f"Your final bill is of INR {finalbill}: ")
            discountgiven = True

        else:
            print("Promo coupon not found")

    elif havepromo == "no":
        print(f"Okay, your total bill is {finalbill} ")

    def digitalinvoice():
        global finalbill
        f = open("invoice.txt", "w")
        f.write(
            "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
        )
        f.write(
            "------------------------------------------Inventify Invoice Generation System-------------------------------------------"
        )
        f.write(
            "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
        )
        f.write("\n")
        f.write(f"Username: {userkaun} \n")
        f.write(f"Order Number: {orderid} \n")
        if sumita > 0:
            f.write(f" • Sumita Arora (CS 12)  x {sumita} : Rs. {sumita * 700}/-\n")
        if hcv > 0:
            f.write(f" • HC Verma (Physics)    x {hcv} : Rs. {hcv * 450}/-\n")
        if loney > 0:
            f.write(f" • SL Loney Textbooks    x {loney} : Rs. {loney * 150}/-\n")
        if cengage > 0:
            f.write(f" • Cengage Mathematics   x {cengage} : Rs. {cengage * 800}/-\n")
        if stone > 0:
            f.write(f" • Inventory Stones      x {stone} : Rs. {stone * 900}/-\n")
        if tsla > 0:
            f.write(f" • Tesla Cars            x {tsla} : Rs. {tsla * 200}/-\n")
        f.write(
            "><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><"
        )

        f.write(f"Grand total = {finalbill}")
        if discountgiven == True:
            f.write(f"Discount applied using promo code {promo.upper()}: {minus}")
        f.close()
        print("Invoice generated as 'invoice.txt'")

    wantinvoice = input("Do you want an invoice?: ")
    if wantinvoice == "yes":
        digitalinvoice()

    f.close()


def accessorder():
    global ordermade
    if ordermade == False:
        print(
            "Your order is not finalised yet, kindly call for an order and come back here"
        )
        return
    else:
        f = open("orders.csv", "r", newline="\r\n")
        r = csv.reader(f)
        next(r)
        orderlist = list(r)
        datalist = orderlist  # skips the header and only gives list of all the data

        # next stops it from editing the header

        haveorderno = input("Do you have your order number? ")
        global orderFound
        orderFound = False

        if haveorderno.lower() in ["y", "yes", "yeah", "haan"]:
            giveorderno = int(input("Kindly provide your order number here: "))
            for i in range(len(datalist)):
                if int(datalist[i][0]) == giveorderno:
                    print(datalist[i])
                    orderFound = True

            if orderFound == False:
                print("Sorry, your order was not found")
        else:
            namefound = False
            retry = input("Kindly give us the name used on the order")
            t.sleep(1)
            for i in range(len(datalist)):
                found1=0
                if datalist[i][1] == retry:
                    if found1==0:
                        print("Found your order(s) here: Kindly verify if it is yours: ")
                        found1==1

                    print(datalist[i])
                    namefound = True
            if namefound == False:
                print("Sorry, your name was not found")

        f.close()


def cancelorder():
    whatcancel = int(input("Kindly enter the order number to cancel"))
    f = open("orders.csv", "r", newline="\r\n")
    r = csv.reader(f)
    listfile = list(r)
    header = listfile[0]
    data = listfile[1:]
    f.close()
    updatedorder = []
    found = False
    for i in data:
        if int(i[0]) == whatcancel:
            found = True
            continue
        updatedorder.append(i)
    if found == True:
        f = open("orders.csv", "w", newline="")  # clears the entire file
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(updatedorder)

        print(f"Order no {whatcancel} has been cancelled")
    else:
        print("Order ID not found")
    f.close()


###############################################---End of Function Definition---###########################################

print(f"\n--- INVENTIFY ENTERPRISE PORTAL  ---")

while True:
    print("\n+---------------------------------------+")
    print("|          INVENTIFY INTERFACE          |")
    print("+---------------------------------------+")
    print("|  [1]  Browse Catalog & Place Order    |")
    print("|  [2]  Track / Access Existing Order   |")
    print("|  [3]  View Past Order History         |")
    print("|  [4]  Cancel Existing Order           |")
    print("|  [5]  Submit Feedback & Complaints    |")
    print("|  [6]  Terminate Session / Log Out     |")
    print("+---------------------------------------+")

    try:
        choice = int(input("Select option (1-6): "))
    except ValueError:
        print("ERROR: Invalid input format. Select a numeric option between 1 and 6.")
        continue

    print("\n" + "-" * 41)

    if choice == 1:
        ordergoods()
    elif choice == 2:
        accessorder()
    elif choice == 3:
        viewpastorder()
    elif choice == 4:
        cancelorder()
    elif choice == 5:
        complaint()
    elif choice == 6:
        print(f"Session terminated. Logging out user...")
        t.sleep(1)
        break
    else:
        print("ERROR: Selection out of range. Select an option from 1 to 6.")

    print("-" * 41)
