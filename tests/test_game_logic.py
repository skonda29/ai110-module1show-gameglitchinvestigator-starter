import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


#copilot test cases for check_guess function
def test_guess_boundary_low():
    # If secret is 1 and guess is 0, hint should be "Too Low"
    result = check_guess(0, 1)
    assert result[0] == "Too Low"

def test_guess_boundary_high():
    # If secret is 100 and guess is 101, hint should be "Too High"
    result = check_guess(101, 100)
    assert result[0] == "Too High"

def test_guess_negative():
    # If secret is 50 and guess is -10, hint should be "Too Low"
    result = check_guess(-10, 50)
    assert result[0] == "Too Low"