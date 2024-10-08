import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck,
    # check the video walkthrough in Step 5.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this
    # happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating
    # an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough
    # in Step 6.
    if player.ycor() > 280:
        player.return_turtle()

        car_manager.increase_car_speed()

        # Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a
        # successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed
        # in the centre. If you get stuck, check the video walkthrough in Step 7.
        scoreboard.increase_level()

screen.exitonclick()
