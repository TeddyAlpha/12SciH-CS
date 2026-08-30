########################################################################---Import Area---##################################################################################
import csv
import pickle
import time as t
import random
from tkinter import messagebox

##########################################################################---SQL Login---#################################################################################


######################################################################---Function Building---###########################################################################


def custlist():
    f = open("orders.csv", "r", newline="\r\n")
    g = open("customers.txt", "w")
    r = csv.reader(f)
    datalist = list(r)
    headskip = datalist[1:]
    listc = []
    for i in headskip:
        client = i[1]

        if client not in listc:
            listc.append(client)

    for i in listc:
        g.write(i + "\n")
    f.close()
    g.close()

    print("Customer records stored in customers.txt")


orderdone = False


def supplierorder():
    global orderdone

    # 1. Try to see if the file exists by opening it in read mode
    try:
        f_check = open("suppliers.csv", "r")
        f_check.close()
        file_exists = True
    except FileNotFoundError:
        file_exists = False

    # 2. Open the file in append mode as usual
    f = open("suppliers.csv", "a", newline="")
    w = csv.writer(f)

    # 3. ONLY write the header row if the file didn't exist
    if not file_exists:
        head = [
            "Orderno",
            "Sumita Arora",
            "HCV",
            "SL Loney",
            "Cengage",
            "Stone",
            "Tesla Car",
        ]
        w.writerow(head)

    print("You will now be displayed the suppliers catalog")
    t.sleep(2)
    print("""
          
+-----------------------------------------------------------------------+
|                       📦 SUPPLY CATALOG 📦                       |
+----------------------------------------------------------------------+
|                                                                      |
|  1. Sumita Arora (CS Class 12) [Pack of 100].............  Rs. 70000 |
|  2. HC Verma (Concepts of Physics) [Pack of 200].......... Rs. 450K  |
|  3. SL Loney [Pack of 500]...............................  Rs. 150K  |
|  4. Cengage (JEE Advanced Math) [Pack of 50].............. Rs. 80K   |
|  5. Stone [Pack of 100K].................................. Rs. 9L    |
|  6. Tesla car .[Shipment of 100].......................... Rs. 2L    |
|                                                                      |
+-----------------------------------------------------------------------+

          
""")
    finalorder = []
    for i in range(1):
        orderid = random.randint(
            100000, 999999
        )  # gives random orderid everytime the order is taken so that when its like 2-3 orders it also works
        sumita = int(input("Enter number of packs of Sumita Arora Class 12 books: "))
        hcv = int(input("Enter number of packs of HC Verma Concepts of Physics: "))
        loney = int(input("Enter number of packs of SL Loney textbooks: "))
        cengage = int(input("Enter number of packs of Cengage Mathematics: "))
        stone = int(input("Enter number of loads of stones: "))
        tsla = int(input("Enter number of shipments of Tesla Cars: "))

        initorder = [orderid, sumita, hcv, loney, cengage, stone, tsla]
        finalorder.append(initorder)

    w.writerows(finalorder)
    orderdone = True

    totalcost = (
        (sumita * 70000)
        + (hcv * 450000)
        + (loney * 150000)
        + (cengage * 80000)
        + (stone * 900000)
        + (tsla * 2000000)
    )
    print(f"Your total cost is {totalcost}")

    def digitalinvoice():
        global finalbill
        f = open("invoice.txt", "w")
        f.write(
            "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
        )
        f.write(
            "------------------------------------------Supplier Invoice Generation System-------------------------------------------"
        )
        f.write(
            "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
        )
        f.write("\n")
        f.write(f"Username: Admin101 \n")
        f.write(f"Order Number: {orderid} \n")
        if sumita > 0:
            f.write(f" • Sumita Arora (CS 12)  x {sumita} : Rs. {sumita * 70000}/-\n")
        if hcv > 0:
            f.write(f" • HC Verma (Physics)    x {hcv} : Rs. {hcv * 450000}/-\n")
        if loney > 0:
            f.write(f" • SL Loney Textbooks    x {loney} : Rs. {loney * 150000}/-\n")
        if cengage > 0:
            f.write(
                f" • Cengage Mathematics   x {cengage} : Rs. {cengage * 800000}/-\n"
            )
        if stone > 0:
            f.write(f" • Inventory Stones      x {stone} : Rs. {stone * 9000000}/-\n")
        if tsla > 0:
            f.write(f" • Tesla Cars            x {tsla} : Rs. {tsla * 200000}/-\n")
        f.write(
            "><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><"
        )

        f.write(f"Grand total = {totalcost}")
        f.close()
        print("Invoice generated as 'invoice.txt'")

    wantinvoice = input("Do you want an invoice?: ")
    if wantinvoice == "yes":
        digitalinvoice()

    f.close()


def viewinv():
    f = open("inventory.csv", "r", newline="")
    r = csv.reader(f)

    headers = next(r)

    print("\n=============================================")
    print("        WAREHOUSE INVENTORY REPORT           ")
    print("=============================================")

    # Loop through each remaining row (Warehouse 1, 2, 3...)
    for row in r:
        ware_no = row[0]  # The warehouse number (1, 2, or 3)

        print(f"\n📦 WAREHOUSE NO: {ware_no}")
        print("-" * 30)

        for i in range(1, len(headers)):
            item_name = headers[i]
            stock_count = int(row[i])

            print(f" • {item_name}: {stock_count} units")

            if stock_count <= 10:
                print(f"   ⚠️ ALERT: Running critically low in Warehouse {ware_no}!")
                messagebox.showwarning(
                    "Low Stock Alert",
                    f"CRITICAL WARNING:\n{item_name} has only {stock_count} units left in Warehouse {ware_no}!",
                )

        print("-" * 30)

    f.close()
    print("\n===================================================================================================\n")


def viewbadmosh():

    q = input("Do you want to view suggestions or complaints? ").lower().strip()

    if q in ["suggestion", "suggestions"]:
        try:
            with open("suggestions.dat", "rb") as g:
                while True:
                    suggest = pickle.load(g)
                    print(suggest + "\n")
        except EOFError:
            pass
        except FileNotFoundError:
            print("No suggestions recorded yet.")

    elif q in ["complaint", "complaints"]:
        try:
            with open("complaints.dat", "rb") as f:
                while True:
                    complaint = pickle.load(f)
                    print(complaint + "\n")
        except EOFError:
            pass
        except FileNotFoundError:
            print("No complaints received yet (good job).")

    else:
        print("Invalid choice. Please type 'suggestions' or 'complaints'.")


def platform_revenue():
    customer_revenue = 0
    try:
        f = open("orders.csv", "r", newline="")
        r = csv.reader(f)
        next(r)

        for row in r:
            sumita = int(row[2])
            hcv = int(row[3])
            loney = int(row[4])
            cengage = int(row[5])
            stone = int(row[6])
            tsla = int(row[7])

            order_total = (
                (sumita * 70000)
                + (hcv * 450000)
                + (loney * 150000)
                + (cengage * 80000)
                + (stone * 900000)
                + (tsla * 2000000)
            )
            customer_revenue += order_total
        f.close()
    except FileNotFoundError:
        customer_revenue = 0

    supplier_expenses = 0
    try:
        sf = open("suppliers.csv", "r", newline="")
        sr = csv.reader(sf)

        for row in sr:
            s_sumita = int(row[1])
            s_hcv = int(row[2])
            s_loney = int(row[3])
            s_cengage = int(row[4])
            s_stone = int(row[5])
            s_tsla = int(row[6])

            supplier_total = (
                (s_sumita * 70000)
                + (s_hcv * 450000)
                + (s_loney * 150000)
                + (s_cengage * 80000)
                + (s_stone * 900000)
                + (s_tsla * 2000000)
            )
            supplier_expenses += supplier_total
        sf.close()
    except FileNotFoundError:
        supplier_expenses = 0

    net_profit = customer_revenue - supplier_expenses
    print('Loading Revenue chart, kindly hold on')
    for i in range(10):
        t.sleep(0.15)
        print(">", end="", flush=True) 
    print('Revenue Chart generated.')
    print('\n'*2)

    print("\n" + "=" * 60)
    print(""" 
          
/$$$$$$$                                                                     /$$$$$$  /$$                             /$$    
| $$__  $$                                                                   /$$__  $$| $$                            | $$    
| $$  \ $$  /$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$  /$$   /$$  /$$$$$$       | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  
| $$$$$$$/ /$$__  $$|  $$  /$$//$$__  $$| $$__  $$| $$  | $$ /$$__  $$      | $$      | $$__  $$ |____  $$ /$$__  $$|_  $$_/  
| $$__  $$| $$$$$$$$ \  $$/$$/| $$$$$$$$| $$  \ $$| $$  | $$| $$$$$$$$      | $$      | $$  \ $$  /$$$$$$$| $$  \__/  | $$    
| $$  \ $$| $$_____/  \  $$$/ | $$_____/| $$  | $$| $$  | $$| $$_____/      | $$    $$| $$  | $$ /$$__  $$| $$        | $$ /$$
| $$  | $$|  $$$$$$$   \  $/  |  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$$      |  $$$$$$/| $$  | $$|  $$$$$$$| $$        |  $$$$/
|__/  |__/ \_______/    \_/    \_______/|__/  |__/ \______/  \_______/       \______/ |__/  |__/ \_______/|__/         \___/  
                                                                                                                                
          
          """)

    print("\n" * 4)
    print("=" * 60)

    # Just learnt that ,.2f is a way of using the f string, it turns a number into like if 50000.0, it becomes 50,000.00 the 2f puts decimal places and the comma puts comma
    print(f" Total Gross Revenue (Sales)       :  Rs. {customer_revenue:,.2f}")
    print(f" Total Capital Expenditure (Supply) :  Rs. {supplier_expenses:,.2f}")
    print("-" * 60)

    if net_profit >= 0:
        print(f" NET SYSTEM SURPLUS (PROFIT)       :  Rs. {net_profit:,.2f}")
        print(f" STATUS                            :  OPERATIONAL MARGIN IN THE GREEN")
    else:
        print(f" NET SYSTEM DEFICIT (LOSS)         :  Rs. {abs(net_profit):,.2f}")
        print(f" STATUS                            :  OPERATIONAL MARGIN IN THE RED")

    print("=" * 60 + "\n")


#####################################################################---Main Code Integration---######################################################################

print(f"\n--- INVENTIFY ADMINISTRATOR PORTAL  ---")

while True:
    print("\n+---------------------------------------+")
    print("|          ADMIN INTERFACE              |")
    print("+---------------------------------------+")
    print("|  [1]  View Customer List              |")
    print("|  [2]  Display Current Inventory       |")
    print("|  [3]  Place Order to Supplier         |")
    print("|  [4]  Complaints and Suggestions      |")
    print("|  [5]  Balance and Revenue Sheet       |")
    print("|  [6]  Log Out                         |")
    print("+---------------------------------------+")

    try:
        choice = int(input("Select option (1-6): "))
    except ValueError:
        print("ERROR: Invalid input format. Select a numeric option between 1 and 6.")
        continue

    print("\n" + "-" * 41)

    if choice == 1:
        custlist()
    elif choice == 2:
        viewinv()
    elif choice == 3:
        supplierorder()
    elif choice == 4:
        viewbadmosh()
    elif choice == 5:
        platform_revenue()
    elif choice == 6:
        print(f"Session terminated. Logging out user...")
        t.sleep(1)

        print(
            "<3 Made with love (and fear of swapnil mam) by anay, 12SciH Batch of 2627"
        )
        break

    else:
        print("ERROR: Selection out of range. Select an option from 1 to 6.")

        print("-" * 41)
