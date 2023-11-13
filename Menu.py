def function_fileCreate():
    try:
        file = open("Data.txt", "r")
    except FileNotFoundError:
        file = open("Data.txt", "w+")
        textname = "NAME"
        textdate = "DATE"
        texttime = "TIME"
        textadult = "ADULTS"
        textchild = "CHILDREN"
        textsubtotal = "SUBTOTAL"
        file.write("# " +textname.ljust(20)+ "," +textdate.ljust(15)+ "," +texttime.ljust(10)+ "," +textadult.ljust(6)+ "," +textchild.ljust(8)+ " " +textsubtotal.ljust(8)+ "\n")
    file.close()

def function_menu():
    print("\n===================================")
    print("RESTAURANT RESERVATION SYSTEM")
    print("===================================")
    print("[A] View all Reservations \n[B] Make Reservation \n[C] Delete Reservation \n[D] Generate Report")
    print("[E] Exit")
    menu_choice = input("\nEnter Choice: ")
    return menu_choice