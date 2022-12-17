#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

#
ifeq ($(OS),Windows_NT) 
    detected_OS := Windows
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif

ifeq ($(detected_OS),Windows)
    pipforos = $(PIP) install -r ./hiphp-win/requirements-win.txt
endif
	
ifeq ($(detected_OS),Linux)#Darwin for Mac OS X
    pipforos = $(PIP) install -r ./hiphp-linux/requirements-linux.txt
endif

#
ifeq ($(arg),cli)
	RUN = $(PYTHON) run.py $(key) $(url)
else
	ifeq ($(arg),tk)
		RUN = $(PYTHON) hiphp-tk/main.py $(key) $(url)
	else
		ifeq ($(arg),dst)
			RUN = $(PYTHON) hiphp-desktop/main.py
		else
			RUN = $(info USAGE: make run arg='cli/dst/tk' url='URL' key='KEY')
		endif
	endif
endif

run: $(VENV)/bin/activate
	$(RUN)

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r ./requirements.txt
	$(PIP) install -r ./requirements-pypi.txt
	$(PIP) install -r ./hiphp-desktop/requirements-dst.txt
	$(PIP) install -r ./hiphp-tk/requirements-tk.txt
	$(pipforos)

clean:
	rm -rf hiphp/__pycache__
	rm -rf $(VENV)
#}END.