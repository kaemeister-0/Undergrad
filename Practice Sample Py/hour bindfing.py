seconds = 1
minutes = 60*seconds
hours= 60*minutes

#all the times in seconds

left_house_time = 6*hours+52*minutes
run_time_easypace = 8*minutes+15*seconds
tempo_time = 7*minutes+12*seconds
run_time_easypacetwo = 8*minutes+15*seconds

breafast_time = (left_house_time+run_time_easypace+run_time_easypacetwo+tempo_time)

#change seconds into hourly format
breakfast_hour = breafast_time//3600
breakmin = (breafast_time%3600)
breakfast_minute = (breakmin//60)

print ("I get home for breakfast at %s:%s a.m. " %(breakfast_hour,breakfast_minute))