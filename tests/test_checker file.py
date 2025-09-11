# tests/test_checker.py
from check_password import check_password_strength

def test_very_weak():
    r = check_password_strength('abc')
    assert r['label'] in ('Very weak', 'Weak')

def test_strong():
    r = check_password_strength('S3cureP@ssw0rd!')
    assert r['label'] in ('Strong', 'Very strong')
