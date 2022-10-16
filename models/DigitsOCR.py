import cv2 as cv
import easyocr
import pickle
import os

reader = easyocr.Reader(['en','en'])

def get_digits(images):   
    "get digit as string from images list and append them as integers into another list using an OCR"
    digits = []
    SudokuVector = []
    for i in range (81):
        print(f"Getting digit {i + 1} of 81")        
        up_width = 400
        up_height = 400
        up_points = (up_width, up_height)
        resized_up = cv.resize(images[i], up_points, interpolation= cv.INTER_LINEAR)
        cv.imwrite("ActualPicture.JPG",resized_up)
        #Use OCR to extract digit from digit image
        result = reader.readtext('ActualPicture.JPG')
               
        
        
        if len(result)> 0:
            digits.append(int(result[0][1]))
        else:
            digits.append(0)
            
    #remove temporary JPG        
            
    os.remove("ActualPicture.JPG")
    
    #transform digits list to the sudoku vector for backtracking algorithm
    
    for i in range (9):
        for j in range (9):
            SudokuVector.append(digits[(j * 9) + i])
    
    return SudokuVector
            
    
            
    