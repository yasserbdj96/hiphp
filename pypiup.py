#import os
import pexpect
import sys
#import shutil

try:
    user=sys.argv[1]
    passw=sys.argv[2]

except:
    print(f"USAGE : python3 {sys.argv[0]} <USER> <PASSWORD>")
    exit()

#os.chdir(path)

child=pexpect.spawn("python setup.py sdist bdist_wheel")
#child.before
child.interact()
#print(child.read().decode("utf-8"))
child.kill(0)

child=pexpect.spawn("python -m twine upload dist/*")
#child.before
child.expect('Enter your username: ')
child.sendline(user)
child.expect('Enter your password: ')
child.sendline(passw)
#print(child.read().decode("utf-8"))
child.interact()
child.kill(0)

#rmv=["build","dist",path+".egg-info"]

#try:
#    for i in range(len(rmv)):
#        shutil.rmtree(rmv[i])
#except OSError as e:
#    print("Error: %s - %s." % (e.filename, e.strerror))
