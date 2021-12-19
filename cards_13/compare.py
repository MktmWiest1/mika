class CompareCardes:
    def __init__(self, player_list, computer_list):
        self.player_list = player_list
        self.computer_list = computer_list

    def compare_results(self):
        if sum(self.player_list) > 20 and sum( self.computer_list) < 20:
            print(f'Our cards: {sum(self.player_list)} Computer Wins! Computer results {sum(self.computer_list)}')
            return True
        elif sum(self.player_list) < 20 and sum(self.computer_list) > 20:
            print(f'Our cards: {(self.player_list)} Computer Wins! Conratgs! Computer results {sum(self.computer_list)}')
            return True
        elif sum(self.player_list) > 20 and sum(self.computer_list) > 20:
            print(f'Our cards: {sum(self.player_list)}Draw! No winners! Computer results: {sum(self.computer_list)}')
            return True

