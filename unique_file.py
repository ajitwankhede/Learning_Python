def unique_file(input_file, output_file):
    input_file = open(input_file, "r")
    file_content = input_file.read()
    input_file.close()
    duplicates =[]
    word_list = file_content.split()
    file = open(output_file, "w")
    for word in word_list:
        if word not in duplicates:
            duplicates.append(word)
            file.write(str(word) + '\n')
    file.close()
    
