x = None
print(x)
print(type(x))

result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

if result is not None:
    print("Result is ready")
else:
    print("No result yet")

print(bool(None))

def func():
    z = 5

y = func()
print(y)