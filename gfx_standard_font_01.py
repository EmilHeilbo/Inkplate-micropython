# The MIT License (MIT)
#
# Copyright (c) 2018 Jonah Yolles-Murphy for Makers Anywhere!
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`gfx_standard_font_01`
====================================================

CircuitPython pixel graphics drawing library.

* Author(s): Jonah Yolles-Murphy

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* letter format:
    { 'character_here' : bytearray(WIDTH,HEIGHT,right-most-data,more-bytes-here,left-most-data')}
    the right most bit is the top most bit of each vertical stripe of a char
* Key format:
    keys of one length only represent one character. longer then one is either
    extended characters or special characters like the degree sign.
    all extended or special charaters have all capitalized keys.
    "?CHAR?" is used when an input character is not in the font dictionary

"""
# pylint: disable=invalid-name
text_dict = {
    "A": bytearray(b"\x05\x07?DDD?"),
    "B": bytearray(b"\x05\x07\x7fAII6"),
    "C": bytearray(b'\x05\x07>AAA"'),
    "D": bytearray(b'\x05\x07\x7fAA"\x1c'),
    "E": bytearray(b"\x05\x07\x7fIIIA"),
    "F": bytearray(b"\x05\x07\x7fHH@@"),
    "G": bytearray(b"\x05\x07>AII."),
    "H": bytearray(b"\x05\x07\x7f\x08\x08\x08\x7f"),
    "I": bytearray(b"\x05\x07AA\x7fAA"),
    "J": bytearray(b"\x05\x07FA~@@"),
    "K": bytearray(b"\x05\x07\x7f\x08\x08t\x03"),
    "L": bytearray(b"\x05\x07\x7f\x01\x01\x01\x01"),
    "M": bytearray(b"\x05\x07\x7f \x10 \x7f"),
    "N": bytearray(b"\x05\x07\x7f \x1c\x02\x7f"),
    "O": bytearray(b"\x05\x07>AAA>"),
    "P": bytearray(b"\x05\x07\x7fHHH0"),
    "Q": bytearray(b"\x05\x07>AEB="),
    "R": bytearray(b"\x05\x07\x7fHLJ1"),
    "S": bytearray(b"\x05\x072III&"),
    "T": bytearray(b"\x05\x07@@\x7f@@"),
    "U": bytearray(b"\x05\x07~\x01\x01\x01~"),
    "V": bytearray(b"\x05\x07p\x0e\x01\x0ep"),
    "W": bytearray(b"\x05\x07|\x03\x04\x03|"),
    "X": bytearray(b"\x05\x07c\x14\x08\x14c"),
    "Y": bytearray(b"\x05\x07`\x10\x0f\x10`"),
    "Z": bytearray(b"\x05\x07CEIQa"),
    "Æ": bytearray(b"\x05\x07?D\x7fIA"),
    "Ø": bytearray(b"\x05\x07>C]a>"),
    "Å": bytearray(b"\x05\x07\x1f$d$\x1f"),

    "a": bytearray(b"\x05\x07\x02\x15\x15\x15\x0f"),
    "b": bytearray(b"\x05\x07\x7f\x05\x09\x09\x06"),
    "c": bytearray(b'\x05\x07\x0e\x11\x11\x11\x05'),
    "d": bytearray(b'\x05\x07\x06\x09\x09\x05\x7f'),
    "e": bytearray(b"\x05\x07\x0e\x15\x15\x15\x08"),
    "f": bytearray(b"\x05\x07\x08?HH "),
    "g": bytearray(b"\x05\x08\x00\x19%%>"),
    "h": bytearray(b"\x05\x07\x7f\x04\x08\x08\x05"),
    "i": bytearray(b"\x05\x07\x00\x10_\x00\x00"),
    "j": bytearray(b"\x05\x08\x00\x01\x01\xbe\x00"),
    "k": bytearray(b"\x05\x07\x7f\x04\x0a\x11\x00"),
    "l": bytearray(b"\x05\x07\x00\x7e\x01\x00\x00"),
    "m": bytearray(b"\x05\x07\x1f\x10\x1f\x10\x0f"),
    "n": bytearray(b"\x05\x07\x1f\x08\x10\x10\x0f"),
    "o": bytearray(b"\x05\x07\x0e\x11\x11\x11\x0e"),
    "p": bytearray(b"\x05\x08?$$$\x18"),
    "q": bytearray(b"\x05\x08\x18$$$?"),
    "r": bytearray(b"\x05\x07\x1f\x08\x10\x10\x08"),
    "s": bytearray(b"\x05\x07\x09\x15\x15\x15\x12"),
    "t": bytearray(b"\x05\x07\x10\x7e\x11\x11\x02"),
    "u": bytearray(b"\x05\x07\x1e\x01\x01\x02\x1f"),
    "v": bytearray(b"\x05\x07\x18\x06\x01\x06\x18"),
    "w": bytearray(b"\x05\x07\x1e\x01\x0e\x01\x1e"),
    "x": bytearray(b"\x05\x07\x11\x09\x04\x09\x11"),
    "y": bytearray(b"\x05\x089\x05\x05\x05>"),
    "z": bytearray(b"\x05\x07\x11\x13\x15\x19\x11"),
    "æ": bytearray(b"\x05\x07\x16\x15\x0f\x15\x0d"),
    "ø": bytearray(b"\x05\x07\x0e\x13\x15\x19\x0e"),
    "å": bytearray(b"\x05\x07\x02\x15U\x15\x0f"),

    "0": bytearray(b"\x05\x07>EIQ>"),
    "1": bytearray(b"\x05\x07\x11!\x7f\x01\x01"),
    "2": bytearray(b"\x05\x07!CEI1"),
    "3": bytearray(b"\x05\x07FAQiF"),
    "4": bytearray(b"\x05\x07x\x08\x08\x08\x7f"),
    "5": bytearray(b"\x05\x07rQQQN"),
    "6": bytearray(b"\x05\x07\x1e)II\x06"),
    "7": bytearray(b"\x05\x07@GHP`"),
    "8": bytearray(b"\x05\x076III6"),
    "9": bytearray(b"\x05\x070IIJ<"),
    ")": bytearray(b"\x05\x07\x00A>\x00\x00"),
    "(": bytearray(b"\x05\x07\x00\x00>A\x00"),
    "[": bytearray(b"\x05\x07\x00\x00\x7fA\x00"),
    "]": bytearray(b"\x05\x07\x00A\x7f\x00\x00"),
    ".": bytearray(b"\x05\x07\x00\x03\x03\x00\x00"),
    "'": bytearray(b"\x05\x07\x00\x000\x00\x00"),
    ":": bytearray(b"\x05\x07\x00\x0066\x00"),
    "?CHAR?": bytearray(b"\x05\x07\x7f_RG\x7f"),
    "!": bytearray(b"\x05\x07\x00{{\x00\x00"),
    "?": bytearray(b"\x05\x07 @EH0"),
    ",": bytearray(b"\x05\x07\x00\x05\x06\x00\x00"),
    ";": bytearray(b"\x05\x07\x0056\x00\x00"),
    "/": bytearray(b"\x05\x07\x01\x06\x080@"),
    ">": bytearray(b"\x05\x07Ac6\x1c\x08"),
    "<": bytearray(b"\x05\x07\x08\x1c6cA"),
    "%": bytearray(b"\x05\x07af\x083C"),
    "@": bytearray(b"\x05\x07&IOA>"),
    "#": bytearray(b"\x05\x07\x14\x7f\x14\x7f\x14"),
    "$": bytearray(b"\x05\x072I\x7fI&"),
    "€": bytearray(b'\x05\x07\x14\x1eUU"'),
    "&": bytearray(b'\x05\x076IU"\x05'),
    "*": bytearray(b"\x05\x07(\x10|\x10("),
    "-": bytearray(b"\x05\x07\x00\x08\x08\x08\x00"),
    "_": bytearray(b"\x05\x07\x01\x01\x01\x01\x01"),
    "+": bytearray(b"\x05\x07\x08\x08>\x08\x08"),
    "=": bytearray(b"\x05\x07\x00\x14\x14\x14\x00"),
    '"': bytearray(b"\x05\x07\x00p\x00p\x00"),
    "`": bytearray(b"\x05\x07\x00\x00 \x10\x00"),
    "~": bytearray(b"\x05\x07\x08\x10\x08\x04\x08"),
    " ": bytearray(b"\x05\x07\x00\x00\x00\x00\x00"),
    "^": bytearray(b"\x05\x07\x10 @ \x10"),
    "NONE": bytearray(b"\x00\x07"),
    "BLANK": bytearray(b"\x05\x07\x00\x00\x00\x00\x00"),
    "BATA0": bytearray(b"\x0b\x07\x7fAAAAAAAA\x7f\x1c"),
    "BATA1": bytearray(b"\x0b\x07\x7fA]AAAAAA\x7f\x1c"),
    "BATA2": bytearray(b"\x0b\x07\x7fA]]AAAAA\x7f\x1c"),
    "BATA3": bytearray(b"\x0b\x07\x7fA]]]AAAA\x7f\x1c"),
    "BATA4": bytearray(b"\x0b\x07\x7fA]]]]AAA\x7f\x1c"),
    "BATA5": bytearray(b"\x0b\x07\x7fA]]]]]AA\x7f\x1c"),
    "BATA6": bytearray(b"\x0b\x07\x7fA]]]]]]A\x7f\x1c"),
    "BATACHRG": bytearray(b"\x0b\x07\x7fAIYyOMIA\x7f\x1c"),
    "BATB0": bytearray(b"\x0b\x07\x7fAAAAAAAA\x7f\x1c"),
    "FULL": bytearray(b"\x05\x07\x7f\x7f\x7f\x7f\x7f"),
    "\n": bytearray(b"\x05\x07\x00\x00\x00\x00\x00"),
    "DEGREESIGN": bytearray(b"\x05\x07\x18$$\x18\x00"),
}
