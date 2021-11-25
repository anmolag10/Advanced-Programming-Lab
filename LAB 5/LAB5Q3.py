class uniqueSubset:
    def __init__(self):
        self.n = int(input("ENTER NUMBER OF ELEMENTS IN LIST: "))
        self.arr = []
        for i in range(self.n):
            self.arr.append(int(input("Enter element: ")))

    def bigcalc(self):
        return self.subsetsRecur([], sorted(self.arr))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]    


def main():
    list1 = uniqueSubset()
    print(list1.bigcalc())
    

if __name__=="__main__":
    main()