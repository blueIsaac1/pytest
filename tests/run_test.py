from tests import run

# mock total
def test_get_discount(mocker):
    mocker.patch("tests.run.fetch_discount_rate", return_value=0.15)
    
    resp = run.get_discount(100)
    assert resp == 85 and isinstance(resp, float)
    
# mockspy - integration
def test_get_discount_with_spy_integration(mocker):
    spy = mocker.spy(run, "fetch_discount_rate")
    resp = run.get_discount(100)
    
    assert resp == 91.00 and isinstance(resp, float) # return test
    
    spy.assert_called_once() # comportament test
    spy.assert_called_with(0.9)
    
def fake_discount_rate(initial_value):
    return 0.40

def test_get_discount_with_spy_and_custom_return(mocker): # spy with mock comportament
    spy = mocker.patch("tests.run.fetch_discount_rate", side_effect=fake_discount_rate)
    result = run.get_discount(100)
    print(result)
    assert result == 60.0
    spy.assert_called_once()
    spy.assert_called_with(0.9)