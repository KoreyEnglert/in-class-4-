
import palindrome

def test_answer():
    assert palindrome.verify("aba") == True;

def test_answer2():
    assert palindrome.verify("aba") == False;

def test_answer3():
    assert palindrome.verify("ab a") == True;

def test_answer4():
    assert palindrome.verify("ab a") == False;

def test_answer5():
    assert palindrome.verify("123321") == True;

def test_answer6():
    assert palindrome.verify("123321") == False;
