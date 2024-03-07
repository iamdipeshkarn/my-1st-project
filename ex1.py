print ("Hello world")
print ("Hello Again")
print ("I like typing this")
print ("Yag!printing")
print ("I'd musch rather you 'not'")
print ("I said donot touch this")
print("i will now count my chickens")
print("hens", 25+30/6)
print("Roosters",100-25*3%4)
print("now i will count the eggs")
print (3+2+1-5+4%2-1/4+6)
print("is it trur that 3+2<5-7?")
print (3+2<5-7)
print("what is 3+2<5-7")
print("what is 5-7"),5-7
print("oh,that's why it false")
print("how about Some more")
print("is it greater"),5>-2
print("is it greater or equal?"),5>=-2
print("is it less or equal?"),5<=-2

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_drivens=space_in_a_car
cars_driven = drivers
carpool_capacity = space_in_a_car
average_passangers_per_cars = passengers / cars_driven

print("there are",cars,"cars available")
print("there are Only",drivers,"drivers available")
print("there will be ",cars_not_drivens,"empty cars tpday")
print("we can transport",'passanger',"to carpool today")
print("we need to put about",'average_passengers_per_cars',"in each car")

my_name = 'zed Z. Shaw'
my_age = 35 #not a lie
my_height = 74 # inches
my_weight = 180 #1bs
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'Brown'
print("Lets talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds,heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."% (my_eyes ,my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)      


x = ("there are %d types of people." % 10)
binary = ("binary")
do_not = ("do_not")
y = ("those who know %s and those who %s." % (binary,do_not))
print(x)
print(y)
print("i said:%r."% x)
print("i also said: '%s'."% y)
hilarious = "false"
joke_evaluation = ("Isnot that joke so funny? %r")
print (joke_evaluation % hilarious)
w = ("this is the left side of...")
e = ("a string with a right side")
print(w+e)

print("Marry had a littele lamb.")
print("its fleece was white as %s."% 'snow')
print("And everywhere that Mary went.")
print("."* 10) #where'd that do?
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#watch that comma at the end. try removing it to see what happens
print (end1+end2+end3+end4+end5+end6)
print (end7+end8+end9+end10+end11+end12)


formatter = ("%r %r %r %r")
print (formatter %(1,2,3,4))
print (formatter %("one","two","three","four"))
print (formatter %("true","false","false","true"))
print (formatter %("i had this things.",
       "that you could type up right.",
       "But it didn't sing",
       "so i said goodnoght"))

#heres some new stranger stuff, remember type it exactly.
days = ("mon tue thu fri sat sun")
months = ("jan\nfeb\nmar\napr\njun\njul\naug")
print("here are the days:",days)
print("here are the months:",months)
print("""There's something going on here.",
      "with the three double-quotes.",
      "we'll be able to type as much as we like.",
      "even 4 lines if we want, or 5,or 6""")

taddy_cat = ("\ti'm tabbled in.")
persian_cat = ("i'm split\non a line.")
backlash_cat = ("i'm\\a\\cat.")
fat_cat = (""""i'll da a list:
           \*t cat food
           \*t fishes
           \*t catnip\n\t*grass
           """)
print (taddy_cat)
print (persian_cat)
print (backlash_cat)
print (fat_cat)

print("how old are you")
age = int(input("raw input()"))
print("how tall are you")
height = int(input("raw input()"))
print("how much do you weight")
weight = int(input("raw inpt()"))
print("so yoy're %r old %r tall and %r heavy." %(age,height,weight))

# prompting people
age = input("how old are you")
height = input("how tall are you?")
weight = input("how musch do you weight")
print("so you are %r old, %r tall and %r heavy."%(age,height,weight))

'''#parameter unpacking variables
from sys import argv
script, first, second, third = argv
print("the script is called:",script)
print("your first variable is:",first)
print("your second variable is",second)
print("your third variable is:",third)
'''
#prompting and passing
from sys import argv
script,user_name = argv
prompt = '>'
print = ("hi %s, i'm the %s scripts .", user_name, script)
print = ("i'd like to ask you a few question.")
print = ("do you like me %s", user_name)
likes = input(prompt)
print = ("where do you live %s",user_name)
lives = input(prompt)
print = ("what kind of computer do you have")
computer = input(prompt)

print = ("""
alright, so you said %r about liking me.
you live %r.Not sure where that is .
and you have a %r computer.nice.""",likes,lives,computer)

