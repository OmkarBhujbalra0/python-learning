# Generators

def generate():
    yield "Result One"
    yield "Result Two"
    yield "Result Three"

res = generate()

for i in res:
    print(i)

res2 = generate()
print(next(res2))