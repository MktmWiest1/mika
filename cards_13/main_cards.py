import random
from cards_13 import compare


class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]
        self.die_or_win = [0, 1000, 0]

    def game(self):
        print('Choose Option: ')
        print('1.Draw Cards')
        print('2. Draw card only to plyer')
        print('3. Draw card only to computer')
        print('4. Russian Roulette')
        print(f'Your cards: {sum(self.player)}')
        choose = int(input('Your choice:'))
        while 1:
            compare_1 = compare.CompareCardes(player_list=self.player,
                                             computer_list=self.computer)
            if choose == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choose == 2:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choose == 3:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choose == 4:
                self.player.append(random.choice(self.die_or_win))
                self.computer.append(random.choice(self.die_or_win))
                if compare_1.compare_results():
                    break



cards_1 = BlackJack()
cards_1.game()
