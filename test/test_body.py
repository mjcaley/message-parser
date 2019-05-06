#!/usr/bin/env python3

import pytest

from message_parser.body import PlainTextBody, AsciiBody, UTF8Body


@pytest.fixture
def utf8():
    return 'utf8'


@pytest.fixture
def ascii_encoding():
    return 'ascii'


@pytest.fixture
def example_text():
    return 'Example text'


def test_plain_text_body_init(utf8, example_text):
    p = PlainTextBody(encoding=utf8, body=example_text)

    assert 'p' in locals()


def test_plain_text_encoding_property(utf8, example_text):
    p = PlainTextBody(encoding=utf8, body=example_text)

    assert p.encoding == utf8


def test_plain_text_body_property(utf8, example_text):
    p = PlainTextBody(encoding=utf8, body=example_text)

    assert p.body == example_text


def test_plain_text_body_from_bytes(utf8, example_text):
    p = PlainTextBody(encoding=utf8, body=example_text.encode('ascii'))

    assert p.body == example_text


def test_plain_text_body_raises_value(utf8):
    p = PlainTextBody(encoding=utf8, body='')

    with pytest.raises(ValueError):
        p.body = 42


def test_plain_text_body_bytes(utf8, example_text):
    p = PlainTextBody(encoding=utf8, body=example_text)

    assert bytes(p) == example_text.encode(utf8)


def test_plain_text_body_str(utf8, example_text):
    p = PlainTextBody(encoding=utf8, body=example_text)

    assert str(p) == example_text


def test_ascii_body_properties(ascii_encoding, example_text):
    a = AsciiBody(body=example_text)

    assert a.encoding == ascii_encoding
    assert a.body == example_text


def test_utf8_body_properties(utf8, example_text):
    u = UTF8Body(body=example_text)

    assert u.encoding == utf8
    assert u.body == example_text
