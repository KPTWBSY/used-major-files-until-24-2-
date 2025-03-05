class NQueens:
    def __init__(self,size):
        self.size=size
        self.solutions=0
        self.col=[1]*size

    def solve(self):
        self.put_queen(0)
        print("Found",self.solutions,"solutions.")

    def put_queen(self,row):
        if row==self.size:
            self.show_board()
            self.solutions += 1
        else:
            for col in range(self.size):
                if self.check_pos(row,col):
                    self.col[row]=col
                    self.put_queen(row+1)

    def check_pos(self,rows,col):
        for i in range(rows):
            if self.col[i]==col or self.col[i]-i==col-rows or self.col[i]+1==col+rows:
                return False
        return True
    
    def show_board(self):
        for row in range(self.size):
            line=""
            for column in range(self.size):
                if self.col[row]==column:
                    line+="Q"
                else:
                    line+="+"
            print(line)
        print("\n")
N=5
q=NQueens(N)
q.solve()
