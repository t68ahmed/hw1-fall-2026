trips_duration = []
filename = "mini-trips.csv"

infile = open(filename)
header = infile.readline()

for line in infile:
    row = line.split(",")
    seconds = int(row[0])
    trips_duration.append(seconds)
infile.close()

trips_duration_sorted = sorted(trips_duration)

print("Number of Trips: ", len(trips_duration))
print("Shortest Duration in Seconds: ", trips_duration_sorted[0])
print("Longest Duration in Seconds: ", trips_duration_sorted[-1])
print("Mean Duration in Seconds: ", (sum(trips_duration)/len(trips_duration)))
print("Median Duration in Seconds: ", trips_duration_sorted[len(trips_duration_sorted) // 2])