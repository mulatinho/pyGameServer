import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir, "security"))
import security as SEC

def test_IF_KEY_IS_CREATE():
    instance = SEC.Security()
    instance.pk_new_key()

def test_IF_KEY_IS_A_FILE():
    return 0
