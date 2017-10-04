#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

from log import mylog
from settings import rsyncsource
from settings import dirpath
from settings import archivedir
from settings import releasedir
from settings import lockfile

recipient = 'mirror@linux.cs.nctu.edu.tw'
subject = 'ubuntu archive sync error'


def mailto():
    
    try:
      process = subprocess.Popen(['mail', '-s', subject, recipient],
                               stdin=subprocess.PIPE)
    except Exception, error:
        print error
    process.communicate(body)

send_message(recipient, subject, body)

print("sent the email")

def MergePath(finaldir):
    tmppath = os.path.join(os.sep, *dirpath)
    tmppath = os.path.join(tmppath, finaldir)
    return os.path.abspath(tmppath)


def InitSystem():
    PID = os.getpid()
    logger = mylog()
    archivedirpath = MergePath(archivedir)
    releasedirpath = MergePath(releasedir)
    lockrsync = os.path.abspath(os.sep, *lockfile)
    if os.path.isfile(lockrsync):
        with open(lockrsync, 'r') as lock:
            mailto(lock)
    pass


def ArchiveMirror():
    pass


def ReleaseMirror():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
