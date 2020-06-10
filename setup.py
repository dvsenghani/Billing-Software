# from cx_Freeze import setup, Executable
# setup(name = "Bill System",
#         version = "0.1",
#         description = "Grocery Billing System",
#         executable = [Executable(r'/Users/DS-MAC/Desktop/SSU/Python/Bill.py/bill.py')]
# )
import sys
from cx_Freeze import setup, Executable



# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Bill System",
        version = "0.1",
        description = "Grocery Billing System",
        
        executables = [Executable(r'/Users/DS-MAC/Desktop/SSU/Python/Bill.py/bill.py', base=base)])