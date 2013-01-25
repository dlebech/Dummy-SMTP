#!/usr/bin/env python
"""A little script that starts an SMTP server and saves outgoing mails to the
filesystem."""

import os
import smtpd
import datetime
import asyncore
import argparse

class DummySMTPServer(smtpd.SMTPServer):
    """An smtp server that saves outgoing mails to files."""

    def __init__(self, addr, port, maildir):
        smtpd.SMTPServer.__init__(self, (addr, port), None)
        self.maildir = maildir

    def process_message(self, peer, mailfrom, recipients, data):
        print 'New mail from %s' % mailfrom
        today = datetime.datetime.today()
        mail = open('%s/%s.eml' % (self.maildir,
                                   today.strftime('%Y-%m-%d-%H:%M:%S')), 
                    'w')
        mail.write(data)
        mail.close()


parser = argparse.ArgumentParser()
parser.description = ('Sets up an SMTP server that saves outgoing emails to '
                      'a directory on the local machine')
parser.add_argument('-a', '--addr',
                    default='localhost',
                    help='The address to listen on, default is localhost')
parser.add_argument('-p', '--port',
                    type=int, 
                    default=25,
                    help='The port to listen to, default is 25')
parser.add_argument('-m', '--maildir',
                    default='mails',
                    help='The directory to save emails to, default is mails')


if __name__ == "__main__":
    args = parser.parse_args()
    if not os.path.isdir(args.maildir):
        print 'The given maildir does not exist.'
    else:
        smtp_server = DummySMTPServer(args.addr, args.port, args.maildir)
        print 'Running dummy smtp server on port %s' % args.port
        try:
            asyncore.loop()
        except KeyboardInterrupt:
            smtp_server.close()
