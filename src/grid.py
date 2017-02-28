import urllib.request
import argparse

def create_grid(N):
    a2d = [ [0]*N for _ in range(N) ]
    return print(a2d)
  
def read_file(fname):
    if fname.startswith('http'):
        req= urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
            else:
        filename = ".txt"
        with open(filename) as f:
            for line in f.readlines():      
                values = line.strip().split()
                return values

def lights_on(x,y,grid):
    for i in range(x):
        for j in range(y):
        if(i, j, grid[i][j]) = False
            return (i, j, grid[i][j]) = True
    
def lights_off(x,y,grid):
    for i in range(x):
        for j in range(y):
        if(i, j, grid[i][j]) = True
            return (i, j, grid[i][j]) = False

def switch_lights(x,y,grid):
    for i in range(x):
        for j in range(y):
        if(i, j, grid[i][j]) = True
            return (i, j, grid[i][j]) = False
        else
            return (i, j, grid[i][j]) = True