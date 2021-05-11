from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


scoreboard=Scoreboard()
game_is_on= True
while game_is_on:
    screen.update()
    time.sleep((0.1))
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        scoreboard.increase_score()
        snake.grow()
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        scoreboard.game_over()
    #detect collision with itself.
    for segment in snake.segments:
        if segment==snake.head or segment==snake.tail:
            pass
        else:
            if snake.head.distance(segment) < 15:
                game_is_on=False
                scoreboard.game_over()



                


screen.exitonclick()
