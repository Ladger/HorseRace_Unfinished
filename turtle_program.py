
import random
import turtle


class Horse():
    
    
    def create_horse(self,color,startx,starty):
        horse = turtle.Turtle()
        horse.shapesize(1,1,5)
        horse.color(color)
        horse.shape('turtle')
        horse.speed(0)
        horse.penup()
        horse.goto(startx,starty)
        horse.pendown()
        return horse

class Setup():
    def __init__(self):
        self.start()
    
    def start(self):
        pen = turtle.Turtle()
        screen = turtle.Screen()

        screen.bgcolor('light green')
        screen.setup(1.0,1.0)
        screen.title("Atatürk Hipodromu")

        pen.speed(0)
        pen.up()
        pen.goto(-250,180)
        pen.down()

        for i in (range(1,8)):
           pen.forward(500)
           pen.up()
           pen.back(500)
           pen.setheading(270)
           pen.forward(60)
           pen.setheading(0)
           pen.down()
           if (i == 7):
            break
           pen.write(i,font=('Arial',20))
        pen.hideturtle()

        writing = turtle.Turtle()
        writing.speed(0)

    
        self.h1 = Horse().create_horse('red',-250,150)
        writing.penup()
        writing.color("red")
        writing.goto(-300,150)
        writing.pendown()
        writing.write('Altay',font=('Arial',15))

        self.h2 = Horse().create_horse('blue',-250,90)
        writing.penup()
        writing.color("blue")
        writing.goto(-300,90)
        writing.pendown()
        writing.write('Koptagel',font=('Arial',15))

        self.h3 = Horse().create_horse('orange',-250,30)
        writing.penup()
        writing.color("orange")
        writing.goto(-300,30)
        writing.pendown()
        writing.write('Berhan',font=('Arial',15))

        self.h4 = Horse().create_horse('green',-250,-30)
        writing.penup()
        writing.color("green")
        writing.goto(-300,-30)
        writing.pendown()
        writing.write('Horsea',font=('Arial',15))

        self.h5 = Horse().create_horse('yellow',-250,-90)
        writing.penup()
        writing.color("yellow")
        writing.goto(-300,-90)
        writing.pendown()
        writing.write('Düldül',font=('Arial',15))

        self.h6 = Horse().create_horse('purple',-250,-150)
        writing.penup()
        writing.color("purple")
        writing.goto(-300,-150)
        writing.pendown()
        writing.write('Dıgıdık',font=('Arial',15))
        writing.hideturtle()
    
    def race(self):
        self.h1_win = False
        self.h2_win = False
        self.h3_win = False
        self.h4_win = False
        self.h5_win = False
        self.h6_win = False
        
        while True:
            self.h1.forward(random.randint(3,8))

            if (self.h1.pos()[0] >= 250):
                self.h1.write(' Altay WON!',font=('Arial',30))
                self.h1_win = True
                break   

            self.h2.forward(random.randint(3,8))
            if (self.h2.pos()[0] >= 250):
                self.h2.write(' Koptagel WON!',font=('Arial',30))
                self.h2_win = True
                break

            self.h3.forward(random.randint(3,8))
            if (self.h3.pos()[0] >= 250):
                self.h3.write(' Berhan WON!',font=('Arial',30))
                self.h3_win = True
                break

            self.h4.forward(random.randint(3,8))
            if (self.h4.pos()[0] >= 250):
                self.h4.write(' Horsea WON!',font=('Arial',30))
                self.h4_win = True
                break

            self.h5.forward(random.randint(3,8))
            if (self.h5.pos()[0] >= 250):
                self.h5.write(' Düldül WON!',font=('Arial',30))
                self.h5_win = True
                break

            self.h6.forward(random.randint(3,8))
            if (self.h6.pos()[0] >= 250):
                self.h6.write(' Dıgıdık WON!',font=('Arial',30))
                self.h6_win = True
                break
        
        turtle.done()
        if (self.h1_win):
            return "1"
        elif (self.h2_win):
            return "2"
        elif (self.h3_win):
            return "3"
        elif (self.h4_win):
            return "4"
        elif (self.h5_win):
            return "5"
        elif (self.h6_win):
            return "6"