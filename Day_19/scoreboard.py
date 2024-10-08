from turtle import Turtle
FONT = ("Courier", 24, "normal")

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful
# crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If
# you get stuck, check the video walkthrough in Step 7.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-265, 265)
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT )


