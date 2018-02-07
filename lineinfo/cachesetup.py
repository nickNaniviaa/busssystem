def readparams():
    file= open(r"C:\startup_info.txt","r")

    x = file.readline()
    driver_id = x[x.index(":")+1:-1]#Discard \n
    
    x = file.readline()
    driver_name = x[x.index(":")+1:-1] #Discard \n
    
    x = file.readline()
    line_number = x[x.index(":")+1:-1] #Discard \n
    
    x = file.readline()
    direction = x[x.index(":")+1:-1] #Discard \n
    
    x = file.readline()
    time= x[x.index(":")+1:-7] #Discard \n and last 6 digits of precision - seconds
    
    file.close()

    return(driver_id,driver_name,line_number,direction,time)
    