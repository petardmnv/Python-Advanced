def numbers_searching(*args):
    result = [i for i in range(min(args), max(args) + 1)]
    dub = []
    my_set = set([n for n in args])
    print(my_set)
    for num in args:
        if num in result:
            result.remove(num)
    for num in my_set:
        if args.count(num) > 1:
            dub.append(num)

    result.append(sorted(dub))
    return result
