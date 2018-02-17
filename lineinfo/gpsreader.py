def readGps():
    file= open(r"C:\\gps_info.txt","r")

    x = file.readline()
    latitude = float(x[x.index(":")+1:-1])#Discard \n
    
    x = file.readline()
    longitude = float((x[x.index(":")+1:]))
    
    file.close()

    return(latitude,longitude)