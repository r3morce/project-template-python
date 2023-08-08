#/bin/bash
source venv/bin/activate
isort . &> /dev/null
black . &> /dev/null
python3 main.py # --debug
