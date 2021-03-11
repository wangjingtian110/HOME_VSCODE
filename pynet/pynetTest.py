import clr
import sys
import System

sys.path.append(r'E:\code\vs\Console\TestDLL\bin\Debug')
d = clr.AddReference('TestDLL')

from TestDLL import * 


m = MasterImpl()
s = m.GetString()
print(s)
m.SetMessage("Hello Python")
s = m.GetString()
print(s)

# 调用返回byte
a = b'1234'
print(a)
print(str(a, encoding="utf-8"))
meta = m.GetMeta(a)
b = meta.get_value()
lb = bytes(b)
print(lb)
s = str(lb, encoding="utf-8")
print(s)


# Event

def handler(source,args):
    print(a.PackageMessage)

def handler(source, args):
    print('my_handler called!')

m.packageEventHandller += handler
m.packageEventHandller += lambda s,a: print("lambda event")
m.GetString()

#exception

try:
    m.Raise()
except TestException as e:
    print(e.Message)

print("ok")