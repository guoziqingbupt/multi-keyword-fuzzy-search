import fuzzy_query

index = ["C++", "Java", "Python"]

for i in range(100):
    print(fuzzy_query.fuzzyQuery("PHP", index))