import random

# unicode characters:
# print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')

# ● ┌ ─ ┐ │ └ ┘

'┌─────────┐'
'│         │'
'│         │'
'│         │'
'└─────────┘'

dice_dictionary = {
    1: ('┌─────────┐',
        '│         │',
        '│    ●    │',
        '│         │',
        '└─────────┘'),
    2: ('┌─────────┐',
        '│ ●       │',
        '│         │',
        '│       ● │',
        '└─────────┘'),
    3: ('┌─────────┐',
        '│ ●       │',
        '│    ●    │',
        '│       ● │',
        '└─────────┘'),
    4: ('┌─────────┐',
        '│ ●     ● │',
        '│         │',
        '│ ●     ● │',
        '└─────────┘'),
    5: ('┌─────────┐',
        '│ ●     ● │',
        '│    ●    │',
        '│ ●     ● │',
        '└─────────┘'),
    6: ('┌─────────┐',
        '│ ●     ● │',
        '│ ●     ● │',
        '│ ●     ● │',
        '└─────────┘'),
}
dice = []
total = 0
while True:
    nr_dice = input('How many dice ? : ')

    for die in range(int(nr_dice)):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(dice_dictionary.get(die)[line], end='')
        print()

    for die in dice:
        total += die
    print(f'Total: {total}')

    play_again = input('Do you want to play again ? y (yes) or n (no) : ')
    if play_again.lower() == 'y':
        dice = []
        total = 0
        continue
    else:
        break
