import paramiko

t = paramiko.Transport(('',22))
t.connect(username="", password="")
sftp = paramiko.SFTPClient.from_transport(t)
remote_path = '/tmp/SecooMobile_program'
local_path = '/tmp/'
sftp.get(remote_path,local_path)
t.close()
