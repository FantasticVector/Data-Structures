from tabnanny import check
import numpy as np
def validate_battlefield(field):
    def checker(ship, field):
        b = 0
        for i in range(field.shape[0] - ship.shape[0]+1):
            for j in range(field.shape[1] - ship.shape[1]+1):
                b+= np.all(field[i:(i+ship.shape[0]), j:(j+ship.shape[1])] == ship) 
        return b
    field = np.pad(np.array(field, dtype=int), 1, mode='constant')
    battleship = np.array([[0,0,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]], dtype=int)
    cruisers = np.array([[0,0,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]], dtype=int)
    destroyers = np.array([[0,0,0],[0,1,0],[0,1,0],[0,0,0]], dtype=int)
    submarines = np.array([[0,0,0],[0,1,0],[0,0,0]], dtype=int)
    ans = {'b':0, 'c':0, 'd':0, 's':0}
    for i in [battleship, cruisers, destroyers, submarines, battleship.T, cruisers.T, destroyers.T]:
        x = checker(i, field)
        if np.array_equal(i, battleship) or np.array_equal(i, battleship.T): ans['b'] += x
        if np.array_equal(i, cruisers) or np.array_equal(i, cruisers.T): ans['c'] += x
        if np.array_equal(i, destroyers) or np.array_equal(i, destroyers.T): ans['d'] += x
        if np.array_equal(i, submarines): ans['s'] += x
    print(checker(destroyers, field))
    print(ans)
    print(field)
    #return ans == {'b': 1, 'c': 2, 'd': 3, 's': 4}

battleField = [[0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]

validate_battlefield(battleField)