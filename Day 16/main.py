# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([["pikachu", "Electric"],
                  ["Suirtle", "Water"],
                  ["Charmendar", "Fire"],])

table.align = "l"
print(table)