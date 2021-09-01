
def generate_sudoku(arr):
    print("Question: \n")
    for i in range(9):
        answer = ""
        for j in range(9):
            answer += " " + str(arr[i][j])
        print(answer)


