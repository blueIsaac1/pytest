from run import divisao, info

def test_divisao():
    val = 8
    resp = divisao(val)

    assert resp == 4
    assert isinstance(resp, float)
    
def test_info():
    resp = info()
    assert isinstance(resp, dict)
    assert "is_check" and "age" and 200 and 404 in resp
    
    assert isinstance(resp["is_check"], bool)
    assert isinstance(resp["age"], int)
    assert isinstance(resp[200], str)
    assert isinstance(resp[404], str)
    
    # assert True == resp["is_check"]
    assert resp["is_check"]
    assert 18 == resp["age"]
    assert "ok" in resp[200]
    assert "not found" in resp[404]