class Matrix:
    def __init__(self, List):
        self.List = List

    def display(self):
        print(self.List)

    def __add__(self, M):
        Temp = Matrix([])
        for i in range(len(self.List)):
            for j in range(len(self.List[0])):
                Temp.List.append(self.List[i][j] + M.List[i][j])
        return Temp


Matrix1 = Matrix([[1, 2], [3, 4]])
Matrix2 = Matrix([[4, 5], [6, 7]])
Matrix3 = Matrix([])
Matrix3 = Matrix1 + Matrix2
print("The addition of Matrix: ")
Matrix3.display()
