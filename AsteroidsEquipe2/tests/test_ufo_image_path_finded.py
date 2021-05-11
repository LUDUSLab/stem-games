from os import path
import ufo

def test_ufo_image_path_finded():
    bigufo = ufo.BigUFO(200, 1)
    assert path.exists(bigufo.sprite_path)
