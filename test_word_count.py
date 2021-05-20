
import word_count

def test_answer():
    assert word_count.count("aba") == 1;

def test_answer2():
    assert word_count.count("aba") == 2;

def test_answer3():
    assert word_count.count("ab a") == 2;

def test_answer4():
    assert word_count.count("ab a") == 3;

def test_answer5():
    assert word_count.count("1     233 21") == 3;

def test_answer6():
    assert word_count.count("12     33 21") == 2;
