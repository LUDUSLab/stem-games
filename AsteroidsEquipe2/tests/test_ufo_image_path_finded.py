from os import path
import ufo

def test_ufo_image_path_finded():
    bigufo = ufo.BigUFO((1, 0))
    assert path.exists(bigufo.sprite_path)
