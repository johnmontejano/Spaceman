from app import *

def test_is_guess_in_word():
   assert is_guess_in_word('c', 'cat') == True
   assert is_guess_in_word('d', 'cat') == False
   assert is_guess_in_word('f', 'cat') == False

def test_is_word_guessed():
   assert is_word_guessed('cat', 'cat') == True
   assert is_word_guessed('cat', 'csa') == False
   assert is_word_guessed('cat', 'cia') == False

def test_get_guessed_word ():
    assert get_guessed_word('world',['w', 'e', 'l']) == "w _ _ l _ "
    assert get_guessed_word('cat', ['a', 'r', 'g', 'f']) == '_ _ _  '
    assert get_guessed_word('chaotic', ['c', 'i', 's', 'r']) == 'c _ _ _ _ _ c '







 