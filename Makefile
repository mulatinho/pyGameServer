#
# A simple python game server
# Alexandre Mulatinho @ 2019
#

init:
	pip install -r requirements.txt

test:
	py.test -v

clean:
	find . -name '*~' -exec rm -rfv '{}' \+
	find . -name '*pyc' -exec rm -rfv '{}' \+
	find . -name '__pycache__' -exec rm -rfv '{}' \+
	find . -name '.pytest_cache' -exec rm -rfv '{}' \+
