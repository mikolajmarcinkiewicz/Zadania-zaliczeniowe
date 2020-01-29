class Matrix():
    
    
    def __init__(self, m, n):
        self.m = m #liczba wierzy
        self.n = n #liczba kolumn
    
    def fill(self):
        self.body = []
        for i in range(self.m):
            init_list = []
            for j in range(self.n):
                element = float(input("aij = "))
                init_list.append(element)
            
            self.body.append(init_list)
            
    def zeros(self):
        self.body = []
        for i in range(self.m):
            init_list = []
            for j in range(self.n):
                element = 0
                init_list.append(element)
            
            self.body.append(init_list)
            
    def ones(self):
        self.body = []
        for i in range(self.m):
            init_list = []
            for j in range(self.n):
                element = 1
                init_list.append(element)
            
            self.body.append(init_list)
            
    def unit(self):
        if(self.m == self.n):
            self.body = []
            for i in range(self.m):
                init_list = []
                for j in range(self.n):
                    if (i==j):
                        element = 1
                    else:
                        element = 0
                    init_list.append(element)
            
                self.body.append(init_list)
        else:
            print("dimensions not equal")
            
    def add(self, other):
        if(self.n == other.n and self.m == other.m and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.m):
                for j in range(self.n):
                    self.body[i][j] = self.body[i][j] + other.body[i][j]
            
        else:
            print("dimensions not equal")
            
    def substr(self, other):
        if(self.n == other.n and self.m == other.m and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.m):
                for j in range(self.n):
                    self.body[i][j] = self.body[i][j] - other.body[i][j]
            
        else:
            print("dimensions not equal")
            
    def multByNumber(self, a):
        for i in range(self.m):
            for j in range(self.n):
                self.body[i][j] = a*self.body[i][j]      
