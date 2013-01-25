#!/usr/bin/env python
"""Sends a single test email to the SMTP server at the specified address and
port.
"""

import argparse
import smtplib
from email.mime.text import MIMEText

parser = argparse.ArgumentParser()
parser.description = ('Sends a single test email to the SMTP server at the '
                      'specified address and port')
parser.add_argument('-a', '--addr',
                    default='localhost',
                    help='The address to send to, default is localhost')
parser.add_argument('-p', '--port',
                    type=int, 
                    default=25,
                    help='The port to send to, default is 25')

def send_test_email(host, port):
    msg = MIMEText('This is a test email')
    msg['Subject'] = 'Test email'
    msg['From'] = 'sender@test.com'
    msg['To'] = 'receiver@test.com'
    print 'Setting up test SMTP connection'
    s = smtplib.SMTP('localhost', port)
    print 'Sending test email'
    s.sendmail('sender@test.com', ['receiver@test.com'], msg.as_string())
    s.quit()
    print 'The server is working just fine'

if __name__ == "__main__":
    args = parser.parse_args()
    send_test_email(args.addr, args.port)
