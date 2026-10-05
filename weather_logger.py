temps = []

while True:
    entry = input("Enter temperature ('done' to stop): ")

    if entry.lower() == "done":
        break

    temps.append(float(entry))

print(temps)