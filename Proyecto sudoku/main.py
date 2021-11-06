import numpy as np
from functions import *

wrk_pos=dict()



my_sudoku=np.array([[0,0,0, 2,0,9, 0,6,0],
                    [5,0,7, 6,0,0, 0,0,0],
                    [0,0,4, 0,0,0, 0,1,0],

                    [8,0,0, 0,7,0, 0,5,0],
                    [3,0,0, 0,0,0, 9,0,0],
                    [0,9,0, 8,0,3, 0,0,0],

                    [0,0,0, 3,8,6 ,0,7,0],
                    [0,0,1, 0,0,0, 3,0,2],
                    [0,0,8, 0,2,0, 0,0,0]])            


               
                  
dictionary(my_sudoku,wrk_pos) #inicia el diccionario


        

                    
#============================MAIN===========================#

def func(sudoku,dict):          
          #iniciamos el diccionario

    val_x_y_sqr(sudoku,dict)
    put_val(dict,sudoku)
    only_one_option_in_family(dict,sudoku)

def fun(sudoku_old,sudoku_new):
    while True:
        if not np.array_equiv(sudoku_old, sudoku_new):
            sudoku_old=sudoku_new.copy()
            func(sudoku_new,wrk_pos)
            
            
        else:    
            print("bien, se acabaron los valores faciles")
            break
    


def ciclo_resolucion(sudoku,dict):
    for i in range(9):
        for j in range(9):
            if sudoku[i,j]==0:
                ghst_values_chk(sudoku,dict,i,j)   
            only_one_option_in_family(dict,sudoku)
    same_pos_and_val(dict)
    put_val(dict,sudoku)


while 0 in my_sudoku:
    fun(sudoku_compare,my_sudoku)
    ciclo_resolucion(my_sudoku,wrk_pos)

print(my_sudoku)


      

    
           















