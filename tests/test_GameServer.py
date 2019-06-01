import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir, "pyGameServer"))
import GameServer as GS

def test_IF_EXISTS():
    instance = GS.GameServer()
    assert instance is not None
    
def test_HAS_FUNC_TEST():
    instance = GS.GameServer()
    instance.test()
