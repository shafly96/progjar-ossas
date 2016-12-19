from ftplib import FTP
import sys

username = "user"
password = "password"

try:
    ftp = FTP('localhost')
    ftp.login(username, password)
    ftp.retrlines('LIST')
    ftp.quit()

except Exception, e:
    print "username or password is wrong or the server is unreachable"
    sys.exit(1)