#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Rsync settings
rsyncsource = 'rsync://debian.linux.org.tw/ubuntu/'
dirpath = ['mirror', 'ubuntu']
archivedir = 'ubuntu'
releasedir = 'release'
lockfile = ['mirror', 'LockRsync.lock']

# log setting
logfilepath = '/var/log/ubuntu/rsync'
# default <os>_rsync.log
logfilename = ''
# ind only, default 5 MB
maxmb = 5
# DEBUG, INFO, WARNING, ERROR and CRITICAL, default WARNING
loglevel = 'DEBUG'

# mail setting
mailto = 'mirror@linux.cs.nctu.edu.tw'
