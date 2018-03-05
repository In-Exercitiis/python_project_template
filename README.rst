Python Project Template
=======================

Simple python project template.

What to replace
===============

in src/template_project/ - rename to correct project name

if the project has console scripts, in
src/template_project/__about__.py - replace
'some_consle_script=template_project.__main__:script_fn' with the
appropriate names for some_consle_script, template_project and
script_fn or if there are no consol_scripts, just assign
__entry_points__ an empty dict '{}'

in src/template_project/__about__.py - replace __package_name__ =
'template_project' with correct project name

in tests/test_cli_script.py - replace completely with correct test file


Install
=======

Install with pip::

  sudo -H pip install /path/to/python_project_template

Remove
======

Remove with pip::

  # __package_name__ in __about__.py defines the project name 'template_project'
  sudo -H pip uninstall template_project

Run tests
=========

Use pytest.
