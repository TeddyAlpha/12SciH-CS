#############################################################-----Import Area-----#################################################################################
import time as t


########################################################------ Function Definition ------############################################################################
def usern():
    global nme
    nme = input(
        "Welcome to Inventify, your inventory management system. Before we get started, please enter your name: "
    )
    return nme


# id built this function just so that i can call usern everwhere all over the files and use it, main purpose for this


def intro():
    global username
    print(
        """
     █████                                              ███     ███     ██████            
    ░░███                                             ░░███     ░░░     ███░░███           
     ░███   ████████   ███  ████  ███████   ████████   ███████  ████   ░███ ░░░  █████ ████
     ░███ ░░███░░███ ░░███ ░░███  ███░░███░░███░░███ ░░░███░   ░░███  ███████   ░░███ ░███ 
     ░███  ░███ ░███  ░███  ░███ ░███████  ░███ ░███   ░███     ░███ ░░░███░     ░███ ░███ 
     ░███  ░███ ░███  ░░███ ███  ░███░░░   ░███ ░███   ░███ ███ ░███   ░███      ░███ ░███ 
    █████  ████ █████  ░░█████   ░░██████  ████ █████  ░░█████  █████  █████     ░░███████ 
    ░░░░░ ░░░░ ░░░░░    ░░░░░     ░░░░░░  ░░░░ ░░░░░    ░░░░░  ░░░░░  ░░░░░       ░░░░███ 
                                                                                 ███ ░███ 
                                                                                 ░░██████  
                                                                                  ░░░░░░   """
    )
    t.sleep(4)
    username = usern()  # calling the function

    global mode

    mode = 0
    global adminlist
    adminlist = [
        "swapnil mam",
        "administrator",
        "admin",
        "a",
        "manager",
        "owner",
        "arbab",
        "saabji",
    ]
    global custlist
    custlist = ["customer", "cust", "c", "buyer", "shopper", "grihak", "khareed"]

    # Here I used mode so that I can get out of the function and then actually decide the individual file and function calling one by one,
    # so basically its use is like a flag and I used global function here so that it can be accessed wherever needed throughout the entire program
    while True:
        status = input(
            f"Okay, hello {username}, are you a customer or an administrator? "
        )

        if status.lower() in custlist:
            print(f"Welcome {username}. You are registered as a customer.")
            mode = 1
            break

        elif status.lower() in adminlist:
            print(f"Welcome {username}. You are registered as an administrator.")
            mode = 2
            break

        else:
            print("Sorry, please enter a correct role.\n")


intro()


######################################################-------Managing Roles and Executing Role-Specific Codes------#####################################################

if mode == 1:
    print("Loading your dedicated customer experience")
    for i in range(30):
        t.sleep(0.15)
        print(">", end="", flush=True)

    print("\n")
    print("Done!")

    # See readme for how and why i used flush here

    # ALL THE CODE/FILE CALL TO LOAD THE CUSTOMER FILE OF SQL WHATEVER BLABLABLA

elif mode == 2:
    print("Loading admin experience")
    for i in range(30):
        t.sleep(0.15)
        print(">", end="", flush=True)
    print("\n")
    print("Done!")

    # ALL THE CODE/FILE CALL TO LOAD ADMIN FILE OF SQL WHATEVER BLABLABLA
