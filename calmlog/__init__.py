from calmlog import levels
from datetime import datetime
from sys import stdout


class Logger:

    """
    Logger class.
    """

    def __init__(self, logfilepath, debug=False):

        """
        :param logfilepath: Path to log file.
        :param debug: If 'debug' is true, don't ignore DEBUG level.
        """

        if not isinstance(debug, bool):
            raise TypeError("'debug' param must be a boolean.")
        else:
            self.debug = debug

        if not isinstance(logfilepath, str):
            raise TypeError("'logfilepath' param must be a string.")
        else:
            self.logfilepath = logfilepath

    def writelog(self, text, level=levels.INFO, fileout=True):

        """
        :param text: Text of the log.
        :param level: Level of the log (calmlog.levels.Level instance).
        :param fileout: If 'fileout' is true, write logs to logfile.
        """

        if not isinstance(text, str):
            raise TypeError("'text' param must be a string.")

        if not isinstance(level, levels.Level):
            raise TypeError("'level' param must be an instance of calmlog.levels.Level class.")

        if not isinstance(fileout, bool):
            raise TypeError("'fileout' param must be a boolean.")

        if (not self.debug) and (level == levels.DEBUG):
            return
        else:
            content = "{datetime} => {level}: {text}\n".format(
                datetime=datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
                level=level.getname(),
                text=text
            )

            stdout.write(content)

            if fileout:
                with open(self.logfilepath, "a") as log_file_obj:
                    log_file_obj.write(content)
                    log_file_obj.close()
