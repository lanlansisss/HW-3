#QIUHE WANG
Roster1 = {
    'player 1': [],
    'player 2': [],
    'player 3': [],
    'player 4': [],
    'player 5': []
}
for n in range(5):
    jersey = int(input("Enter player %s" % (n + 1) + "'s jersey number:\n"))
    rating = int(input("Enter player %s" % (n + 1) + "'s rating:\n\n"))
    Roster1[f"player {n + 1}"] = (int(jersey), int(rating))

sorted_roster = dict(sorted(Roster1.items(), key=lambda x: x[1][0]))

userchoice = ''

print("ROSTER")
for player, (jersey, rating) in sorted_roster.items():
    print(f'Jersey number: {jersey}, Rating: {rating}')
print('')
print("MENU")
print("a - Add player")
print("d - Remove player")
print("u - Update player rating")
print("r - Output players above a rating")
print("o - Output roster")
print("q - Quit")
print('\nChoose an option:')

while userchoice != 'q':
    userchoice = str(input())

    if userchoice == 'q':
        break
    elif userchoice == 'o':
        print()
        print("ROSTER")
        for player, (jersey, rating) in sorted_roster.items():
            print(f'Jersey number: {jersey}, Rating: {rating}')
        continue
    elif userchoice == 'a':
        addjersey = str(input("Enter a jersey number:\n"))
        addrate = str(input("Enter a new rating for player:\n"))
        sorted_roster["player 6"] = (addjersey, addrate)
        sorted_roster = dict(sorted(Roster1.items(), key=lambda x: x[1][0]))
        print("ROSTER")
        for player, (jersey, rating) in sorted_roster.items():
            print(f'Jersey number: {jersey}, Rating: {rating}')
        print('')
        print("MENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        print('\nChoose an option:')

    elif userchoice == 'd':
        removejersey = int(input("Enter a jersey number:\n"))
        for player, (jersey, rating) in sorted_roster.items():
            if jersey == removejersey:
                del sorted_roster[player]
        print()
        for player, (jersey, rating) in sorted_roster.items():
            print(f'Jersey number: {jersey}, Rating: {rating}')
        print('')
        print("MENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        print('\nChoose an option:')
    elif userchoice == 'r':
        above = int(input("Enter a rating\n"))
        print(f'ABOVE {above}')
        sorted_roster = dict(sorted(Roster1.items(), key=lambda x: x[1][0]))
        for player, (jersey, rating) in sorted_roster.items():
            if rating > above:
                print(f'Jersey number: {jersey}, Rating: {rating}')
        print('')
        print("MENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        print('\nChoose an option:')
