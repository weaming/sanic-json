.PHONY: test build install publish

# the library name
name = sanic-json
# pip version
pip = pip3

clean:
	rm -fr build dist *.egg-info

build: clean
	python setup.py bdist_wheel --universal

install: build
	$(pip) install --force-reinstall ./dist/*.whl

publish: install
	twine upload dist/* && git push --follow-tags

uninstall:
	pip uninstall $(name) -y
	pip3 uninstall $(name) -y
