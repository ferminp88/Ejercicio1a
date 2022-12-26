items = input("Introduce países separados por comas:\n")

for x in range(5):
 paises = [pais for pais in items.split(",")]

print(",".join(sorted(list(set(paises)))))