#!/usr/bin/env python3

from .body import PlainTextBody, AsciiBody, UTF8Body

"""
=============
Mixin Classes
=============

MessageBase

Header - contains header fields

Body - contains message body

MimeBody - contains MIME encoded body

8BitHeaders - bytes output
"""


class Message:
    def __init__(self, from_, subject=None, body=None):
        self.headers = {}
        self.body = None

        self.from_(from_)
        if subject:
            self.subject(subject)
        if body:
            self.body = AsciiBody(body)

    def from_(self, address):
        self.headers["From"] = address
        return self

    def to(self, address, *addresses):
        self.headers["To"] = [address, *addresses]
        return self

    def cc(self, address, *addresses):
        self.headers["Cc"] = [address, *addresses]
        return self

    def bcc(self, address, *addresses):
        self.headers["Bcc"] = [address, *addresses]
        return self

    def subject(self, value):
        self.headers["Subject"] = value
        return self

    def plain_text(self, text, encoding):
        self.body = PlainTextBody(encoding, text)
        return self

    # Message controls
    def content_type(self, encoding):
        self.body


class MessageBase:
    def __init__(self, *args, **kwargs):
        pass


class HeaderBase(MessageBase):
    def __init__(self, *args, header=None, **kwargs):
        self.__header = dict()
        super().__init__(**kwargs)

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, value):
        self.__header = value


class BodyBase(MessageBase):
    def __init__(self, *args, body=None, **kwargs):
        self.__body = body
        super().__init__(**kwargs)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        self.__body = value

    @body.deleter
    def body(self):
        self.__body = None


class ToBytes(HeaderBase, BodyBase, MessageBase):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def __bytes__(self):
        return b"%(header_section)b\r\n%(body_section)b" % {
            "header_section": bytes(self.header),
            "body_section": bytes(self.body),
        }
