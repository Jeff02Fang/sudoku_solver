import cv2
import pytesseract ####
import numpy as np

#引入圖片 裁切 黑白化
def image_process(file_name):

    #file_name = r'images\screen2.jpg' #######自己找張圖
    img = cv2.imread(file_name)

    img = cv2.resize(img, (630,630))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for x in range(630):
        for y in range(630):
            if img[x][y] < 190:
                img[x][y] = 0
            else:
                img[x][y] = 255

    return img

#找到數字所在位置
def find_locations(img):
    locations = []
    for i in range(9):
        for j in range(9):
            width = i * 70 + 10
            height = j * 70 + 10
            black = 0
            for x in range(height,height+50):
                for y in range(width,width+50):
                    if img[x][y] < 255:
                        black += 1
            if black > 100:
                tmp = []
                tmp.append(j)
                tmp.append(i)
                locations.append(tmp)

    locations = sorted(locations)    

    return locations

#輸出只有數字的圖片
def image_of_numbers(img,locations):
    new_img = np.copy(img)
    for pos in range(len(locations)):
        x = locations[pos][0] * 70
        y = locations[pos][1] * 70
        tmp = new_img[x+10:x+60,y+20:y+50]
        if pos == 0:
            num = np.copy(tmp)
        else:
            num = np.hstack((num,tmp))

    strnum_file_route = r'digit_images\string_img.jpg'
    cv2.imwrite(strnum_file_route, num)
    return strnum_file_route

#輸出經由pytessercat轉換來的字串
def string_of_numbers(strnum_file_route):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #####套件要下載
    num_string = pytesseract.image_to_string(strnum_file_route)
    num_string = num_string.strip().replace(' ','')

    return num_string

#生成數獨陣列
def create_sudoku(locations, num_string):
    sudoku = np.zeros((9,9))

    for pos in range(len(locations)):
        i = locations[pos][0]
        j = locations[pos][1]
        sudoku[i][j] = int(num_string[pos])

    return sudoku

#main
def recognition(file_route):
    img = image_process(file_route)
    locations = find_locations(img)
    strnum_file_route = image_of_numbers(img,locations)
    num_string = string_of_numbers(strnum_file_route)
    sudoku = create_sudoku(locations, num_string)
    
    return sudoku