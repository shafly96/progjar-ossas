from ftplib import FTP
import sys

try:
    ftp = FTP('localhost')
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    ftp.login(username, password)

    while True:
        input_message = raw_input("Enter input: ")
        if input_message=='HELP':
            print 'CWD [nama folder]= Ubah direktori aktif'
            print 'CWD [../] = Kembali ke atas'
            print 'LIST = Mencetak'
            print 'QUIT = Keluar'
            print 'PWD = Cetak folder aktif'
            print 'MKD [nama file] = Membuat direktori'
            print 'RMD [nama folder] = Menghapus folder'
            print 'DEL [nama file] = Menghapus file'
            print 'REN [nama awal] TO [nama akhir] = Mengganti nama'
            print  'UNDUH [nama file] = Unduh file'
            print 'UPLOAD [nama file] = Upload file'
        elif input_message[0:3]=='CWD':
            if input_message[4:] in ftp.nlst() or input_message[4:]=='../':
                ftp.cwd(input_message[4:])
                print 'Pindah folder '+input_message[4:]
            else:
                print 'Folder Tidak Ada'
        elif input_message=='QUIT':
            print 'Keluar'
            ftp.quit()
            sys.exit(1)
        elif input_message=='LIST':
            print 'List File:'
            ftp.retrlines('LIST')
        elif input_message=='PWD':
            print ftp.pwd()
        elif input_message[0:3]=='MKD':
            ftp.mkd(input_message[4:])
            print 'Membuat folder '+input_message[4:]
        elif input_message[0:3]=='RMD':
            ftp.rmd(input_message[4:])
            print 'Folder '+input_message[4:]+' terhapus'
        elif input_message[0:3]=='DEL':
            ftp.delete(input_message[4:])
            print  'File '+input_message[4:]+' terhapus'
        elif input_message[0:3]=='REN':
            ftp.rename(input_message.split('TO')[0][4:], input_message.split('TO')[1][1:])
            print 'Berhasil direname'
        elif input_message[0:5]=='UNDUH':
            file=open(input_message[6:],'wb')
            ftp.retrlines('RETR '+ input_message[6:], file)
            print 'Berhasil unduh'
        elif input_message[0:6]=='UPLOAD':
            file=open(input_message[7:],'rb')
            ftp.storlines('STOR '+ input_message[7:], file)
            print 'Berhasil unggah'


except Exception, e:
    print "username atau password salah"
    sys.exit(1)