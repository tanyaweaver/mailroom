# -*- coding: utf -8 -*-
#from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str, super, zip)
# from __future__ import absolute_import, division, print_function
from __future__ import division
try:
    input = raw_input
except NameError:
    pass
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
    try:
        if int(donor_name_input) or float(donor_name_input):
            print('Invalid Input')
            return 'invalid input'
    except ValueError:
        if donor_name_input != ' ':
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
    try:
        if int(donation_amount) or float(donation_amount):
            return donation_amount
    except ValueError:
        print('Invalid Input')
        return 'invalid input'


def amount_to_dict(donor_name_input, donation_amount, dictionary):
    dictionary.setdefault(donor_name_input, []).append(donation_amount)
    return donor_name_input, dictionary[donor_name_input]


def generate_letter(donor_name_input, donation_amount):
    print('Dear {0}, thank you for your donation of'
          '{1}.').format(donor_name_input, donation_amount)
    initial_prompt()


def do_math(dictionary):
    summary_list = []
    for key in dictionary:
        donor_math_list = []
        value = dictionary[key]
        total = sum(value)
        count = len(value)
        average = total / count
        donor_math_list = [key, total, count, average]
        summary_list.append(donor_math_list)
    return sorted(summary_list, key=lambda x: x[1])


def create_report():
    pass
