import time
import turtle
import horse_database
import turtle_program
import sqlite3

con = sqlite3.connect("stable.db")
cursor = con.cursor()
money = 2000

while True:
    print("""
    *******************************
    Welcome to horse race program!
    *******************************
    [1]Start Race
    [2]Show Current Bets
    [3]Show Horses
    [4]Exit
    *******************************
    """)
    inp1 = input("Please enter correct number:")

    if (inp1 == "1"):
        statement = "SELEECT * FROM horses"
        cursor.execute(statement)
        horses = cursor.fetchall()
        
        while True:
            print("""
            ****************************
            Please choose horse to bet.
            ****************************
            [1]Altay x{}
            [2]Koptagel x{}
            [3]Berhan x{}
            [4]Horsea x{}
            [5]Düldül x{}
            [6]Dıgıdık x{}
            ****************************
            Your money: {}
            ****************************
            """.format(horses[0][6],horses[1][6],horses[2][6],horses[3][6],horses[4][6],horses[5][6],money))
            
            inp2 = input("Please enter number:")
            try:    
                inp3 = int(input("Please enter your bet amount:"))
                money -= inp3
            except ValueError:
                print("Wrong entry...")
                time.sleep(1)
                break
            
            result = turtle_program.Setup().race()
            if (result == "1"):
                wining_odd = horses[0][6]
            elif (result == "2"):
                wining_odd = horses[1][6]
            elif (result == "3"):
                wining_odd = horses[2][6]
            elif (result == "4"):
                wining_odd = horses[3][6]
            elif (result == "5"):
                wining_odd = horses[4][6]
            elif (result == "6"):
                wining_odd = horses[5][6]

            if (inp2 == result):
                money += wining_odd * inp3
            
            #I need to change all stats of horses here
            #adding win or lose, decreasing cond and increasing rep, changing odd and calculating effect

    elif (inp1 == "2"):
        horse_database.Stable().show_odds()
    elif (inp1 == "3"):
        horse_database.Stable().horse_list()
    elif (inp1 == "4"):
        print("Exitting from program...")
        time.sleep(2)
        break
    else:
        print("No operation for this number, please check your input again:")

con.close()