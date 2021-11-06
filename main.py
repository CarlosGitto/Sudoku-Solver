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
                    [0,0,8, 0,2,0, 0,0,0]])             #sudoku[8]
my_sudoku_trasp=(my_sudoku.transpose())

               
                    #print(val,"esta",count,"veces en la fila",i,"en las posiciones",l)
dictionary(my_sudoku,wrk_pos)
#################################################
#           Sabe el estado del sudoku           #
#                                               #
#################################################


        

                    
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


      

    
           




#######################################################################
##                                                                    #
##                        Trabajo con diccionario                     #
#######################################################################

                
            
  # only_one_option_in_family(dict,sudoku)
   # print(wrk_pos)
       
    #frm_dict_to_mtrx(wrk_pos,sudoku)


"""  def frm_dict_to_mtrx(dict,sudoku):
        
        for i in range(9):
            for j in range(9):
                family=func_abc(dict,i,j)
                num=str(i)+str(j)
                full_name=family+num
                if sudoku[i,j]==0 and type(dict[full_name])!=list:
                    
                    sudoku[i,j]=dict[full_name]
                    print(full_name,"es",sudoku[i,j])
                else:
                    continue
            
        sudoku_complete(sudoku)"""









"""Estructura que quiero tener:
1 funcion que acomode el diccionario en primer lugar y defina los falores faciles,
cuando no haya mas valores faciles, chequee que no este resuelto y luego vaya a los dificiles hasta resolverlo
siemrpe tiene que  haber una funcion actualizando el dict y los valores resueltos(put_val)"""
