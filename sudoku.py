from typing import Dict

import collections
import numpy as np
wrk_pos=dict()
kn_lst=[1,2,3,4,5,6,7,8,9]
kn_lst_2=np.array([["a","b","c"],["d","e","f"],["g","h","i"]])
kn_lst_3=["a","b","c","d","e","f","g","h","i"]

def func_input():
    
    my_sudoku_2=np.zeros((9,9), dtype=int)
    print(my_sudoku_2)
    for i in range(9):
        for j in range (9):
            x="s"
            while type(x) != int or len(str(x))!=1:
                try:
                    print(i,j)
                    x=int(input("ingrese sus valores \n"))
                    print(type(x))
                    #y=(input("usted ingreso {} , es correcto?(y/n)\n".format(x)))
                    #if y=="n" or y == "no":
                    #    x="s"
                except ValueError:
                    print("not the right number")
            my_sudoku_2[i,j]=x
            print(my_sudoku_2)
            if i==8 and j==8:
                func(my_sudoku_2)


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
####################################################################
#                  me dal a familia de letras en la que esta la coordenada
######################################################################
def func_abc(dict,i,j):
    x=str(i)+str(j)
    for name,val in dict.items():
        if x in name:
            return(name[0])

def func_abc2(dict,nm,value):
    for name,val in dict.items():
        if nm[0] in name:
            return(name[0])       


def func_sqr(dict,i,j):
    k=[]
    name_sqr=func_abc(dict,i,j)
    for name,val in dict.items():
        if name.startswith(name_sqr):
            if type(val)!=list and val!=0:
                k.append(val)
            else:
                continue
    return(k)
#Une todos los valores que no puede tomar una casilla en una lista y la devuelva
def vals_cn_tk(x):
    final_values = set(x)
    pos_val=list(set(kn_lst)-final_values)
    return(pos_val)


############################################
# 
#               Finders
####################################
def fnd_kn_val_x(sudoku,sudoku_row,sudoku_clmn,dict,i,j):
    n=[]

    for val in sudoku_row:
        if val != 0 :
            n.append(val)


    for val in sudoku_clmn:
        if val != 0 :
            n.append(val)

    sub_sqr=func_sqr(dict,i,j)
    for val in sub_sqr:
        if val!=0:
            n.append(val)
    
    return(n)

def count_last_chk(lst):
    for i in lst:
        count=0
        for j in range(len(lst)):
            if i == lst[j]:
                count+=1
        if count==1:
            print(i,"es un valor no repetido")
            return(i)
            


def only_one_option_in_family(dict,sudoku):
    for i in kn_lst_3:
        summ=[]
        for name,val in dict.items():
            if i in name and type(val)==list:
                summ+=dict[name]
        print("para la familia",i,"summ es",summ)
        x=count_last_chk(summ)
        for name,val in dict.items():
            if i in name and type(val)==list and x in val:
                dict.update({name : x})
                print(name,"value updated with",x)
                put_val(dict,sudoku)

def same_pos_and_val(dict):
    for ch in kn_lst_3:
        name_random=[]
        for name,val in dict.items():
            if name.startswith(ch) and type(val)==list:
                name_random.append(name)
                print(name,val)

        print(name_random)
        for n in name_random:
            list_random=[n]
            for i in range(len(name_random)):
                if dict[n]==dict[name_random[i]] and i>name_random.index(n) and i not in list_random:
                        list_random.append(name_random[i])
            if len(list_random)>1:    
                print("listas iguales",list_random)
            if len(list_random)==len(dict[n]):
                print("hay la misma cantidad de listas que de valores para",list_random,dict[n],n)
                for names in name_random:
                    if names not in list_random:
                        for val in dict[n]:
                            if val in dict[names]:
                                dict[names].remove(val)
                                print(val,"fue removido de ",names,dict[names])
    put_val(dict,my_sudoku)


def ghst_values_x(sudoku_row,dict,i,j,lst_ghst,family):
    sum=-1
    
    for value in sudoku_row:
        sum+=1
        numbers=str(i)+str(sum)
        for name in dict.keys():
           if numbers in name and value==0 and type(dict[name])==list and family not in name:
                for ghst in lst_ghst:
                    if ghst in dict[name]:
                        print(name,dict[name])
                        print(ghst,"es un ghst y fue removido de",name)
                        (dict[name]).remove(ghst)
                        print(name,dict[name])
    
def ghst_values_y(sudoku_colmn,dict,i,j,lst_ghst,family):    
    sum=-1
    for value in sudoku_colmn:
        sum+=1
        numbers=str(sum)+str(j)
        for name in dict.keys():
           if numbers in name and value==0 and type(dict[name])==list and family not in name:
                for ghst in lst_ghst:
                    if ghst in dict[name]:
                        print(name,dict[name])
                        print(ghst,"es un ghst y fue removido de",name)
                       
                        (dict[name]).remove(ghst)
                        print(name,wrk_pos)



 

 
                   
def ghst_values_chk(sudoku,dict,i,j):
    
    ghst_lst_x=[]
    ghst_name_x=[]
    ghst_lst_y=[]
    ghst_name_y=[]
    family_items=[]
    family=func_abc(dict,i,j)
    x=(family+str(i)+str(j))
    print("working with",x)
    for name,lst in dict.items():
        if name==x:
            continue

        elif family in name and type(lst)==list and type(dict[x])==list and len(lst)>1:
                family_items.append(name)
                
                if name[1]==str(i):
                    print(name,"same row")
                    for value in lst:
                        if value in dict[x] and value not in ghst_lst_x:
                            print(name,"agrego",value,"a ghst_x")
                            ghst_lst_x.append(value)
                            if name not in ghst_lst_x:
                                ghst_name_x.append(name)
                     
                        
                if name[2]==str(j):
                    
                    print(name,"same column")
                    for value in lst:
                        if value in dict[x] and value not in ghst_lst_y:
                            print(name,"agrego",value,"a ghs_y")
                            ghst_lst_y.append(value)
                            if name not in ghst_lst_y:
                                ghst_name_y.append(name)
                    
                
                                  
    print(ghst_name_x,ghst_name_y)
    print("family with list as values",family_items)
    values_to_remv=[]
    
    for val in ghst_lst_x:
        if val in ghst_lst_y and val not in values_to_remv:
            values_to_remv.append(val)
        else:
            continue
    for values in values_to_remv:
        print(values,"se encuentra tanto en la fila como en la columna de",x,"no puede ser un ghst")
        ghst_lst_x.remove(values)
        ghst_lst_y.remove(values)

    
    if len(ghst_lst_x)==0 and len(ghst_lst_y)==0:
        print("no ghst found")
        return
    for nm in family_items:
        
        if nm in ghst_name_x or nm in ghst_name_y:
            continue
        else:   
            for val in dict[nm]:
                print(nm,val)
                try:
                    if val in ghst_lst_x:
                        print("en",nm,val,"no es un ghst")
                        ghst_lst_x.remove(val)
                        print(val,"ah sido removido de la lista ghst")
                        print(ghst_lst_x)
                    if val in ghst_lst_y:
                        print("en",nm,val,"no es un ghst")
                        ghst_lst_y.remove(val)
                        print(val,"ah sido removido de la lista ghst")
                        print(ghst_lst_y)
                except:
                    continue
        
    if len(ghst_lst_x)!=0:
        print("final list of ghst_x for ",x,ghst_lst_x)
        ghst_values_x(sudoku[i],dict,i,j,ghst_lst_x,family)
    if len(ghst_lst_y)!=0:
        print("final list of ghst_y for ",x,ghst_lst_y)
        ghst_values_y(sudoku[:,j],dict,i,j,ghst_lst_y,family)

     
               
                    #print(val,"esta",count,"veces en la fila",i,"en las posiciones",l)
                    



########################################################
# 
#           Principal 
# ###################################################  

def func(sudoku,chg):
    i=-1
    j=-1
    if len(wrk_pos)<81:
        for row in kn_lst_2:   
            for h in range(3):
                i+=1
                for ch in row:
                    for k in range(3):
                        j+=1
                        if j==9:
                            j=0
                        
                        print("yes")
                        wrk_pos.update({"{}{}".format((ch),str(i)+str(j)) : 0})
                    
                        if sudoku[i,j]!=0:
                                wrk_pos.update({"{}{}".format((ch),str(i)+str(j)) : (sudoku[i][j])})
    
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                x=fnd_kn_val_x(sudoku,sudoku[i],sudoku[:,j],wrk_pos,i,j)      #ok
                pos_val=vals_cn_tk(x)
                #print("coord",i,j,"values",pos_val)
                for name,val in wrk_pos.items():
                    if (str(i)+str(j)) in name:
                        #print(name)
                        wrk_pos.update({name : pos_val})
    
            

    put_val(wrk_pos,sudoku)
    
#############################hasta aca funciona y me agrega los posibles valores en x para cada lugar en x               
###################################################
#
#               chequeador de trabajo
#################################################
def sudoku_complete(sudoku_complete):
    if 0 in sudoku_complete:
       print("f")
       print(sudoku_complete)
        
    else:
        print("bien")
        print(sudoku_complete)

#######################################################################
##                                                                    #
##                        Trabajo con diccionario                     #
#######################################################################
def put_val(dict,sudoku):
    for name, val in dict.items():
        if type(val)==list and len(val)==1:
            for i in val:     #ok
                dict[name]=i
                print(name,":",i)
                ch=func_abc2(dict,name,val)
                for nm, value in dict.items():
                    if ch in nm and type(value)==list and len(value)>1:
                        print("prog",nm,value)
                        try:
                            value.remove(i)
                            print(nm,value)
                        except:
                            continue
                    else:
                        continue

            
    only_one_option_in_family(dict,sudoku)
    print(wrk_pos)
       
    frm_dict_to_mtrx(wrk_pos,sudoku)


def frm_dict_to_mtrx(dict,sudoku):
    
    for i in range(9):
        for j in range(9):
            family=func_abc(dict,i,j)
            num=str(i)+str(j)
            f_n=family+num
            if sudoku[i,j]==0 and type(dict[f_n])!=list:
                
                sudoku[i,j]=dict[f_n]
                print(f_n,"es",sudoku[i,j])
            else:
                continue
        
    sudoku_complete(sudoku)
func(my_sudoku,0)
func(my_sudoku,0)

func(my_sudoku,0)

func(my_sudoku,0)
func(my_sudoku,0)
func(my_sudoku,0)
func(my_sudoku,0)
func(my_sudoku,0)
func(my_sudoku,0)
func(my_sudoku,0)





def ciclo_resolucion(sudoku,dict):
    for i in range(9):
        for j in range(9):
            if sudoku[i,j]==0:
                ghst_values_chk(sudoku,dict,i,j)   
            only_one_option_in_family(dict,sudoku)
    same_pos_and_val(dict)
    put_val(dict,sudoku)



ciclo_resolucion(my_sudoku,wrk_pos)
func(my_sudoku,1)
ciclo_resolucion(my_sudoku,wrk_pos)
func(my_sudoku,0)
ciclo_resolucion(my_sudoku,wrk_pos)
func(my_sudoku,1)
ciclo_resolucion(my_sudoku,wrk_pos)
func(my_sudoku,0)
ciclo_resolucion(my_sudoku,wrk_pos)
func(my_sudoku,1)
