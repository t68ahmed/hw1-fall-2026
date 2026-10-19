trips_duration = []
filename = "trips.csv"

infile = open(filename)
header = infile.readline()

for line in infile:
    row = line.split(",")
    seconds = int(row[0])
    trips_duration.append(seconds)
infile.close()

trips_duration_sorted = sorted(trips_duration)
n = len(trips_duration_sorted)

median = (trips_duration_sorted[(n-1)//2] + trips_duration_sorted[n//2])/2
median_mins =  median/60

min_duration = trips_duration_sorted[0]
min_duration_mins = min_duration/60

max_duration = trips_duration_sorted[-1]
max_duration_mins = max_duration/60

mean_duration = sum(trips_duration_sorted) / n
mean_duration_mins = round((mean_duration/60), 1)


three_longest_trips_list =[]
three_longest_trips = trips_duration_sorted[-3:]
for duration in three_longest_trips:
    line = duration/60
    three_longest_trips_list.append(line)


print("Number of Trips: ", n)
print("Shortest Duration in Seconds: ", min_duration, "and that'll be", min_duration_mins, "minutes.")
print("Longest Duration in Seconds: ", max_duration, "and that'll be", max_duration_mins, "minutes.")
print("Mean Duration in Seconds: ", mean_duration, "and that'll be", mean_duration_mins, "minutes.")
print("Median Duration in Seconds: ", median, "and that'll be", median_mins, "minutes.")
print("The three longest trips in minutes are: ", three_longest_trips_list)