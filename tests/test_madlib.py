import pytest
from madlib import read_template, parse_template, merge

def test_read_template_returns_stripped_string():
    actual = read_template("madlib.txt")
    expected = """It was a {Adjective} and {Adjective} {Noun}.

Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."""
    assert actual == expected

def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected

def test_read_template_raises_exception_with_bad_path():
    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_newList():
    parts = ("Adjective", "Noun", "Verb")
    input_values = ["spooky", "cat", "ran"]
    input_index = 0
    def mock_input(prompt):
        nonlocal input_index
        value = input_values[input_index]
        input_index += 1
        return value
    
    
def test_parse_template_with_no_fillable_parts():
    actual_stripped, actual_parts = parse_template("This is a static template.")
    expected_stripped = "This is a static template."
    expected_parts = ()
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts