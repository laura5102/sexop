import paramiko

t = paramiko.Transport(('',22))
t.connect(username="", password="")
sftp = paramiko.SFTPClient.from_transport(t)
remote_path = '/usr/local/openresty/nginx/conf/nginx.conf'
local_path = 'F:/71_nginx.conf'
sftp.get(remote_path,local_path)
t.close()