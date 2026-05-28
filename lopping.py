#count = 1
#while count<=5:
#    print(1, end=' ')
#    count=count+1


#count = 1
#while count<=5:
#    print(count, end=' ')        #print(1, end='\n')
#    count=count+1

#station = 30
#i = 1
#
#while i <= station:
#
#    if i % 3 == 0 and i % 5 == 0:
#        print("station meet", i)
#
#    i += 1


#danny = 40
#durai_singam = 0
#
#while(durai_singam < danny):
#
#    danny += 2
#    durai_singam += 5
#
#print(durai_singam)



#station_no = 1
#while station_no<=30:
#    if station_no%3==0:
#        print('Train 1 Stops at', station_no)
#    if station_no%5==0:
#        print('Train 2 Stops at', station_no)
#    if station_no%3==0 and station_no%5==0:
#        print('Both Trains Stops at', station_no)
#        
#    station_no = station_no + 1



station_no = 1

first_station = 0
last_station = 0
count = 0

while station_no <= 300:

    if station_no % 3 == 0 and station_no % 8 == 0:

        # First Station
        if first_station == 0:
            first_station = station_no

        # All Stations
        print(station_no)

        # Count
        count = count + 1

        # Last Station
        last_station = station_no

    station_no = station_no + 1


print("First Station :", first_station)
print("All Stations Count :", count)
print("Last Station Number :", last_station)
































