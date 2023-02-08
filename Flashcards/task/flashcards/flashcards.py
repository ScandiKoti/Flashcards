class FlashCards:
    def __init__(self):
        self.number_of_cards = 0
        self.cards_dict = {}

    def check_user_input(self):
        while True:
            try:
                self.number_of_cards = int(input('Input the number of cards:\n'))
                if self.number_of_cards < 1:
                    raise ValueError
            except (ValueError, IndexError):
                print('Invalid input!')
                continue
            break

    def add_card(self):
        for i in range(1, self.number_of_cards + 1):
            term = input(f'The term for card #{i}:\n')
            while True:
                for k in self.cards_dict:
                    if term == k:
                        term = input(f'The term "{term}" already exists. Try again:\n')
                        continue
                break
            definition = input(f'The definition for card #{i}:\n')
            while True:
                for v in self.cards_dict.values():
                    if definition == v:
                        definition = input(f'The definition "{definition}" already exists. Try again:\n')
                        continue
                break
            self.cards_dict[term] = definition

    def check_answer(self):
        for k, v in self.cards_dict.items():
            answer = input(f'Print the definition of "{k}":\n')
            if answer == v:
                print('Correct!')
            else:
                message = f'Wrong. The right answer is "{v}".'
                for term, definition in self.cards_dict.items():
                    if answer == definition:
                        message = f'Wrong. The right answer is "{v}", but your definition is correct for "{term}".'
                        break
                print(message)


def main():
    game = FlashCards()
    game.check_user_input()
    game.add_card()
    game.check_answer()


if __name__ == '__main__':
    main()
