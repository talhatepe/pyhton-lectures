class Calculator:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def infix2Postfix(self,infix):
        prec = {}
        prec["*"] = 2
        prec["/"] = 2
        prec["+"] = 1
        prec["-"] = 1
        self.Stack = Calculator()
        self.PostFix = []
        self.TempArr=[]
        self.infix=infix
        infix=infix.replace(" ","")
        inlen=len(infix)
        for arr in range (inlen):
            self.TempArr.append(infix[arr])
        for value in self.TempArr:
            if value in "0123456789":
                self.PostFix.append(value)
            else:
                while (not self.Stack.isEmpty()) and \
                 (prec[self.Stack.peek()] >= prec[value]):
                    self.PostFix.append(self.Stack.pop())
                self.Stack.push(value)
        while not self.Stack.isEmpty():
            self.PostFix.append(self.Stack.pop())
        return " ".join(self.PostFix)

inf=input("Infix giriniz : ")
pfix=Calculator().infix2Postfix(inf)
print("Postfix : "+pfix)