import json
import sys
f = open(sys.argv[1])
# f = open('lax.json')
lax = json.load(f)
f.close()
in_put = sys.argv[2]
# in_put = "arrival departure"
input_list = in_put.split(" ", len(in_put)-1)
def chosen_data(input_list,lax):
    ReportPeriod = []
    Terminal = []
    Arrival_Departure = []
    data_set = []
    new_data_set =[]
    nnew_data_set = []
    telchange = {"T1": "Terminal 1",
                 "T2": "Terminal 2",
                 "T3": "Terminal 3",
                 "T4": "Terminal 4",
                 "T5": "Terminal 5",
                 "T6": "Terminal 6",
                 "TBI": "Tom Bradley International Terminal"}
    lax["data"] = [line for line in lax["data"] if line[10] in telchange.values()]
    for i in range(0,len(input_list)):
        input_list[i]=input_list[i].upper()
        if input_list[i].startswith("T"):
            Terminal.append(input_list[i])
            Terminal = list(set(Terminal))
        elif input_list[i].isdigit():
            ReportPeriod.append(input_list[i])
            ReportPeriod = list(set(ReportPeriod))
        elif input_list[i] == "DEPARTURE" or input_list[i] == "ARRIVAL":
            Arrival_Departure.append(input_list[i])
            Arrival_Departure = list(set(Arrival_Departure))# remove repetitive items

    if len(Terminal) > 0:
        for item in Terminal:
            for j in range(0, len(lax["data"])):
                if lax["data"][j][10] == telchange[item]:
                    data_set.append(lax["data"][j])

        if len(ReportPeriod) > 0:
            for time in ReportPeriod:
                for k in range(0, len(data_set)):
                    year = data_set[k][9]
                    if year[0:4] == time:
                        new_data_set.append(data_set[k])
            data_set = new_data_set[:]

        if len(Arrival_Departure) > 0:
            for statue in Arrival_Departure:
                statue = statue.title()
                for h in range(0, len(data_set)):
                    if data_set[h][11] == statue:
                        nnew_data_set.append(data_set[h])
            data_set = nnew_data_set[:]

    elif len(ReportPeriod) > 0:
        for time in ReportPeriod:
            for b in range(0, len(lax["data"])):
                year = lax["data"][b][9]
                if year[0:4] == time:
                    data_set.append(lax["data"][b])

        if len(Arrival_Departure) > 0:
            for statue in Arrival_Departure:
                statue = statue.title()
                for a in range(0, len(data_set)):
                    if data_set[a][11] == statue:
                        new_data_set.append(data_set[a])
            data_set = new_data_set[:]

    elif len(Arrival_Departure) > 0:
        for statue in Arrival_Departure:
            statue = statue.title()
            for x in range(0, len(lax["data"])):
                if lax["data"][x][11] == statue:
                    data_set.append(lax["data"][x])

    return data_set


def min_data(data_set):
    passenger_count = []
    for i in range(0,len(data_set)):
        passenger_count.append(data_set[i][13])
    passenger_count = map(int, passenger_count)
    compare_item = passenger_count[0]
    for item in passenger_count:
        if item < compare_item:
            compare_item = item
    return compare_item

def max_data(data_set):
    passenger_count = []
    compare_item = 0
    for i in range(0, len(data_set)):
        passenger_count.append(data_set[i][13])
    passenger_count = map(int, passenger_count)
    for item in passenger_count:
        if item > compare_item:
            compare_item = item
    return compare_item

def median_data(data_set):
    passenger_count = []
    median = 0.0
    for i in range(0,len(data_set)):
        passenger_count.append(data_set[i][13])
    passenger_count = sorted(map(int, passenger_count))
    if len(passenger_count)%2 == 0:
        median = (passenger_count[len(passenger_count)/2]+passenger_count[(len(passenger_count)/2)-1])/2.0
    elif len(passenger_count)%2 !=0:
        median = passenger_count[(len(passenger_count)-1)/2]
    return round(median,1)

def average_data(data_set):
    passenger_count = []
    sum_item = 0.0
    for i in range(0,len(data_set)):
        passenger_count.append(data_set[i][13])
    passenger_count = map(int, passenger_count)
    for item in passenger_count:
        sum_item = sum_item + item
    return round(sum_item/len(passenger_count),2)

def standarddeviation_data(data_set):
    passenger_count = []
    deviation = 0.0
    average = average_data(data_set)
    for i in range(0,len(data_set)):
        passenger_count.append(data_set[i][13])
    passenger_count = map(int, passenger_count)
    for item in passenger_count:
        deviation = deviation + (item - average)**2
    standard_deviation = (deviation/len(passenger_count))**0.5
    return round(standard_deviation,2)

data_set = chosen_data(input_list,lax)
print str(min_data(data_set)) + "," + str(max_data(data_set)) + "," + str(median_data(data_set)) + "," + \
      str(average_data(data_set)) + "," + str(standarddeviation_data(data_set))
