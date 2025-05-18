def divisao(x: int) -> float:
    return x / 2

def info() -> dict:
    return {
        200: "ok",
        404: "not found",
        "age": 18,
        "is_check": True
    }
    
def error():
    raise Exception("erro grave")