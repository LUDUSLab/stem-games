import config
def test_window_initialization():
    assert str(type(config.window)) == "<class 'window.Window'>"
