from Selenium_project.ToolsQA.test3 import add


class addition(add):
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d
        print(self.a)
        print(self.b)
        print(self.d)

    def summation(self):
        c = self.a + self.b + self.d
        print(c)
        return c


obj = addition(10, 20, 30)
print(obj.summation())

obj.addition_section()

