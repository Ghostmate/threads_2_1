def calculate_structure_sum(*args):
    s = 0
    if isinstance(args,int):
        return args
    if isinstance(args,str):
        return len(args)
    if isinstance(args,tuple|list):
        for f in args:
            if isinstance(f,int):
                return f
            if isinstance(f,str):
                return len(f)
            if isinstance(f,dict):
                for k in f.items():
                    s += calculate_structure_sum(k)
            else:
                for k in f:
                    s += calculate_structure_sum(k)
    return s

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)