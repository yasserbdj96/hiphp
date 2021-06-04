# USAGE :
#s
from hiphp import hiphp

p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>")
print(p1.get_code())//Get HIPHP ID for first use.
p1.run("<YOUR_CODE>")//Run a code or line in your website.
p1.run_file("<PHP_CODE_FILE_PATH>")//Run a code or line in your website from a file.
p1.run_file("<PHP_CODE_FILE_PATH>","<__VALUE_NAME__>==<VALUE_CONTENT>")//Run a code or line in your website from a file With the entry of variables.
p1.cli()//open command panel
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>")//Upload a file to the server hosting the site.
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>","./<THE_PATH_YOU_WANT_TO_UPLOAD_THE_FILE_TO>")
#e
