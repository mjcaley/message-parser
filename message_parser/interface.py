#!/usr/bin/env python3

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
        return b'%(header_section)b\r\n%(body_section)b' % \
               {'header_section': bytes(self.header), 'body_section': bytes(self.body)}
