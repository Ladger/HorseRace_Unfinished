
import time
import sqlite3

class Horse():
    def __init__(self,name,age,rep,cond,wins,loses,odd,effect):
        self.name = name
        self.age = age
        self.rep = rep
        self.cond = cond
        self.wins = wins
        self.loses = loses
        self.odd = odd
        self.effect = effect
    
    def __str__(self):
        return "Name: {}\nAge: {}\nReputation: {}\nCondition: {}\nWins: {}\nLoses: {}".format(self.name,self.age,self.rep,self.cond,self.wins,self.loses)

class Stable():
    def __init__(self):
        self.connect()
    
    def connect(self):
        self.con = sqlite3.connect("stable.db")
        self.cursor = self.con.cursor()
        
        statement = "CREATE TABLE IF NOT EXISTS horses (Name TEXT,Age INT,Reputation INT,Condition INT,Wins INT,Loses INT,odd FLOAT,Effect INT)"
        self.cursor.execute(statement)
        self.con.commit()

    def disconnect(self):
        self.con.close()

    def add_horse(self,horse):
        statement = "INSERT INTO horses VALUES (?,?,?,?,?,?,?,?)"
        self.cursor.execute(statement,(horse.name,horse.age,horse.rep,horse.cond,horse.wins,horse.loses,horse.odd,horse.effect))
        self.con.commit()

    def horse_list(self):
        statement = "SELECT * FROM horses"
        self.cursor.execute(statement)
        horses = self.cursor.fetchall()
        for i in horses:
            horse = Horse(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
            print(horse)
            time.sleep(1)
            print("*******************")

    def show_odds(self):
        statement = "SELECT * FROM horses"
        self.cursor.execute(statement)
        horse_list = self.cursor.fetchall()

        temp_number = 1
        for i in horse_list:
            print("[{}]{} x{}".format(temp_number,i[0],i[6]))
            temp_number += 1

    def increase_age(self,horse_name):
        statement1 = "UPDATE horses SET Age = ? where Name = ?"
        statement2 = "SELECT Age FROM horses where Name = ?"
        
        self.cursor.execute(statement2,(horse_name,))
        age_list = self.cursor.fetchall()
        age = age_list[0][0]
        age += 1

        self.cursor.execute(statement1,(age,horse_name,))
        self.con.commit()

    def increase_rep(self,horse_name,amount):
        statement1 = "UPDATE horses SET Reputation = ? where Name = ?"
        statement2 = "SELECT Reputation FROM horses where Name = ?"

        self.cursor.execute(statement2,(horse_name,))
        rep_list = self.cursor.fetchall()
        rep = rep_list[0][0]
        rep += amount

        self.cursor.execute(statement1,(amount,horse_name,))
        self.con.commit()
    
    def decrease_cond(self,horse_name,amount):
        statement1 = "UPDATE horses SET Condition = ? where Name = ?"
        statement2 = "SELECT Condition FROM horses where Name = ?"

        self.cursor.execute(statement2,(horse_name,))
        cond_list = self.cursor.fetchall()
        cond = cond_list[0][0]
        cond -= amount

        self.cursor.execute(statement1,(cond,horse_name,))
        self.con.commit()

    def increase_win(self,horse_name):
        statement1 = "UPDATE horses SET Wins = ? where Name = ?"
        statement2 = "SELECT Wins FROM horses where Name = ?"
        
        self.cursor.execute(statement2,(horse_name,))
        win_list = self.cursor.fetchall()
        wins = win_list[0][0]
        wins += 1

        self.cursor.execute(statement1,(wins,horse_name,))
        self.con.commit()
    
    def increase_lose(self,horse_name):
        statement1 = "UPDATE horses SET Loses = ? where Name = ?"
        statement2 = "SELECT Loses FROM horses where Name = ?"
        
        self.cursor.execute(statement2,(horse_name,))
        lose_list = self.cursor.fetchall()
        loses = lose_list[0][0]
        loses += 1

        self.cursor.execute(statement1,(loses,horse_name,))
        self.con.commit()
    
    def reset_db(self):
        statement1 = "SELECT * FROM horses"
        statement2 = "UPDATE horses SET Reputation = 0 where Name = ?"
        statement3 = "UPDATE horses SET Condition = 100 where Name = ?"
        statement4 = "UPDATE horses SET Wins = 0 where Name = ?"
        statement5 = "UPDATE horses SET Loses = 0 where Name = ?"
        
        self.cursor.execute(statement1)
        horse_list = self.cursor.fetchall()

        for i in horse_list:
            self.cursor.execute(statement2,(i[0],))
            self.cursor.execute(statement3,(i[0],))
            self.cursor.execute(statement4,(i[0],))
            self.cursor.execute(statement5,(i[0],))
        
        self.con.commit()
    
    def calculate_odds(self):
        statement = "SELECT * FROM horses"
        statement2 = "UPDATE horses SET odd = ? where Name = ?"
        self.cursor.execute(statement)
        horse_list = self.cursor.fetchall()

        overall_popularity = 0
        for i in horse_list:
            overall_popularity += (i[2] * 10) + (i[4] * 15) - (i[5] * 5)

        for i in horse_list:
            if ((i[2] * 10) + (i[4] * 15) - (i[5] * 5) == 0):
                horse_odd = 1.5
            else:
                horse_odd = overall_popularity / ((i[2] * 10) + (i[4] * 15) - (i[5] * 5))
        
            self.cursor.execute(statement2,(horse_odd,i[0]))
            self.con.commit()

    def calculate_effect(self):
        statement = "SELECT * FROM horses"
        statement2 = "UPDATE horses SET Effect = ? where Name = ?"
        self.cursor.execute(statement)
        horse_list = self.cursor.fetchall()

        for i in horse_list:
            total_effect = 0
            if (i[3] > 90):
                total_effect += 4
            elif (i[3] > 80):
                total_effect += 3
            elif (i[3] > 70):
                total_effect += 2
            elif (i[3] > 60):
                total_effect += 1
            elif (i[3] > 50):
                total_effect += 0
            elif (i[3] > 40):
                total_effect -= 1
            elif (i[3] > 30):
                total_effect -= 2
            elif (i[3] > 20):
                total_effect -= 3
            elif (i[3] > 10):
                total_effect -= 4
            else:
                total_effect -= 5
            
            if(i[1] > 30):
                total_effect -= 2
            elif (i[1] > 20):
                total_effect -= 1
            elif (i[1] > 10):
                total_effect += 1

            self.cursor.execute(statement2,(total_effect,i[0]))
            self.con.commit()


Stable().disconnect()