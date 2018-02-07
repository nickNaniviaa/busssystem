import datetime

CONST_DRIVERID = "5"
CONST_DRIVERNAME = 'GERALDO C.'


CONST_START_TIME = datetime.datetime.now()

file = open(r"C:\startup_info.txt","w")

line_number = input("Insert Line: ")
direction = input("Direction: 1 for Terminal - O for Neighborhood: ")
file.write("DRIVER_ID:{}".format(CONST_DRIVERID))
file.write("\nDRIVER_NAME:{}".format(CONST_DRIVERNAME))
file.write("\nLINE_NUMBER:{}".format(line_number))
file.write("\nDIRECTION:{}".format(direction))
file.write("\nSTART_TIME:{}".format(CONST_START_TIME))

file.close()


