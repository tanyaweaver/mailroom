# -*- coding: utf -8 -*-
import pytest

DONOR_DICT_KEYS = ['baker', 'williams', 'davidson']
DONOR_DICT_TEST = {
    'baker': [10, 20],
    'williams': [30, 40, 50],
    'davidson': [35, 28, 60]
}

MENU_TABLE = [
    ('thank you letter', 'thank you letter'),
    ('report', 'report'),
    (123, 'invalid input')
]


NAME_TABLE = [
    ('dan', 'dan'),
    (' ', 'invalid input'),
    (123, 'invalid input')
]


AMOUNT_TABLE = [
    (1, 1),
    (1.5, 1.5),
    ('a', 'invalid input'),
]

@pytest.mark.parametrize('u_input, result', MENU_TABLE)
def test_initial_prompt_validator(u_input, result):
    from mailroom import initial_prompt_validator
    assert initial_prompt_validator(u_input) == result


@pytest.mark.parametrize('u_input, result', NAME_TABLE)
def test_name_prompt_validator(u_input, result):
    from mailroom import name_prompt_validator
    assert name_prompt_validator(u_input) == result


@pytest.mark.parametrize('u_input, result', AMOUNT_TABLE)
def test_amount_prompt_validator(u_input, result):
    from mailroom import amount_prompt_validator
    assert amount_prompt_validator(u_input) == result



# def test_name_prompt_elif(DONOR_DICT):
#     from mailroom import name_prompt
#     assert  name_prompt(DONOR_DICT_TEST)== DONOR_DICT_KEYS 
