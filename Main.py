from Amante_Therenze_Day10_Menu import *
class C_Menu:
    def __init__(self, choice):
        self.choice = choice

        if choice == "a" or choice == "A":
            count = 0
            file = open("Data.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1

            if count == 0:
                print("\nNO RESERVATIONS FOUND.")
                print()

            else:
                file = open('Data.txt', 'r')
                for each in file:
                    each = each.rstrip()
                    each = each.replace(',' , ' ')
                    print(each)

        elif choice == "b" or choice == "B":
            with open("Data.txt", "r") as file:
                for last_line in file:
                    pass
            if last_line[0] == "#":
                num = 1
            else:
                num = int(last_line[0]) + 1

            name = input("Enter Name: ")
            date = input("Enter Date: ")
            time = input("Enter Time: ")
            adults = int(input("No. of Adults: "))
            children = int(input("No. of Children: "))
            
            x = int(adults * 500)
            y = int(children * 300)
            z = float(x + y)

            file = open("Data.txt", "a")
            file.write(str(num)+ " " +name.ljust(20)+ "," +date.ljust(15)+ "," +time.ljust(10)+ "," +str(adults).ljust(6)+ "," +str(children).ljust(8)+ "," f"{z}" "\n")
            file.close()


        elif choice == "c" or choice == "C":
            resnum = input("Enter Reservation number: ")
            file_del = open("Data.txt", "r")
            lines = file_del.readlines()
            file_del.close()
            file_new = open("Data.txt", "w")
            for line in lines:
                if not line.startswith(resnum):
                    file_new.write(line)
            file_new.close()

        elif choice == "d" or choice == "D":
            file = open('Data.txt', 'r')
            next(file)
            total_adults_List = []
            total_children_List = []
            for each in file:
                each = each.rstrip()
                each = each.split(',')
                total_adults_List.append(int(each[4]))
                total_children_List.append(int(each[4]))
            sum_adults = sum(total_adults_List) * 500
            sum_children = sum(total_children_List) * 300
            grand_total = sum_adults + sum_children


            print("\n================================================================")
            print("                      GENERATING REPORTS                        ")   
            print("================================================================\n")
            file = open('Data.txt', 'r')
            for each in file:
                each = each.rstrip()
                each = each.replace(',' , ' ')
                print(each)
            print("\nTOTAL NUMBER OF ADULTS: ", sum(total_adults_List))
            print("TOTAL NUMBER OF CHILDREN: ", sum(total_children_List))
            print("GRAND TOTAL: ", float(grand_total))
            print("\n\n=====================   NOTHING FOLLOWS   ======================\n\n\n")

        elif choice == "e" or choice == "E":
            import sys
            sys.exit("\nProgram End, Thank you!\n")
        else:
            print("INVALID CHOICE, TRY AGAIN.")

while True:
    function_fileCreate()
    C_Menu(function_menu())