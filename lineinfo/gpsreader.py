def read_gps():
    file = open(r"C:\\gps_info.txt", "r")

    line_read = file.readline()
    latitude = float(line_read[line_read.index(":")+1:-1])#Discard \n

    line_read = file.readline()
    longitude = float((line_read[line_read.index(":")+1:]))

    file.close()
    return(latitude, longitude)
