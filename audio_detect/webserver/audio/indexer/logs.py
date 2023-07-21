import os
import re
import datetime
import logging
import sys

try:
    import codecs
except ImportError:
    codecs = None

class MultiprocessHandler(logging.FileHandler):
    def __init__(self,filename,when='D',backupCount=0,encoding=None,delay=False):

        self.prefix = filename
        self.backupCount = backupCount
        self.when = when.upper()
        self.extMath = r"^\d{4}-\d{2}-\d{2}"

        self.when_dict = {
            'S':"%Y-%m-%d-%H-%M-%S",
            'M':"%Y-%m-%d-%H-%M",
            'H':"%Y-%m-%d-%H",
            'D':"%Y-%m-%d"
        }

        self.suffix = self.when_dict.get(when)
        if not self.suffix:
            raise ValueError(u"指定的日期间隔单位无效: %s" % self.when)
        
        self.filefmt = os.path.join("logs","%s.%s" % (self.prefix,self.suffix))
        
        self.filePath = datetime.datetime.now().strftime(self.filefmt)
        
        _dir = os.path.dirname(self.filefmt)
        try:
        
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        except Exception:
            print(u"创建文件夹失败")
            print(u"文件夹路径：" + self.filePath)
            pass

        if codecs is None:
            encoding = None

        logging.FileHandler.__init__(self,self.filePath,'a+',encoding,delay)

    def shouldChangeFileToWrite(self):
      
        _filePath = datetime.datetime.now().strftime(self.filefmt)
      
        if _filePath != self.filePath:
            self.filePath = _filePath
            return True
        return False

    def doChangeFile(self):
    
        self.baseFilename = os.path.abspath(self.filePath)
  
        if self.stream:
            
            self.stream.close()
            
            self.stream = None

        if not self.delay:
          
            self.stream = self._open()

        if self.backupCount > 0:
            print('-----------delete backup logs------------')
            for s in self.getFilesToDelete():
                print(s)
                os.remove(s)

    def getFilesToDelete(self):

        dirName,_ = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []

        prefix = self.prefix + '.'
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:

                suffix = fileName[plen:]

                if re.compile(self.extMath).match(suffix):
                    result.append(os.path.join(dirName,fileName))
        result.sort()


        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):

        try:
            if self.shouldChangeFileToWrite():
                self.doChangeFile()
            logging.FileHandler.emit(self,record)
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            self.handleError(record)


def write_log(log_message, level=0):
    logger = logging.getLogger()
    formattler = '%(asctime)s - %(levelname)s - %(message)s'
    fmt = logging.Formatter(formattler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(fmt)


    log_name = "app.log"
    file_handler = MultiprocessHandler(log_name, when='D', backupCount=7)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fmt)


    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    if level:
        logger.error(log_message)
    else:
        logger.info(log_message)


