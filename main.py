# -*- coding: utf-8 -*-
"""
Created on Thu May 14 05:07:55 2020

@author: abdil
"""

import csv
def data_store1():
    with open('expenses.csv','a',newline='')as csv_file:
        csv_writer = csv.writer(csv_file) 
#        field_names = ["Month",*all_expenses,"Total"]
#        writer = csv.DictWriter(csv_file, fieldnames = field_names)
#        writer.writeheader()
        lines = [ ["Month",*all_expenses.keys(),"Total"],
                [month,*all_expenses.values(),"$"+str(total)+"\n"]]
        for row in lines:
            max_len = len(row)
            count = 0
            for colmn in row:
                count +=1
                comma = ","
                if count == max_len:
                    comma = ""
                csv_file.write(str(colmn)+ comma)
            csv_file.write("\n")

def data_store2():
    with open('data.csv','w')as csv_file:
        file_writer = csv.writer(csv_file) 
        lines = [ ["Month: "+month,all_expenses,"Total: "+"$"+str(total)+"\n"]]
        for row in lines:
            max_len = len(row)
            count = 0
            for colmn in row:
                count +=1
                comma = ","
                if count == max_len:
                    comma = ""
                csv_file.write(str(colmn)+ comma)
            csv_file.write("\n")
def read():
    filename = "data.csv"

    with open(filename, 'r') as stream:
        reader = csv.reader(stream, delimiter=',', quotechar='"')

        for row in reader:
            print(row)
       

def display_menu():
    print("COMMAND MENU\n")
    print("read - Read all stored expenses")
    print("add -  Add a new expense")
    print("del -  Delete previous expense")
    print("updt -  Update previous expense")
    print("exit - Exit program")
    print()    
def add():
    global more,expense,amount,all_expenses,all_amounts,month,calc_expense,subtotal
    global num_of_expenses,new_expense,total
    all_expenses = {}
#    all_amounts = []
    while True:
        month = "Unkonwn"
        num_of_expenses = 0
        more= 0
        new_expense = 0
        calc_expense = 0
        subtotal = 0

        try:
            num_of_expenses = int(input("How many expenses you want to add:\t"))
            month = str(input("Month:\t"))
        except ValueError:
            print("You didn't enter a number!!!. Please try again.\n")
            break
        except Exception as e:
            print("Error: %s" %e)
            break
        for n in range(num_of_expenses):
            try:
                more+=1
                expense = str(input("Expense " + str(more)+" :\t"))
                amount = float(input("Amount " + str(more)+" :\t"))
                print()
                all_expenses[expense]= "$"+str(amount)
#                all_amounts.append(amount)
            except ValueError:
                print("You Didn't Enter a number ,Please try again.\n")
                break
            except Exception as e:
                print("Error: %s" %e)
                break
#            new_expense += expense
            calc_expense += amount
            subtotal += amount
            total = subtotal
        print("---------Info---------")    
        print("Month : " + month)
        print("Number of calculations: " +str(num_of_expenses))
        print("All Expenses: " , *all_expenses.keys())
        print("All Amounts: " , *all_expenses.values())
        print("Total = $", total)
        print()
        
        try:
            data_store2()
            data_store1()
        except IOError:  
            print("Cannot open input files.")
        except Exception as e:
            print("Error: %s" %e)
        break
        
        
    
    
        

def delete():
    pass

def update():
    pass

def main():
    
    
    while True:     
        display_menu()
        command = input("Command: ")
        if command == "read":
            read()
        elif command == "add":
            add()
        elif command == "del":
            delete()
        elif command == "updt":
            update()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
            
        
if __name__ == "__main__":
    main()