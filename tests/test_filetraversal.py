from musichoarder import filetraversal
import os
import sys
import logging

logger = logging.getLogger("filetraversal")
logger.setLevel(logging.DEBUG)

def printitem(item):
    print(item)
    logger.debug(item)

def test_filetraversal():
    filetraverser = filetraversal.FileTraversal(printitem, printitem)
    result = filetraverser.recurse(os.path.join(os.getcwd(), "tests/testfiles"))
    assert len(result.getfilestraversed()) == 2
    assert len(result.getfolderstraversed()) == 2
    assert result.getmaximumdepth() == 1