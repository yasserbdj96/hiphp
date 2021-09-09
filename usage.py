#call the package:
from hiphp import hiphp
#
#
#In order to print the result directly.
p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>",False)
#
#In order to make the result as a variable.
#p1=hiphp("<PASSWORD>","<http://THE/LINK/TO/THE/PHP/FILE/THAT/CONTAINS/THE/HIPHP/ID>")
#
#
#Get HIPHP ID for first use.
print(p1.get_code())
#
#
#Run a code or line in your website.
p1.run("<YOUR_CODE>")
#
#Run a code or line in your website from a file.
p1.run_file("<PHP_CODE_FILE_PATH>")
#
#Run a code or line in your website from a file With the entry of variables.
p1.run_file("<PHP_CODE_FILE_PATH>","<__VALUE_NAME__>==<VALUE_CONTENT>")
#
#
#open command line interface.
p1.cli()
#
#
#Upload a file to the server hosting the site.
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>")
#
#Upload a file to a specific folder in the server hosting the site.
p1.upload("<THE_PATH_OF_THE_FILE_TO_BE_UPLOADED>","./<THE_PATH_YOU_WANT_TO_UPLOAD_THE_FILE_TO>") 
