from tests import run

def test_get_discount(mocker):
    mocker.patch("tests.run.fetch_discount_rate", return_value=0.15)
    
    resp = run.get_discount(100)
    assert resp == 85 and isinstance(resp, float)
    print(resp)