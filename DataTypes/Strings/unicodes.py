Converting to Bytes. The opposite method of bytes.decode() is str.encode(),
which returns a bytes representation of the Unicode string,
encoded in the requested encoding.


The errors parameter is the same as the parameter of the
decode() method but supports a few more possible handlers.



UTF-8 is one such encoding.
The low codepoints are encoded using a single byte,
and higher codepoints are encoded as sequences of bytes.

Python's unicode type is a collection of codepoints.

The line ustring = u'A unicode \u018e string \xf1' creates a
Unicode string with 20 characters.



Python's str type is a collection of 8-bit characters. The English alphabet can be represented using these 8-bit characters, but symbols such as ±, ♠, Ω and ℑ cannot.

Unicode is a standard for working with a wide range of characters. Each symbol has a codepoint (a number), and these codepoints can be encoded (converted to a sequence of bytes) using a variety of encodings.

UTF-8 is one such encoding. The low codepoints are encoded using a single byte, and higher codepoints are encoded as sequences of bytes.

Python's unicode type is a collection of codepoints. The line ustring = u'A unicode \u018e string \xf1' creates a Unicode string with 20 characters.

When the Python interpreter displays the value of ustring, it escapes two of the characters (Ǝ and ñ) because they are not in the standard printable range.

The line s = unistring.encode('utf-8') encodes the Unicode string using UTF-8. This converts each codepoint to the appropriate byte or sequence of bytes. The result is a collection of bytes, which is returned as a str. The size of s is 22 bytes, because two of the characters have high codepoints and are encoded as a sequence of two bytes rather than a single byte.

When the Python interpreter displays the value of s, it escapes four bytes that are not in the printable range (\xc6, \x8e, \xc3, and \xb1). The two pairs of bytes are not treated as single characters like before because s is of type str, not unicode.

The line t = unicode(s, 'utf-8') does the opposite of encode(). It reconstructs the original codepoints by looking at the bytes of s and parsing byte sequences. The result is a Unicode string.

The call to codecs.open() specifies utf-8 as the encoding, which tells Python to interpret the contents of the file (a collection of bytes) as a Unicode string that has been encoded using UTF-8.
