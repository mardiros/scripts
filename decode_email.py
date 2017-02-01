#!/usr/bin/env python3

import email
import sys


msg = email.message_from_string(sys.stdin.read())

for key, val in msg.items():
    print("{}: {}".format(key, val))

print()
print(msg.get_payload(decode=True).decode('utf-8'))

