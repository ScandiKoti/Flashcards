import json
import random


class FlashCards:
    def __init__(self):
        self.number_of_cards = 0
        self.cards_dict = {}

    def game_menu(self):
        while True:
            user_choice = input('Input the action (add, remove, import, export, ask, exit):\n')
            if user_choice == 'add':
                self.add_card()
            elif user_choice == 'remove':
                self.remove_card()
            elif user_choice == 'import':
                self.import_cards()
            elif user_choice == 'export':
                self.export_cards()
            elif user_choice == 'ask':
                self.check_user_input()
                self.check_answer()
            elif user_choice == 'exit':
                break

    def add_card(self):
        # for i in range(1, self.number_of_cards + 1):
        term = input(f'The card:\n')
        while True:
            for k in self.cards_dict:
                if term == k:
                    term = input(f'The term "{term}" already exists. Try again:\n')
                    continue
            break
        definition = input(f'The definition for card:\n')
        while True:
            for v in self.cards_dict.values():
                if definition == v:
                    definition = input(f'The definition "{definition}" already exists. Try again:\n')
                    continue
            break
        print(f'The pair ("{term}":"{definition}") has been added.')
        self.cards_dict[term] = definition

    def remove_card(self):
        term = input(f'Which card?:\n')
        try:
            self.cards_dict.pop(term)
            print('The card has been removed.')
        except KeyError:
            print(f'Can\'t remove "{term}": there is no such card.')

    def import_cards(self):
        file_name = input('File name:\n')
        try:
            with open(file_name, 'r') as json_file:
                cards_dict_json = json.load(json_file)
                self.cards_dict.update(cards_dict_json)
                print(f'{len(cards_dict_json)} cards have been loaded.')
        except FileNotFoundError:
            print('File not found.')

    def export_cards(self):
        file_name = input('File name:\n')
        with open(file_name, 'w') as json_file:
            json.dump(self.cards_dict, json_file)
            print(f'{len(self.cards_dict)} cards have been saved.')

    def check_user_input(self):
        while True:
            try:
                self.number_of_cards = int(input('How many times to ask?\n'))
                if self.number_of_cards < 1:
                    raise ValueError
            except (ValueError, IndexError):
                print('Invalid input!')
                continue
            break

    def check_answer(self):
        for i in range(self.number_of_cards):
            term = random.choice(list(self.cards_dict.keys()))
            answer = input(f'Print the definition of "{term}":\n')
            if answer == self.cards_dict[term]:
                print('Correct!')
            else:
                message = f'Wrong. The right answer is "{self.cards_dict[term]}".'
                for k, v in self.cards_dict.items():
                    if answer == v:
                        message = f'Wrong. The right answer is "{self.cards_dict[term]}", but your definition is ' \
                                  f'correct for "{k}".'
                        break
                print(message)


def main():
    game = FlashCards()
    game.game_menu()
    print('Bye bye!')


if __name__ == '__main__':
    main()
