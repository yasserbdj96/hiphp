# EXAMPLES :
# EXAMPLES :
#s
from hiphp import hiphp

# Example:1
# CLI:
hiphp("123","https://localhost/index.php").run()

# Example:2
# Command:
hiphp("123","https://localhost/index.php",False,False).run("-c echo 'hi';")

# Example:3
# Command:
p1=hiphp("123","https://localhost/index.php",True,False).run("-c echo 'hi';")
print(p1)

# Example:4
#-example_4.php content:
'''<?php
    $fp=fopen("test.txt","w+");
    Fwrite($fp,"this is a test");//Writing inside the file
?>'''
# File:
hiphp("123","https://localhost/index.php",False,False).run("example_4.php")

# Example:5
#-example_5.txt content:
'''// prints something like: Wednesday the 15th
    echo date('l \t\h\e jS');'''
# File:
p1=hiphp("123","https://localhost/index.php",True,False).run("example_5.txt")
print(p1)
#e
# EXAMPLES :
#s
from hiphp import hiphp

# Example:1
# CLI:
hiphp("123","https://localhost/index.php").run()

# Example:2
# Command:
hiphp("123","https://localhost/index.php",False,False).run("-c echo 'hi';")

# Example:3
# Command:
p1=hiphp("123","https://localhost/index.php",True,False).run("-c echo 'hi';")
print(p1)

# Example:4
#-example_4.php content:
'''<?php
    $fp=fopen("test.txt","w+");
    Fwrite($fp,"this is a test");//Writing inside the file
?>'''
# File:
hiphp("123","https://localhost/index.php",False,False).run("example_4.php")

# Example:5
#-example_5.txt content:
'''// prints something like: Wednesday the 15th
    echo date('l \t\h\e jS');'''
# File:
p1=hiphp("123","https://localhost/index.php",True,False).run("example_5.txt")
print(p1)
#e
