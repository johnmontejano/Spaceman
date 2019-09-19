from app import *

def test_is_guess_in_word():
   assert is_guess_in_word('c', 'cat') == True
   assert is_guess_in_word('d', 'cat') == False
   assert is_guess_in_word('f', 'cat') == False

def test_get_guessed_word():
   assert get_guessed_word('cat', 'cat') == True
   assert get_guessed_word('cat', 'csa') == False
   assert get_guessed_word('cat', 'cia') == False









 