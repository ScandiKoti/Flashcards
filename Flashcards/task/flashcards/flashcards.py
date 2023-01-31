def check_user_input():
    while True:
        number_of_cards = input('Input the number of cards:\n')
        try:
            number_of_cards = int(number_of_cards)
            if number_of_cards < 1:
                raise ValueError
        except (ValueError, IndexError):
            print('Invalid input!')
            continue
        break
    return number_of_cards


def main():
    number_of_cards = check_user_input()
    cards_dict = {}
    for i in range(1, number_of_cards + 1):
        term, definition = input(f'The term for card #{i}:\n'), input(f'The definition for card #{i}:\n')
        cards_dict.update({term: definition})
    for k, v in cards_dict.items():
        print('Correct!' if input(f'Print the definition of "{k}":\n') == v else f'Wrong. The right answer is "{v}"')


if __name__ == '__main__':
    main()
