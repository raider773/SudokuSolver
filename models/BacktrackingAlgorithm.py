from utils import ValidateNumber,ValidateRow,ValidateColumn,Validate_box,solucion

def backtrackingSudoku (vector,vectorO,step,soluciones): 
    "Backtracking Algorithm for solving Sudoku Puzzzle given a Sudoku vector"
    if ValidateNumber(step,vector) == False:
        backtrackingSudoku (vector,vectorO,step + 1,soluciones)
    elif ValidateNumber(step,vector) == True:     
        for i in range (1,10):        
            if ValidateRow(i,step,vector) and  ValidateColumn(i,step,vector) and Validate_box(i,step,vector):
                vector[step] = i                
                if 0 not in vector:                   
                    if solucion(vector):                        
                        soluciones.append(vector.copy())
                else:
                    backtrackingSudoku (vector,vectorO,step + 1,soluciones)                               
                vector[step] = 0