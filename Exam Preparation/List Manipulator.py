def list_manipulator(*argv):
    result = list(argv[0])
    if argv[1] == "add":
        if argv[2] == "beginning":
            index = 0
            for i in range(3, len(argv)):
                result.insert(index, argv[i])
                index += 1
        else:
            for i in range(3, len(argv)):
                result.append(argv[i])
    else:
        if argv[2] == "beginning":
            if len(argv) == 3:
                result.pop(0)
            else:
                for i in range(argv[3]):
                    if len(result) == 0:
                        break
                    result.pop(0)
        else:
            if len(argv) == 3:
                result.pop()
            else:
                for i in range(argv[3]):
                    result.pop()

    return result


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))



