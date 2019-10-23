from msc.rot13 import rot13
from msc.rot13 import rot13_char

def test_rot13_char_a():
	assert "n" == rot13_char("a"), "Unexpected character"

def test_rot13_hello():
	assert "uryyb" == rot13("hello"), "Unexpected string"

def test_rot13_helo():
	assert "uryb" == rot13("helo"), "Unexpected string"

