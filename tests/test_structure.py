import pytest 
from all_questions import (
    question1,
)
from pytest_utils.decorators import max_score

@max_score(5)
def test_question1_structure():
    answer = question1()
    assert isinstance(answer["correct"], int), "answer['correct'] should be an int"
