# -*- coding: utf -8 -*-
import pytest

DONOR_DICT_KEYS = ['baker', 'williams', 'davidson']
DONOR_DICT_TEST = {
    'baker': [10, 20],
    'williams': [30, 40, 50],
    'davidson': [35, 28, 60]
}

INPUT_TABLE = [
    ('thank you letter', 'thank you letter'),
    ('report', 'report'),
    (123, 'invalid input')
]

@pytest.mark.parametrize('u_input, result', INPUT_TABLE)
def test_initial_prompt_validator(u_input, result):
    from mailroom import initial_prompt_validator
    assert initial_prompt_validator(u_input) == result 




# def test_name_prompt_elif(DONOR_DICT):
#     from mailroom import name_prompt
#     assert  name_prompt(DONOR_DICT_TEST)== DONOR_DICT_KEYS 
