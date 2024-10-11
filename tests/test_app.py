""" This module contains tests for the calculator app"""
from app import App

def test_menu_startup(monkeypatch, capsys):
    """ Test if the menu displays the correct commands at startup """
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    captured = capsys.readouterr()

    assert "Available commands" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "exit" in captured.out
    assert "menu" in captured.out
    assert "Exiting..." in captured.out


def test_add_command(monkeypatch, capsys):
    """ Test add command functionality """
    inputs = iter(['add 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    captured = capsys.readouterr()
    assert "15" in captured.out
    assert "Exiting..." in captured.out

def test_subtract_command(monkeypatch, capsys):
    """ Test subtract command functionality """
    inputs = iter(['subtract 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    captured = capsys.readouterr()
    assert "5" in captured.out
    assert "Exiting..." in captured.out

def test_multiply_command(monkeypatch, capsys):
    """ Test multiply command functionality """
    inputs = iter(['multiply 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    captured = capsys.readouterr()
    assert "50" in captured.out
    assert "Exiting..." in captured.out

def test_divide_command(monkeypatch, capsys):
    """ Test multiply command functionality """
    inputs = iter(['divide 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    captured = capsys.readouterr()
    assert "2" in captured.out
    assert "Exiting..." in captured.out

def test_divide_by_zero(monkeypatch, capsys):
    """ Test divide by zero error handling """
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    app.start()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out
    assert "Exiting..." in captured.out
