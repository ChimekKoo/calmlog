# Calmlog

#### Code examples:
```python
from calmlog import Logger, levels

logger = Logger("logfile.log", debug=True) # If debug is true, don't ignore DEBUG level.

logger.writelog("It's info!")
logger.writelog("It's debug...", level=levels.DEBUG)
logger.writelog("---Warring---", level=levels.WARRING)
logger.writelog("Error!", level=levels.ERROR)
logger.writelog("FATAL!!!", level=levels.FATAL)

mynewlevel = levels.Level("MY-LEVEL-NAME")
logger.writelog("My new level ;-) !", level=mynewlevel, fileout=False) # If 'fileout' is true, write log to file.
```
More documentation:
```
>>> import calmlog
>>> help(calmlog)
```
