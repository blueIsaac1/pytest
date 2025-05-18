from run import error
import pytest

def test_error():
    try:
        error()
    except Exception as e:
        print(e)
        assert str(e) == "erro grave"
        
def test_error_with_pytest():
    with pytest.raises(Exception):
        error()
        
# def test_error_with_pytest():
# with pytest.raises(Exception) as error_info:
#     error()
# assert str(error_info.value) = "erro grave"