from Selenium_project.ToolsQA.test import addition
from Selenium_project.ToolsQA.test3 import add


class sum(addition, add):
    def __init__(self):
        addition.__init__(self, 2, 10, 40)

    def summat(self):
        e = self.a + self.b
        print(e)
        return e

obj = sum()
print(obj.summat())
obj.addition_section()
