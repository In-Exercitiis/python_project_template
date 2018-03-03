'''Template test.

'''


import pytest
import template_project


def test_cli():
    assert template_project.__main__.script_fn() == 1
    pytest.raises(Exception, template_project.__main__.script_fn, 'thing')
