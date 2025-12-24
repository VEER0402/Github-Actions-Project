# app.py
# This is a just to verify that ci is working or not
# thisis the the second cheack
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
