from rupyks import Cube

def test_initial_state():
    cube = Cube()
    assert cube.check() == True, 'New cube should be solved'

def test_shuffle_state():
    cube = Cube()
    cube.shuffle()
    assert cube.check() == False, 'Shuffled cube should not be solved'

if __name__ == '__main__':
    test_initial_state()
    test_shuffle_state()
    print('Everything passed')