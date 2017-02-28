import sys
from nose.tools import *
from grid import file_exists
from grid import grid_in_range
from grid import instructions_within_grid
from _operator import and_

def test_file_exists():
    import os.path
    os.path.exists(file_path)
    ok_()
    
def test_grid_in_range(filename,n,x, y):
    grid = open(filename).read()
    for line in grid.split('\n'):
        if (row <=x and col <= y):
        ok_()

def test_instructions_within_grid(x,y,a,b):
    for i in range(x):
        for j in range(y):
            if(i, j)<=(a,b):
                ok_()
    