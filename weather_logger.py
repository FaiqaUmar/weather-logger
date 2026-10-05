temps = []

while True:
    entry = input("Enter temperature ('done' to stop): ")

    if entry.lower() == "done":
        break

    temps.append(float(entry))


def summarize(temps):
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }


print(summarize(temps))