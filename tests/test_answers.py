import pytest 
from all_questions import (
    question1,
)
from pytest_utils.decorators import max_score

@max_score(10)
def test_question1():
    answer = question1()
    assert answer["correct"] == 3, "answer['correct'] should be 3"
