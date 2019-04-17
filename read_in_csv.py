#name                                                             Convolve Team
#Assignment                                                         readin file
#date                                                                 4-16-2019

def file_reader(infile_name):

    # setting up the headers for the csv
    TSn = 0 # timestep
    C0n = 0
    C1n = 0
    C2n = 0
    C3n = 0
    C4n = 0
    C5n = 0
    
    # setting up arrays
    t_array = []
    C0_array = []
    C1_array = []
    C2_array = []
    C3_array = []
    C4_array = []
    C5_array = []
    
    # opening the file
    file = open(infile_name, 'r')
    
    # checking the first line in the file for header names
    firstline = file.readline()
    firstline = firstline.strip() # fixing any odd spacing
    firstline_list = firstline.split(',') # creating a list
    print(firstline_list)

    In = 0 # iterations
    
    # this assigns a number to each header(array) of the csv infile
    for things in firstline_list:
        if firstline_list[In] == 't':
            TSn = In
            In += 1
        elif firstline_list[In] == 'curve0':
            C0n = In
            In += 1
        elif firstline_list[In] == 'curve1':
            C1n = In
            In += 1
        elif firstline_list[In] == 'curve2':
            C2n = In
            In += 1
        elif firstline_list[In] == 'curve3':
            C3n = In
            In += 1
        elif firstline_list[In] == 'curve4':
            C4n = In
            In += 1
        elif firstline_list[In] == 'curve5':
            C5n = In
            In += 1
        else:
            In += 1

    # initializing line number
    line_num = 0

    # reading in lines
    for lines in file:
        #print(lines)
        newlines = lines.split(',')
        
        # setting up which portion of the list to grab for the array
        t = float(newlines[TSn])
        Curve_0 = float(newlines[C0n])
        Curve_01 = float(newlines[C1n])
        Curve_02 = float(newlines[C2n])
        Curve_03 = float(newlines[C3n])
        Curve_04 = float(newlines[C4n])
        Curve_05 = float(newlines[C5n])
        
        # headers
        if line_num == 0:
            t_array.append('Time')
            C0_array.append('Curve_0')
            C1_array.append('Curve_01')
            C2_array.append('Curve_02')
            C3_array.append('Curve_03')
            C4_array.append('Curve_04')
            C5_array.append('Curve_05')
            line_num += 1
        
        # data
        else:
            t_array.append(t)
            C0_array.append(Curve_0)
            C1_array.append(Curve_01)
            C2_array.append(Curve_02)
            C3_array.append(Curve_03)
            C4_array.append(Curve_04)
            C5_array.append(Curve_05)
            line_num += 1

    file.close()

    # checking for correctness
    print(t_array)
    print(C0_array)
    print(C1_array)
    print(C2_array)
    print(C3_array)
    print(C4_array)
    print(C5_array)

# calling the function
file_reader('sample_batmanCurves.csv')

