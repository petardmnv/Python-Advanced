get_info = lambda name, town, age: f'This is {name} from {town} and he is {age} years old'

print(get_info(**{"name": "Peter", "town": "Sofia", "age": "17"}))