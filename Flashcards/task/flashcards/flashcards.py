import json
import random
import io


class FlashCards:
    def __init__(self):
        self.number_of_cards = 0
        self.cards_dict = {}
        self.errors_list = []
        self.memory_file = io.StringIO()
        self.counter = 0

    def game_menu(self):
        while True:
            choice = self.user_input('Input the action (add, remove, import, export, ask, exit, log, hardest card, '
                                     'reset stats):\n')
            if choice == 'add':
                self.add_card()
            elif choice == 'remove':
                self.remove_card()
            elif choice == 'import':
                self.import_cards()
            elif choice == 'export':
                self.export_cards()
            elif choice == 'ask':
                self.check_user_input()
                self.check_answer()
            elif choice == 'exit':
                break
            elif choice == "log":
                self.user_log()
            elif choice == "hardest card":
                self.count_mistakes()
            elif choice == "reset stats":
                self.clear_mistakes()

    def add_card(self):
        term = input(f'The card:\n')
        while True:
            for k in self.cards_dict:
                if term == k:
                    term = self.user_input(f'The term "{term}" already exists. Try again:\n')
                    continue
            break
        definition = self.user_input(f'The definition for card:\n')
        while True:
            for v in self.cards_dict.values():
                if definition == v["user_def"]:
                    definition = self.user_input(f'The definition "{definition}" already exists. Try again:\n')
                    continue
            break
        self.user_output(f'The pair ("{term}":"{definition}") has been added.')
        self.cards_dict.update({term: {"user_def": definition, "errors_num": 0}})

    def remove_card(self):
        term = self.user_input(f'Which card?:\n')
        try:
            self.cards_dict.pop(term)
            self.user_output('The card has been removed.')
        except KeyError:
            self.user_output(f'Can\'t remove "{term}": there is no such card.')

    def import_cards(self):
        file_name = self.user_input('File name:\n')
        try:
            with open(file_name, 'r') as json_file:
                cards_dict_json = json.load(json_file)
                self.cards_dict.update(cards_dict_json)
                self.user_output(f'{len(cards_dict_json)} cards have been loaded.')
        except FileNotFoundError:
            self.user_output('File not found.')

    def export_cards(self):
        file_name = self.user_input('File name:\n')
        with open(file_name, 'w') as json_file:
            json.dump(self.cards_dict, json_file)
            self.user_output(f'{len(self.cards_dict)} cards have been saved.')

    def check_user_input(self):
        while True:
            try:
                self.number_of_cards = int(self.user_input('How many times to ask?\n'))
                if self.number_of_cards < 1:
                    raise ValueError
            except (ValueError, IndexError):
                self.user_output('Invalid input!')
                continue
            break

    def check_answer(self):
        for i in range(self.number_of_cards):
            term = random.choice(list(self.cards_dict.keys()))
            answer = self.user_input(f'Print the definition of "{term}":\n')
            if answer == self.cards_dict[term]["user_def"]:
                self.user_output('Correct!')
            else:
                message = f'Wrong. The right answer is "{self.cards_dict[term]["user_def"]}".'
                self.cards_dict[term]["errors_num"] += 1
                for k, v in self.cards_dict.items():
                    if answer == v["user_def"]:
                        message = f'Wrong. The right answer is "{self.cards_dict[term]["user_def"]}", ' \
                                  f'but your definition is correct for "{k}".'
                        break
                self.user_output(message)

    def user_log(self):
        log_file = self.user_input("File name:\n")
        with open(log_file, "w") as log:
            lines = self.memory_file.getvalue().split('\n')
            for line in lines:
                log.write(line)
        self.user_output("The log has been saved.")

    def user_output(self, msg):
        self.memory_file.write(msg)
        print(msg)

    def user_input(self, msg):
        obj = input(msg)
        self.memory_file.write(msg + obj)
        return obj

    def count_mistakes(self):
        for k, v in self.cards_dict.items():
            if v["errors_num"] > self.counter:
                self.counter = v["errors_num"]
                self.errors_list = [k]
            elif v["errors_num"] == self.counter and self.counter > 0:
                self.errors_list.append(k)
        self.counter = 0
        if len(self.errors_list) == 1:
            self.user_output(f'The hardest card is "{"".join(self.errors_list)}". You have '
                             f'{self.cards_dict["".join(self.errors_list)]["errors_num"]} errors answering it.')
        elif len(self.errors_list) > 1:
            self.user_output('The hardest cards are "{}". You have {} errors answering it'.format
                             ('", "'.join(self.errors_list), self.cards_dict["".join(self.errors_list)]["errors_num"]))
        else:
            self.user_output("There are no cards with errors.")

    def clear_mistakes(self):
        for v in self.cards_dict.values():
            v["errors_num"] = 0
        self.errors_list = []
        self.user_output("Card statistics have been reset.")


def main():
    game = FlashCards()
    game.game_menu()
    print('Bye bye!')


if __name__ == '__main__':
    main()
