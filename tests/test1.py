import pippity

result = pippity.install("numpy")

print(result.ok)
print(result.stdout)
print("\n\n\n")
print(result.stderr)


result = pippity.install(["flask", "quart"])

print(result.ok)
print(result.stdout)
print("\n\n\n")
print(result.stderr)
