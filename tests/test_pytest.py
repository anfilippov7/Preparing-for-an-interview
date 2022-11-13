import pytest
from main import balance


fixture = [
    ('(((([{}]))))', True),
    ('[([])((([[[]]])))]{()}', True),
    ('}{}', False),
]



@pytest.mark.parametrize('staples, result', fixture)
def test_balance(staples, result):
    bal_result = balance(staples)
    assert bal_result == result