with open("My_first_text_file.txt", 'w') as f:
    f.write("My first words.Blagh")
with open("My_first_text_file.txt", 'r') as f:
    print(f.readline())
