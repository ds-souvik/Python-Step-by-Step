"""This is a python mini project- Health Management System.
This app maintains the food habits and exercises performed by 3 people-Souvik, Atanu and Abhijit
along with time-stamp.
You can either add their activities or retrieve their activities till now as per your requirement.
It involves: dynamic programming, functions, while loop, for loop, if elif else conditional statement
and an app building mindset development methodology."""

print("**********************************************************************************************")
print("*****************************HEALTH MANAGEMENT SYSTEM*****************************************")
print("**********************************************************************************************")

def func_action():
    print("Hello. Please select your action.")
    print("For locking action     : Press 1")
    print("For retrieving data    : Press 2")

def func_name():
    print("For whom do you want to perform the action?")
    print("For Souvik  : Press 1")
    print("For Atanu   : Press 2")
    print("For Abhijit : Press 3")

def func_lock_what():
    print("What do you want to lock?")
    print("For locking meals     : Press 1")
    print("For locking exercise  : Press 2")

def func_retrieve_what():
    print("What do you want to retrieving?")
    print("For retrieving meals     : Press 1")
    print("For retrieving exercise  : Press 2")

def getdate():
    import datetime
    return datetime.datetime.now()

flag="Y"
while(flag=="Y"):
    func_action()
    action = input()
    if action=="1":
        func_name()
        name = input()
        if name=="1":
            func_lock_what()
            lock_what = input()
            if lock_what=="1":
                f = open("21A Souvik_food.txt", "a")
                print("What did you eat?")
                food=input()
                a=str(getdate())+""+food
                f.write(a+"\n")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag=input()
                if(flag=="Y" or flag=="N"):
                    continue
                else:
                    print("Invalid option.")
            elif lock_what=="2":
                f = open("21A Souvik_exercise.txt", "a")
                print("What exercise did you do?")
                exercise = input()
                a=str(getdate())+""+exercise
                f.write(a+"\n")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag = input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")
            else:
                print("Invalid locking option. Do you want to continue any other action?(Y/N)")
                flag= input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

        elif name=="2":
            func_lock_what()
            lock_what = input()
            if lock_what=="1":
                f = open("21A Atanu_food.txt", "a")
                print("What did you eat?")
                food=input()
                a = str(getdate()) + "" + food
                f.write(a+"\n")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag=input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            elif lock_what=="2":
                f = open("21A Atanu_exercise.txt", "a")
                print("What exercise did you do?")
                exercise = input()
                a = str(getdate()) + "" + exercise
                f.write(a+"\n")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag = input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            else:
                print("Invalid locking option. Do you want to continue any other action?(Y/N)")
                flag= input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

        elif name=="3":
            func_lock_what()
            lock_what = input()
            if lock_what=="1":
                f = open("21A Abhijit_food.txt", "a")
                print("What did you eat?")
                food=input()
                a = str(getdate()) + "" + food
                f.write(a+"\n")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag=input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            elif lock_what=="2":
                f = open("21A Abhijit_exercise.txt", "a")
                print("What exercise did you do?")
                exercise = input()
                a = str(getdate()) + "" + exercise
                f.write(a+"\n")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag = input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            else:
                print("Invalid locking option. Do you want to continue any other action?(Y/N)")
                flag= input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

        else:
            print("Invalid person option. Do you want to continue any other action?(Y/N)")
            flag = input()
            if (flag == "Y" or flag == "N"):
                continue
            else:
                print("Invalid option.")



    elif action=="2":
        func_name()
        name=input()
        if name=="1":
            func_retrieve_what()
            retrieve_what=input()
            if retrieve_what=="1":
                f = open("21A Souvik_food.txt", "r")
                for line in f:
                    print(line,end="")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag=input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            elif retrieve_what=="2":
                f = open("21A Souvik_exercise.txt", "r")
                for line in f:
                    print(line, end="")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag = input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            else:
                print("Invalid retrieving option. Do you want to continue any other action?(Y/N)")
                flag= input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

        elif name=="2":
            func_retrieve_what()
            retrieve_what=input()
            if retrieve_what=="1":
                f = open("21A Atanu_food.txt", "r")
                for line in f:
                    print(line,end="")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag=input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            elif retrieve_what=="2":
                f = open("21A Atanu_exercise.txt", "r")
                for line in f:
                    print(line, end="")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag = input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            else:
                print("Invalid retrieving option. Do you want to continue any other action?(Y/N)")
                flag= input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

        elif name=="3":
            func_retrieve_what()
            retrieve_what=input()
            if retrieve_what=="1":
                f = open("21A Abhijit_food.txt", "r")
                for line in f:
                    print(line,end="")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag=input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            elif retrieve_what=="2":
                f = open("21A Abhijit_exercise.txt", "r")
                for line in f:
                    print(line, end="")
                f.close()
                print("Do you want to continue any other action?(Y/N)")
                flag = input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

            else:
                print("Invalid retrieving option. Do you want to continue any other action?(Y/N)")
                flag= input()
                if (flag == "Y" or flag == "N"):
                    continue
                else:
                    print("Invalid option.")

        else:
            print("Invalid person option. Do you want to continue any other action?(Y/N)")
            flag = input()
            if (flag == "Y" or flag == "N"):
                continue
            else:
                print("Invalid option.")

    else:
        print("Invalid action. Do you want to try again?(Y/N)")
        flag=input()
        if (flag == "Y" or flag == "N"):
            continue
        else:
            print("Invalid option.")

print("Thanks for using our Health Management System. Take care!!")