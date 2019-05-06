#!/usr/bin/env python3


class PlainTextBody:
    __slots__ = ["encoding", "_body"]

    def __init__(self, encoding, body):
        self.encoding = encoding
        self.body = body

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, text):
        if isinstance(text, str):
            self._body = text
        elif isinstance(text, bytes):
            self._body = text.decode(self.encoding)
        else:
            raise ValueError("Must be str or bytes object")

    def __bytes__(self):
        return self.body.encode(self.encoding)

    def __str__(self):
        return self.body


class AsciiBody(PlainTextBody):
    def __init__(self, body):
        super().__init__("ascii", body)


class UTF8Body(PlainTextBody):
    def __init__(self, body):
        super().__init__("utf8", body)
