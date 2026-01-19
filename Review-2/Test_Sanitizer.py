import pytest

from Sanitizer import read_config

def test_commentsandemptylines():
    lines = ["", "# comment", "#dhiraj"]
    config, errors = read_config(lines)
    assert config == {}
    assert errors == []

def test_valid_errors():
    lines = [
        "# dinesh",
        " owner = dhiruu ",
        "age = 22",
        "it ",
        "company",
        "names = diensh"
    ]

    config, errors = read_config(lines)

    expect_config = {'owner ': 'dhiruu', 'age ': '22', 'names ': 'diensh'}
    expect_errors = [(4, 'it'), (5, 'company')]

    assert config == expect_config
    assert errors == expect_errors
    
    