from word_frequency_counter import process_text, read_file
import pytest

def test_process_text():
    text = "Don't stop believing. It's 3 times better!"
    result = process_text(text)
    assert "don't" in result      
    assert "3" in result  
    assert "it's" in result       
    assert len(result) == 7

def test_read_file():
    text = read_file('test.txt')  
    assert text == "hello world this is a test file."  
    assert isinstance(text, str)  
    assert "hello" in text 
    assert "test" in text 

    csv_text = read_file('test.csv')
    assert csv_text == "hello world this is a test file" 
    assert isinstance(csv_text, str)  
    assert "world" in csv_text  
    assert "python" not in csv_text

pytest.main(["-v", "--tb=line", "-rN", __file__])