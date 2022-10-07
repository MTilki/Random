distance_km = 10

time_s = (42 * 60) + 42
time_m = time_s / 60
time_h = time_m /60

print ("distance_km:",distance_km)
print ("time_s:",time_s)
print ("time_m:",time_m)
print ("time_h:",time_h)

#convert km to miles

distance_mile = distance_km / 1.61

print("distance_mile:",distance_mile)


#cal time per mile in seconds

seconds_per_mile = distance_mile / time_s

print("Seconds per mile:",seconds_per_mile)
#cal time per mile in minuets
minuet_per_mile = distance_mile / time_m

print("Minuet per mile:",minuet_per_mile)

#cal mph
mph = distance_mile / time_h

print("MPH:",mph)
