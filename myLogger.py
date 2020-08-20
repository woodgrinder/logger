#!/usr/bin/python

import logging
import os

myFile = "mylog.log"

class myMod():
    def __init__(self, logSpec):
        logSpec = str(logSpec).upper()
        fmtStr = '%(asctime)s|%(funcName)s:%(lineno)-4s|%(levelname)-8s|%(message)s'
        logging.basicConfig(filename=myFile, format=fmtStr)
        logger = logging.getLogger()
        if logSpec == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif logSpec == "INFO":
            logger.setLevel(logging.INFO)
        elif logSpec == "WARNING":
            logger.setLevel(logging.WARNING)
        elif logSpec == "ERROR":
            logger.setLevel(logging.ERROR)
        elif logSpec == "Critical":
            logger.setLevel(logging.CRITICAL)

    def doTask(self):
        logging.debug("debug")
        logging.info("info")
        logging.warning("warning")
        logging.error("error")
        logging.critical("critical")
        logging.critical("---------------------")

if __name__ == "__main__":
    os.system("del "+myFile)

    a = myMod("DEBUG")
    a.doTask()

    b = myMod("INFO")
    b.doTask()

    c = myMod("WARNING")
    c.doTask()

    d = myMod("ERROR")
    d.doTask()

    e = myMod("CRITICAL")
    e.doTask()

    os.system("type "+myFile)
