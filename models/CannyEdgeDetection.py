import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pickle

def DetectEdge(path,thr1,thr2):
    "Apllies CannyEdgeDetection and returns original image and coordinates of edges"
    img = cv.imread(path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #Use Canny Edge Detection Algorithm
    edged = cv.Canny(img_gray, thr1, thr2)
    #get contours from the edged image
    contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, 
                               cv.CHAIN_APPROX_SIMPLE)
    return img,contours



def crop_image(img,contours):
    "returns an image with only the sudoku board"
    img_out = img.copy()
    w, h = img.shape[1], img.shape[0]
    for cntr in contours:
        imgx, imgy, imgw, imgh = cv.boundingRect(cntr)
        if imgw < w/5 or imgw < h/5 or imgw/imgh < 0.25 or imgw/imgh > 1.5:
            continue
      # Approximate the contour with 4 points
        peri = cv.arcLength(cntr, True)
        frm = cv.approxPolyDP(cntr, 0.1*peri, True)
        if len(frm) != 4:
            continue

      # Converted image should fit into the original size
        board_size = max(imgw, imgh)
        if imgx + board_size >= w or imgy + board_size >= h:
            continue
      # Points should not be too close to each other 
      # (use euclidian distance)
        if cv.norm(frm[0][0] - frm[1][0], cv.NORM_L2) < 0.1*peri or \
            cv.norm(frm[2][0] - frm[1][0], cv.NORM_L2) < 0.1*peri or \
            cv.norm(frm[3][0] - frm[1][0], cv.NORM_L2) < 0.1*peri or \
            cv.norm(frm[3][0] - frm[2][0], cv.NORM_L2) < 0.1*peri:
            continue
            
    #crop image based on points
        
    croped_image = img_out[frm[0][0][1]:frm[1][0][1],frm[1][0][0]:frm[2][0][1]]
    croped_image = cv.cvtColor(croped_image, cv.COLOR_BGR2GRAY)
    
    return croped_image


def get_digits_image(croped_image):
    'divides cropped image in 81 individual iamges and returns them. Each iamge is a digit'
    images = []
    cell_w, cell_h = croped_image.shape[1]//9,croped_image.shape[0]//9
    for x in range(9):
        for y in range(9):
            x1, y1 = x*cell_w, y*cell_h 
            x2, y2 = (x + 1)*cell_w, (y + 1)*cell_h
            cx, cy = (x1 + x2)//2, (y1 + y2)//2 
            w2, h2 = cell_w, cell_h

            #add + 10 and -5 for better cropping
            crop = croped_image[y1+10:y2-5, x1+10:x2-5]
            images.append(np.concatenate((np.expand_dims(crop, axis = 2),np.expand_dims(crop, axis = 2),np.expand_dims(crop, axis = 2)),axis = 2)) 
    return images


def CannyEdgeDetection(path,thr1,thr2):
    "Divides Sudoku image into 81 digit images"
    img,edges = DetectEdge(path,thr1,thr2)
    croped_image = crop_image(img,edges)
    digits = get_digits_image(croped_image)      
    return (np.array(digits))


    