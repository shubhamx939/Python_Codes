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


def get_valid_option():
    x = input()
    x = int(x)
    while x < 1 or x > 6:
        print('Invalid option!! Please choose any among 1 to 6.')
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
    print('\t6 - Quit')

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
        sys.exit()
        break