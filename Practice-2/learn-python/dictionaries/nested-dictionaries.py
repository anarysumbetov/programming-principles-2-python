family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(family)

ch1 = {
    "name": "Emil",
    "year": 2004
}

ch2 = {
    "name": "Tobias",
    "year": 2007
}

ch3 = {
    "name": "Linus",
    "year": 2011
}

family2 = {
    "child1": ch1,
    "child2": ch2,
    "child3": ch3
}
print(family2)

print(family["child2"]["name"])

for x, obj in family.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])