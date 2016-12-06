# Homework - 4

players = int(input('Input number players in tennis tournament'))
print()
dict_1 = {}
counter = 0

if players >= 16:
    print('your tournament is big')

elif players < 16:
    print('your tournament is small')

for i in range(players):
    print('input name of player')
    player = input()
    dict_1['player_' + str(i+1)] = str(player)

print('Your list of players')
while counter != players:
    print(dict_1['player_' + str(counter+1)])
    counter += 1
