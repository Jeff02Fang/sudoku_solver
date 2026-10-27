import numpy as np
import copy
import recognition_ver2

def main():
    possibility = [

               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 1 row
               
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 2 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 3 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 4 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 5 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 6 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 7 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]],# 8 row
                
               [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
                [1,2,3,4,5,6,7,8,9]]# 9 row
                
               ]

    sudoku = tensorflow_or_tesseract()

    sudoku, possibility, run_times, not_important = dont_stop_till_get_enough(sudoku, possibility,1,0)
    print(sudoku.astype(int))
    #print(possibility)
    #print(run_times)
    #print(legal_or_illegal(sudoku))

def tensorflow_or_tesseract():
    tmp = int(input("手寫還是印刷\n手寫按1\n印刷按2\n"))
    if tmp == 2:
        sudoku = from_img_get_sudoku_tesseract()
    else:
        sudoku = from_img_get_sudoku_tensorflow()
    return sudoku

def from_img_get_sudoku_tensorflow():
    img_route = input('輸入圖片路徑 (請多打1次 \\ )\n')
    sudoku = np.array()

    return sudoku

def from_img_get_sudoku_tesseract():
    img_route = input('輸入圖片路徑 (請多打1次 \\ )\n')
    sudoku = recognition_ver2.recognition(img_route)

    return sudoku

def puzzle_unsolved(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return True
    return False

#符合數獨規則回傳True
def legal_or_illegal(sudoku):
    for i in range(9):
        for j in range(9):
            row, col, blk = get_sudoku_rows_cols_blks(sudoku, i, j)
            para = 0
            for k in range(9):
                if sudoku[i][j] == row[k]:
                    para += 1
                if sudoku[i][j] == col[k]:
                    para += 1
                if sudoku[i][j] == blk[k]:
                    para += 1
            if para != 3:
                return False
    return True

def there_are_still_double_candidates(possibility):
    for i in range(9):
        for j in range(9):
            if len(possibility[i][j]) == 2:
                return True
    return False

def find_double_candidates_location(possibility):
    for i in range(9):
        for j in range(9):
            if len(possibility[i][j]) == 2:
                return i, j

#從只有2個可能的假設第一個數字去解
#如果第一個數字得到的答案正確 那回傳位置(i, j)跟這個數字
#錯誤則回傳 另一個數字
def make_some_guess(sudoku, possibility, run_times):
    i, j = find_double_candidates_location(possibility)
    guess1 = possibility[i][j][0]
    guess2 = possibility[i][j][1]
    new_sudoku = sudoku.copy()
    new_possibility = copy.deepcopy(possibility)

    new_sudoku[i][j] = guess1
    new_sudoku, new_possibility, run_times, double_consecutive_times = dont_stop_till_get_enough(new_sudoku, new_possibility, run_times, 0)
    if legal_or_illegal(new_sudoku):
        return i, j, guess1
    else:
        return i, j, guess2

def dont_stop_till_get_enough(sudoku, possibility, run_times, double_consecutive_times):
    max_run_times = 30
    pre_possibility = copy.deepcopy(possibility)
    possibility = run_the_kill(sudoku, possibility)
    sudoku, possibility = run_single_candidate(sudoku, possibility)
    #可能的數量有減少 那就繼續用single candidate去解
    if pre_possibility != possibility and run_times < max_run_times: 
        double_consecutive_times = 0
        run_times += 1
        return dont_stop_till_get_enough(sudoku, possibility, run_times, double_consecutive_times)
    #可能的數量沒有減少 也尚未完成數獨 那改用double candidates 去解
    elif puzzle_unsolved(sudoku) and run_times < max_run_times and double_consecutive_times < 3:
        double_consecutive_times += 1
        run_times += 1
        sudoku, possibility = run_double_candidates(sudoku, possibility)
        return dont_stop_till_get_enough(sudoku, possibility, run_times, double_consecutive_times)
    #如果連 double candidates 都卡關 那只好用猜的(從剩2種可能的猜1個數)
    elif puzzle_unsolved(sudoku) and run_times < max_run_times:
        double_consecutive_times = 0
        run_times += 1
        if there_are_still_double_candidates(possibility):
            i, j, confirmed_guess = make_some_guess(sudoku, possibility, run_times)
            sudoku[i][j] = confirmed_guess
            return dont_stop_till_get_enough(sudoku, possibility, run_times, double_consecutive_times)
        #print('怪怪的')

    return sudoku, possibility, run_times, double_consecutive_times

def get_sudoku_rows_cols_blks(sudoku, i, j):
    sudoku_T = np.transpose(sudoku)
    rows = sudoku[i]
    cols = sudoku_T[j]
    i = i - i % 3
    j = j - j % 3
    blks = np.array(0,int)
    for row in range(i,i+3,1):
        blks = np.append(blks,sudoku[row][j:j+3])
    blks = blks[1:]

    return rows, cols, blks

def get_possibility_rows_cols_blks(possibility, i, j):
    row_possi = possibility[i].copy()
    del row_possi[j]
    col_possi = []
    for rows in range(9):
        if rows != i:
            col_possi.append(possibility[rows][j])
    blk_possi = []
    row = i - i % 3
    col = j - j % 3
    for rows in range(row,row+3,1):
        for cols in range(col,col+3,1):
            if rows != i or cols != j:
                blk_possi.append(possibility[rows][cols])

    return row_possi, col_possi, blk_possi

def run_the_kill(sudoku, possibility):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                possibility = kill_candidates(sudoku, possibility, i, j)
            else:
                possibility[i][j] = []
    return possibility

#按照數獨上已知的結果 把不會是答案的可能性刪掉
def kill_candidates(sudoku,possibility,i,j):
    rows, cols, blks = get_sudoku_rows_cols_blks(sudoku, i, j)
    unnecessary = []
    for cdt in range(len(possibility[i][j])):# candidate as cdt
        candidate = possibility[i][j][cdt]
        if candidate in rows or candidate in cols or candidate in blks:
            unnecessary.append(cdt)
    unnecessary = sorted(unnecessary, reverse= True)
    for cdt in range(len(unnecessary)):
        del possibility[i][j][unnecessary[cdt]]
    
    return possibility

def run_double_candidates(sudoku, possibility):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                possibility = double_candidates(possibility, i, j)
                sudoku, possibility = single_candidate(sudoku, possibility, i, j)
    return sudoku, possibility

def run_single_candidate(sudoku, possibility):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku, possibility = single_candidate(sudoku,possibility, i, j)

    return sudoku, possibility
        
def single_candidate(sudoku,possibility, i, j):
    if len(possibility[i][j]) == 1:
        #剩下1種可能的就直接加到數獨上
        sudoku[i][j] = possibility[i][j][0]
        return sudoku, possibility
    else:
        #某個可能性在同個 row or col or blk 只出現1次
        row_possi, col_possi, blk_possi = get_possibility_rows_cols_blks(possibility,i,j)
        for box in range(len(possibility[i][j])):
            candidate = possibility[i][j][box]
            row_times = 0
            col_times = 0
            blk_times = 0
            for cdt in range(8):
                if candidate in row_possi[cdt]:
                    row_times += 1
                if candidate in col_possi[cdt]:
                    col_times += 1
                if candidate in blk_possi[cdt]:
                    blk_times += 1
            if row_times == 0:
                sudoku[i][j] = candidate
            elif col_times == 0:
                sudoku[i][j] = candidate
            elif blk_times == 0:
                sudoku[i][j] = candidate
        return sudoku, possibility

#探討 Hidden Pair 的問題 看圖7/11 https://www.rd.com/list/sudoku-tips/
def double_candidates(possibility, i, j):
    row_possi, col_possi, blk_possi = get_possibility_rows_cols_blks(possibility,i,j)
    row_candidates = []
    col_candidates = []
    blk_candidates = []
    row_candidate_index = []
    col_candidate_index = []
    blk_candidate_index = []

    #如果框框中的某個可能性只出現在框框所屬的 row 1次(不算框框內的1次) 那把這個可能加到row_candidates中 
    # row_candidates 內容不可能只有1個 因為 那是single_candidate()的處理範圍
    # row_candidates 內容 > 2 不再此函式討論範圍
    # row_candidates 內容只會是 0 或 2
    for box in range(len(possibility[i][j])):
        row_appear = 0
        for cdt in range(8):
            if possibility[i][j][box] in row_possi[cdt]:
                row_appear += 1
                row_cdt = possibility[i][j][box]  #--
                index = cdt #index 等會會用到        |
        if row_appear == 1:     #                   |
            row_candidates.append(row_cdt)    #<-----
            row_candidate_index.append(index) #index 等會會用到
    #同樣概念 用在col
    for box in range(len(possibility[i][j])):
        col_appear = 0
        for cdt in range(8):
            if possibility[i][j][box] in col_possi[cdt]:
                col_appear += 1
                col_cdt = possibility[i][j][box]
                index = cdt
        if col_appear == 1:
            col_candidates.append(col_cdt)
            col_candidate_index.append(index)
    #同樣概念 用在blk    block as blk 九宮格的意思
    for box in range(len(possibility[i][j])):
        blk_appear = 0
        for cdt in range(8):
            if possibility[i][j][box] in blk_possi[cdt]:
                blk_appear += 1
                blk_cdt = possibility[i][j][box]
                index = cdt
        if blk_appear == 1:
            blk_candidates.append(blk_cdt)
            blk_candidate_index.append(index)

    #index 確認2個candidates 來源於同一個框框 
    # 如果來自不同框框那會變成triple問題 ex [2,3] [2,5] [3,5]
    if len(row_candidates) == 2 and row_candidate_index[0] != row_candidate_index[1]:
        row_candidates = []
    if len(col_candidates) == 2 and col_candidate_index[0] != col_candidate_index[1]:
        col_candidates = []
    if len(blk_candidates) == 2 and blk_candidate_index[0] != blk_candidate_index[1]:
        blk_candidates = []

    # 處理3對 hidden pair
    if len(row_candidates) == len(col_candidates) == len(blk_candidates) == 2:
        #如果 3 個內容都一樣 ex [2,3] == [2,3] == [2,3]
        if row_candidates == col_candidates == blk_candidates:
            possibility[i][j] = row_candidates #原本可能性可能是[1,2,3,5,7] 變成 [2,3]

        # ex分別為 [2,3] [2,3] [2,4] 要把可能性變成 [2]
        elif row_candidates == col_candidates:
            if row_candidates[0] in blk_candidates:
                del row_candidates[1]
                possibility[i][j] = row_candidates
            else:
                del row_candidates[0]
                possibility[i][j] = row_candidates
        elif col_candidates == blk_candidates:
            if col_candidates[0] in row_candidates:
                del col_candidates[1]
                possibility[i][j] = col_candidates
            else:
                del col_candidates[0]
                possibility[i][j] = col_candidates
        elif row_candidates == blk_candidates:
            if row_candidates[0] in col_candidates:
                del row_candidates[1]
                possibility[i][j] = row_candidates
            else:
                del row_candidates[0]
                possibility[i][j] = row_candidates
    # 處理2對 hidden pair
    elif len(row_candidates) == len(col_candidates) == 2:
        if row_candidates == col_candidates:
            possibility[i][j] = row_candidates
        else:
            if row_candidates[0] in col_candidates:
                del row_candidates[1]
                possibility[i][j] = row_candidates
            else:
                del row_candidates[0]
                possibility[i][j] = row_candidates
    elif len(col_candidates) == len(blk_candidates) == 2:
        if col_candidates == blk_candidates:
            possibility[i][j] = col_candidates
        else:
            if col_candidates[0] in blk_candidates:
                del col_candidates[1]
                possibility[i][j] = col_candidates
            else:
                del col_candidates[0]
                possibility[i][j] = col_candidates
    elif len(row_candidates) == len(blk_candidates) == 2:
        if row_candidates == blk_candidates:
            possibility[i][j] = row_candidates
        else:
            if row_candidates[0] in blk_candidates:
                del row_candidates[1]
                possibility[i][j] = row_candidates
            else:
                del row_candidates[0]
                possibility[i][j] = row_candidates
    #這邊是只有找到1個 row 或 col 或 blk 有 hidden pair
    elif len(row_candidates) == 2:
        possibility[i][j] = row_candidates
    elif len(col_candidates) == 2:
        possibility[i][j] = col_candidates
    elif len(blk_candidates) == 2:
        possibility[i][j] = blk_candidates

    return possibility

if __name__ == '__main__':
    main()

#100%原創 如有雷同純屬巧合
#靈感來源於https://www.rd.com/list/sudoku-tips/