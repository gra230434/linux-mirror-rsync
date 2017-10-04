#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from logging.handlers import RotatingFileHandler
# settings
from settingsdefault import OPERATINGSYSTEM
from settingsdefault import RSYNCUSER
from settings import logfilename
from settings import loglevel
from settings import maxmb


def MaxBytes():
	if type(maxmb) is int:
		return maxmb*1024*1024
	else:
		return 5*1024*1024


def MergeFileName():
	if logfilename is not None:
		if logfilename.find('.log'):
		    return logfilename
		else:
			return '{}.log'.format(logfilename)
	return '{}_rsync.log'.format(OPERATINGSYSTEM)


def RotatingFile():
	Filename = MergeFileName()
	Bytes = MaxBytes()
	return RotatingFileHandler(Filename, maxBytes=Bytes)


def LogLevel():
	logger = logging.getLogger(RSYNCUSER)
	# DEBUG, INFO, WARNING, ERROR and CRITICAL
	if loglevel is 'DEBUG':
		logger.setLevel(logging.DEBUG)
	elif loglevel is 'INFO':
		logger.setLevel(logging.INFO)
	elif loglevel is 'WARNING':
		logger.setLevel(logging.WARNING)
	elif loglevel is 'ERROR':
		logger.setLevel(logging.ERROR)
	elif loglevel is 'CRITICAL':
		logger.setLevel(logging.CRITICAL)
	else:
		logger.setLevel(logging.DEBUG)
	return logger


def mylog():
    logger = LogLevel()
    handler = RotatingFile()
    logger.addHandler(handler)
    return logger

def main():
	mylog()

if __name__ == '__main__':
	main()