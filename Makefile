#   |                                                         |   #
# --+---------------------------------------------------------+-- #
#   |    Code by: yasserbdj96                                 |   #
#   |    Email: yasser.bdj96@gmail.com                        |   #
#   |    GitHub: github.com/yasserbdj96                       |   #
#   |    Sponsor: github.com/sponsors/yasserbdj96             |   #
#   |    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      |   #
#   |                                                         |   #
#   |    All posts with #yasserbdj96                          |   #
#   |    All views are my own.                                |   #
# --+---------------------------------------------------------+-- #
#   |                                                         |   #

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
ifeq ($(filter-out $(MAKECMDGOALS),run),)
    ARGUMENTS := $(filter-out $@,$(MAKECMDGOALS))
endif


# Extract the values of specific arguments
URL := $(shell echo $(ARGUMENTS) | sed -n 's/.*\(--url\)[= ]\+\([^ ]\+\).*/\2/p')
ifeq ($(strip $(URL)),)
    URL := $(shell echo $(ARGUMENTS) | sed -n 's/.*\(--URL\)[= ]\+\([^ ]\+\).*/\2/p')
endif

KEY := $(shell echo $(ARGUMENTS) | sed -n 's/.*\(--key\)[= ]\+\([^ ]\+\).*/\2/p')
ifeq ($(strip $(KEY)),)
    KEY := $(shell echo $(ARGUMENTS) | sed -n 's/.*\(--KEY\)[= ]\+\([^ ]\+\).*/\2/p')
endif

ifeq ($(filter --TK,$(ARGUMENTS)),--TK)
	ifeq ($(strip $(URL)$(KEY)),)
    	RUN = $(PYTHON) main.py --TK
	else
		RUN = $(PYTHON) main.py --TK --KEY='$(KEY)' --URL='$(URL)'
	endif
else ifeq ($(filter --tk,$(ARGUMENTS)),--tk)
	ifeq ($(strip $(URL)$(KEY)),)
    	RUN = $(PYTHON) main.py --TK
	else
		RUN = $(PYTHON) main.py --TK --KEY='$(KEY)' --URL='$(URL)'
	endif
else ifeq ($(filter --dst,$(ARGUMENTS)),--dst)
	RUN = $(PYTHON) main.py --DST
else ifeq ($(filter --DST,$(ARGUMENTS)),--DST)
	RUN = $(PYTHON) main.py --DST
else
	ifeq ($(strip $(URL)$(KEY)),)
		$(error URL and KEY are both empty)
	else
		RUN = $(PYTHON) main.py --KEY=$(KEY) --URL=$(URL)
	endif
endif

run: $(VENV)/bin/activate
	$(RUN)

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r ./requirements.txt
	$(pipforos)

clean:
	rm -rf hiphp/__pycache__
	rm -rf $(VENV)
#}END.