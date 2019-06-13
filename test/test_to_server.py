#!/usr/bin/env python3

import smtplib


def test_accepted():
    conn = smtplib.SMTP('localhost')
    conn.sendmail(
        from_addr='outside@localhost',
        to_addrs='mjcaley@localhost',
        msg='This is my message'
    )

    assert True
