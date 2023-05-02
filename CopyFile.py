def copyfile():
    infile = input('Enter the input file name with extension: ')
    outfile = input('Enter the output file name with extension: ')
    
    # Open the input file in reading mode
    f1 = open(infile , "r")
    
    # Open the output file in write mode
    f2 = open(outfile, "w+")
    
    # Read the contain in file f1 to convert variable
    content = f1.read()
    
    # Then write the vale of content variable to f2
    f2.write(content)
    
    # closing the file f1 and f2
    f1.close()
    f2.close()
    