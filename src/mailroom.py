# -*- coding: utf -8 -*-
DONOR_DICT = {}


def initial_prompt():
    user_menu_choice = input('Choose: Thank You Letter or Report  ')
    return user_menu_choice.lower()


def initial_prompt_validator(user_menu_choice):
    if user_menu_choice in ('thank you letter', 'report'):
        return user_menu_choice
    else:
        print('Invalid Input')
        return 'invalid input'


def menu_choice_action(user_menu_choice):
    if user_menu_choice == 'thank you letter':
        name_prompt()
    elif user_menu_choice == 'report':
        create_report()
    else: 
        initial_prompt()

def name_prompt():
    donor_name_input = input('Enter Donor Name or List  ')
    return donor_name_input.lower


def name_prompt_validator(donor_name_input):
    if isinstance(donor_name_input, str) and donor_name_input != ' ':
        return donor_name_input
    else:
        print('Invalid Input')
        return 'invalid input'


def name_input_action(donor_name_input):
    if donor_name_input == 'list':
        print(DONOR_DICT.keys())
        name_prompt()
    elif donor_name_input == 'invalid input':
        name_prompt()
    else:
        DONOR_DICT.setdefault(donor_name_input.lower(), [])
        amount_prompt()


def amount_prompt():
    donation_amount = input('Enter Donation Amount  ')
    return donation_amount


def amount_prompt_validator(donation_amount):
    if isinstance(donation_amount, int) or isinstance(donation_amount, float):
        return donation_amount
    else:
        print('Invalid Input')
        return 'invalid input'

    # if isinstance(donor_amount.lower(), str):
    #     donor_dict.setdefault(donor_name_input.lower(), []).append(donor_name_input.lower())


def create_report():
    pass
