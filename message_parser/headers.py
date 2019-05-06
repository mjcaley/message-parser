#!/usr/bin/env python3


class Header:
    def __init__(self, field):
        self._field = field

    @property
    def field(self):
        return self._field


class UniqueHeader(Header):
    def __init__(self, field):
        super().__init__(field=field)

    def __hash__(self):
        return hash(self.field)


class From(Header):
    def __init__(self, address):
        super().__init__(field="From")
        self.address = address
