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

run: $(VENV)/bin/activate
#
	$(PYTHON) run.py
# \
	$(PYTHON) hiphp-desktop/main.py
# \
	$(PYTHON) hiphp-tk/main.py


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r ./requirements.txt
	$(PIP) install -r ./requirements-pypi.txt
	$(PIP) install -r ./hiphp-desktop/requirements-dst.txt
	$(PIP) install -r ./hiphp-tk/requirements-tk.txt
	$(PIP) install -r ./requirements-linux.txt

clean:
	rm -rf hiphp/__pycache__
	rm -rf $(VENV)
#}END.