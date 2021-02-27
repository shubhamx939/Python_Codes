import csv
import statistics
import sys


def load_data():
    
    try:
        filename = input("Enter the File Name \n")
        filename = filename + ".csv"
        fptr = open(filename,"r")
        read_head = csv.reader(fptr)
        data = list(read_head)
        
        for i in data:
            value_list = []
            key = i[0]
            value = i[1:]
            
            for j in value:
                elem = int(j)
                value_list.append(elem)
                data_dict[key] = value_list        

        print("Data is Loaded ! \n")
        
        
    except Exception as e:
        print(e)
        
        choice = input("Do you want to enter Filename again : Y/N \n")
        
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return
    
    return


def display_data():
    
    if(len(data_dict) != 0):
        for key,value in data_dict.items():
            print(key)
            print("-" * len(key))
            
            for i in value:
                print(i, end = " ")
            print("\n")    
  
    else:
        print("Data is not Loaded ! \n")
        choice = input("Do you want to Load the Data: Y/N \n")
        
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return
    
    return


def rename_set():
    
    if(len(data_dict) != 0):
        print("which set do you want to rename?")
        counter = 1
        key_list = []
        
        for key in data_dict:
            set_name = str(counter) + "-" + key
            counter = counter+1
            key_list.append(key)
            print(" ",set_name)
            
        while True:
            choice = int(input("Enter ur choice "))
            if(choice>0 and choice<=len(key_list)):
                while True:
                    rename = input("Enter the Name ")
                    if(rename == ""):
                        print("Name cannot be blank")
                    elif(rename in data_dict):
                        print("Name must be unique")
                    else:
                        index = choice-1
                        index1 = key_list[index]
                        data_dict[rename] = data_dict.pop(index1)
                        print(index1,"renamed to",rename)
                        break
                break
            
            else:
                print("You entered invalid choice ! \n")
                continue
            
    else:
        print("Data is not Loaded ! \n")
        choice = input("Do you want to Load the Data: Y/N \n")
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return

    return


def sort_set():
    
    if(len(data_dict) != 0):
        print("which set do you want to Sort?")
        counter = 1
        key_list = []
        
        for key in data_dict:
            set_name = str(counter) + "-" + key
            counter = counter+1
            key_list.append(key)
            print(" ",set_name)
        
        while True:
            choice = int(input("Enter ur choice "))
            if(choice>0 and choice<=len(key_list)):
                index = choice-1
                index1 = key_list[index]
                values = data_dict[index1]
                data_dict[index1] = sorted(values)
                print("Set Sorted ! \n")
                break
          
            else:
                print("You entered invalid choice ! \n")
                continue
            
    else:
        print("Data is not Loaded ! \n")
        choice = input("Do you want to Load the Data: Y/N \n")
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return

    return


def analyze_set():
    
    if(len(data_dict) != 0):
        
        print("\nWhich set do you want to Analyze?")
        counter = 1
        key_list = []
        
        for key in data_dict:
            set_name = str(counter) + "-" + key
            counter = counter+1
            key_list.append(key)
            print(" ",set_name)
        
        choice = int(input("Enter ur choice "))
        
        if(choice>0 and choice<=len(key_list)):
            index = choice-1
            index1 = key_list[index]
            values = data_dict[index1]
            print(index1)
            print(len(index1)*"-")
            print("Number of values (n):",len(values))
            print("\t\t\tMaximum :",max(values))
            print("\t\t\tMinimum :",min(values))
            print("\t\t\t   Mean : {:.2f}".format(sum(values)/len(values)))
            print("\t\t\t Median : {:.2f}".format(statistics.median(values)))
            print("\t\t\t   Mode :" ,statistics.mode(values))
            print(" Standard deviation : {:.2f}".format(statistics.stdev(values)))
            
        else:
            print("You entered invalid choice ! \n")
            analyze_set()
    
    else:
        print("Data is not Loaded ! \n")
        choice = input("Do you want to Load the Data: Y/N \n")
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return

    return

def save_data():
    print("Save data")
    return

def compare_sets():
    
    if(len(data_dict) != 0):
        print("\nWhich set do you want to compare first?")
        counter = 1
        key_list = []
        
        for key in data_dict:
            set_name = str(counter) + "-" + key
            counter = counter+1
            key_list.append(key)
            print(" ",set_name)
        
        choice1 = int(input("Enter ur choice "))
        
        print("\nWhich set do you want to compare first?")
        counter = 1
        key_list = []
        
        for key in data_dict:
            set_name = str(counter) + "-" + key
            counter = counter+1
            key_list.append(key)
            print(" ",set_name)
            
        choice2 = int(input("Enter ur choice "))
        
        if(choice1 > 0 and choice1 <= len(key_list)):
            if(choice2 > 0 and choice2 <= len(key_list)):
                if(choice1 != choice2):
                    index1 = choice1 - 1
                    index2 = choice2 - 1
                    index11 = key_list[index1]
                    index22 = key_list[index2]
                    values1 = data_dict[index11]
                    values2 = data_dict[index22]
                    
                    print("\t\t\t\t\t", index11,"\t",index22)
                    print("\t\t\t\t\t",len(index11)*"-","\t",len(index22)*"-")
                    print("Number of values (n):",len(values1),"\t\t\t\t\t\t",len(values2))
                    print("\t\t\tMaximum :",max(values1),"\t\t\t\t\t\t", max(values2))
                    print("\t\t\tMinimum :",min(values1),"\t\t\t\t\t\t", min(values2))
                    print("\t\t\t   Mean : {:.2f} \t\t\t\t\t {:.2f}".format(sum(values1)/len(values1), sum(values2)/len(values2)))
                    print("\t\t\t Median : {:.2f} \t\t\t\t\t {:.2f}".format(statistics.median(values1), statistics.median(values2)))
                    print("\t\t\t   Mode :" ,statistics.mode(values1),"\t\t\t\t\t\t", statistics.mode(values2))
                    print(" Standard deviation : {:.2f} \t\t\t\t\t\t {:.2f}".format(statistics.stdev(values1), statistics.stdev(values2)))
                
                else:
                    print("There's no point comparing a set to itself !")
        else:
            print("Invalid choice")   
          
   
    else:
        print("Data is not Loaded ! \n")
        choice = input("Do you want to Load the Data: Y/N \n")
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return

    return

def edit_set():
    if(len(data_dict) != 0):
        print("which set do you want to Sort?\n")
        counter = 1
        key_list = []
        
        for key in data_dict:
            set_name = str(counter) + "-" + key
            counter = counter+1
            key_list.append(key)
            print(" ",set_name)
        
        choice = input("Enter ur choice\n")
        
        print("You are editing {}".format(key_list[choice]))
        
        print("(I)nsert a value")
        print("(M)odify a value")
        print("(D)elete a value")
        print("(F)inished editing")
        
        edit_choice = input()
        
        if(edit_choice == "i" or edit_choice == "I"):
            print()
            
        elif(edit_choice == "m" or edit_choice == "M"):
            print()
            
        elif(edit_choice == "d" or edit_choice == "D"):
            print()
        
        elif(edit_choice == "f" or edit_choice == "F"):
            print()
            
            
    else:
        print("Data is not Loaded ! \n")
        choice = input("Do you want to Load the Data: Y/N \n")
        if(choice == "Y" or choice == "y"):
            load_data()
        elif(choice == "N" or choice == "n"):
            return

    return


def get_valid_option():
    x = input()
    x = int(x)
    while x < 1 or x > 9:
        print('Invalid option!! Please choose any among 1 to 9.')
        x = input()
        x = int(x)

    return x


print('Welcome to The Smart Statistician!')
print('\t Programmed by Shubham')

data_dict = {}

while True:
    print('\nPlease choose from the following options:')
    print('\t1 - Load data from a file')
    print('\t2 - Display the data to the screen')
    print('\t3 - Rename a set')
    print('\t4 - Sort a set')
    print('\t5 - Analyze a set')
    print('\t6 - Save data to a file')
    print('\t7 - Compare two sets')
    print('\t8 - Edit a set')
    print('\t9 - Quit')

    option = get_valid_option()

    if option == 1:
        load_data()
    elif option == 2:
        display_data()
    elif option == 3:
        rename_set()
    elif option == 4:
        sort_set()
    elif option == 5:
        analyze_set()
    elif option == 6:
        save_data()
    elif option == 7:
        compare_sets()
    elif option == 8:
        edit_set()
    elif option == 9:
        sys.exit()
        break