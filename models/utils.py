def get_matrix(vector):
    "Transform vector into Sudoku Matrix"
    pre = 0
    matrix = []
    for i in range(3,82,3):    
        matrix.append(vector[pre:i])   
        pre = i
    return matrix

def multiples(m, count):
    "Get count multiples from m"
    multiples = []
    for i in range(0,count*m,m):
        multiples.append(i)
    return multiples


def printSudoku(vector):
    "Print sudoku vector as a sudoku board"
    matrix =  get_matrix(vector)
    multiplesOf3= multiples(3,10)
    count = 0
    for i in multiplesOf3[:-1]:
        pre = i
        if (count) % 3 == 0:
            print("-"* 33)
        print(matrix[pre], "|", matrix[pre+1],"|", matrix[pre+2])   
        count += 1
    print("-"* 33)
    
    
def ValidateNumber(step,vector):
    "Validates if cell is available to fill"
    result = True  
    if vector[step] != 0:
        result = False   
    return result
        
        


def ValidateRow(number,step,vector):
    "Validates if x number in y step is valid row wise"
    pre = 0
    result = True
    for i in multiples(9,10):
        if step > pre and step < i:              
            if number in vector[pre:i]:
                result = False                   
        pre = i
    return result


def ValidateColumn(number,step,vector):  
    "Validates if x number in y step is valid column wise"
    result = True
    for i in multiples(9,9):
        if number == vector[step - i]:
            result = False
    return result
        

def get_cuadrants(vector):
    "get vectors of each of the nine cuadrants"
    cuadrantes = {}
    cont = 1
    for i in multiples(27,3):

        indice = i
        indice2 = i + 3
        indice3 = i + 6
        cuad = [vector[indice],vector[indice+1],vector[indice+2],
         vector[indice + 9],vector[indice+10],vector[indice+11],
         vector[indice + 18],vector[indice+19],vector[indice+20]
        ]

        cuadrantes[f"cuadrante_{cont}"] = [cuad,
        [indice,indice+1,indice+2,indice+9,indice+10,indice+11,indice+18,indice+19,indice+20]]

        cuad2 = [vector[indice2],vector[indice2+1],vector[indice2+2],
         vector[indice2 + 9],vector[indice2+10],vector[indice2+11],
         vector[indice2 + 18],vector[indice2+19],vector[indice2+20]
        ]

        cuadrantes[f"cuadrante_{cont+1}"] = [cuad2,
        [indice2,indice2+1,indice2+2,indice2+9,indice2+10,indice2+11,indice2+18,indice2+19,indice2+20]]

        cuad3 = [vector[indice3],vector[indice3+1],vector[indice3+2],
         vector[indice3 + 9],vector[indice3+10],vector[indice3+11],
         vector[indice3 + 18],vector[indice3+19],vector[indice3+20]
        ]    

        cuadrantes[f"cuadrante_{cont+2}"] = [cuad3,
        [indice3,indice3+1,indice3+2,indice3+9,indice3+10,indice3+11,indice3+18,indice3+19,indice3+20]]

        cont = cont + 3
        
    return cuadrantes 

def Validate_box(number,step,vector):
    "Validates if x number in y step is valid box wise"
    resultado = True
    cuadrants = get_cuadrants(vector)    
    for i in range(1,10):
        if step in cuadrants[f"cuadrante_{i}"][1]:            
            if number in cuadrants[f"cuadrante_{i}"][0]:
                resultado = False
    return resultado


def solucion(vector):
    "Validates if sudoku vector is a valid solution"
    result = True
    for i in range(len(vector)):
        vectorreemplazar = vector.copy()
        vectorreemplazar[i] = 0
        if ValidateRow(vector[i],i,vectorreemplazar) == False or ValidateColumn(vector[i],i,vectorreemplazar) == False or Validate_box(vector[i],i,vectorreemplazar) == False:            
            result = False
    return result