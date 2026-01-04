class Test:
    def __init__(self):
        print("INIT sef id:", id(self))

t1 = Test()
t2 = Test()

print("t1 id:", id(t1))
print("t2 id:", id(t2))