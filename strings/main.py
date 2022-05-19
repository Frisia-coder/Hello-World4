# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

doelpunt_maker_0= "Ruud Gullit"
doelpunt_maker_1= "Marco van Basten"
print(doelpunt_maker_0)
print(doelpunt_maker_1)

goal_0= 32
goal_1= 54
print(goal_0)
print(goal_1)

scorers= doelpunt_maker_0 + " " + str(goal_0) + ','+" " + doelpunt_maker_1 + " " + str(goal_1)
print(scorers)

report= f"{doelpunt_maker_0} scored in the {goal_0}nd minute\n{doelpunt_maker_1} scored in the {goal_1}th minute"
print(report)

player= "Ronald Koeman"
print(player)

first_name= player[0:6]
player.find(" ")
print(first_name)

last_name_len = len(player[-player.find(' '):])
print(last_name_len)

name_short = player[:player.find(' ')].upper()[:1] + '. ' + player[-player.find(' '):]
print(name_short)

chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')])).strip()
print(chant)

good_chant = chant[-1:] != ' '
print(good_chant)























