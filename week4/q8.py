def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]
def determinantOfMatrix(mat):
	if(len(mat) == 2):
		value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
		return value
	Sum = 0
	for current_column in range(len(mat)):
		
		sign = (-1) ** (current_column)
		sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
		Sum += (sign * mat[0][current_column] * sub_det)
	return Sum
class rankMatrix(object):
    def __init__(self, Matrix):
        self.R = len(Matrix)
        self.C = len(Matrix[0])
         
    
    def swap(self, Matrix, row1, row2, col):
        for i in range(col):
            temp = Matrix[row1][i]
            Matrix[row1][i] = Matrix[row2][i]
            Matrix[row2][i] = temp
             
    
    def Display(self, Matrix, row, col):
        for i in range(row):
            for j in range(col):
                print (" " + str(Matrix[i][j]))
            print ('\n')
             
    
    def rankOfMatrix(self, Matrix):
        rank = self.C
        for row in range(0, rank, 1):
             
            
            
            
            
     
            
            if Matrix[row][row] != 0:
                for col in range(0, self.R, 1):
                    if col != row:
                         
                        
                        
                        multiplier = (Matrix[col][row] /
                                      Matrix[row][row])
                        for i in range(rank):
                            Matrix[col][i] -= (multiplier *
                                               Matrix[row][i])
                                                 
            
            
            
            
            
            
            
            
            
            
            
            else:
                reduce = True
                 
                
                
                for i in range(row + 1, self.R, 1):
                     
                    
                    
                    if Matrix[i][row] != 0:
                        self.swap(Matrix, row, i, rank)
                        reduce = False
                        break
                         
                
                
                
                
                if reduce:
                     
                    
                    rank -= 1
                     
                    
                    for i in range(0, self.R, 1):
                        Matrix[i][row] = Matrix[i][rank]
                         
                
                row -= 1
                 
        
        return (rank)

mat = [[1, 0, 2, -1],
		[3, 0, 0, 5],
		[2, 1, 4, -3],
		[1, 0, 5, 0]]
RankMatrix = rankMatrix(mat)
print ("Rank of the Matrix is:",(RankMatrix.rankOfMatrix(mat)))
print('Determinant of the matrix is :', determinantOfMatrix(mat))