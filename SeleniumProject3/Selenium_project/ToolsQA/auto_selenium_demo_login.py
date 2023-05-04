
from auto_starting import Staring
from auto_checkbox import CheckBox


class toolsqa(Staring, CheckBox):
    pass


obj = toolsqa()
obj.initialize("https://demoqa.com/")
obj.checkbox_section()

