from datetime import datetime


class GTFS:

    def __init__(self):
        self.stop_times = []
        with open("./data/bus/stop_times.txt") as stop_times:
            for line in stop_times:
                data = line.split(',')
                trip_id, arrival_time, _, stop_id, *_ = data
                self.stop_times.append([trip_id, arrival_time, stop_id])

        self.trips = {}
        with open("./data/bus/trips.txt") as trips:
            for line in trips:
                data = line.split(',')
                _, service_id, trip_id, *_ = data
                self.trips[trip_id] = service_id

        self.calendar_dates = {}
        with open("./data/bus/calendar_dates.txt") as calendar_dates:
            for line in calendar_dates:
                data = line.split(',')
                service_id, date, _ = data
                self.calendar_dates[service_id] = date

    def __get_date_for_trip(self, trip_id):
        service_id = self.trips[trip_id]
        return self.calendar_dates[service_id]

    def __format_date(self, date):
        return datetime.strptime(date, "%Y%m%d").strftime("%Y-%m-%d")

    def schedules(self, orig_code, dest_code):
        ret = []
        trip_selector = ""
        eta = ""
        etd = ""
        for record in self.stop_times:
            trip_id, arrival_time, stop_id = record

            if (trip_id != trip_selector):
                trip_selector = trip_id
                eta = ""
                etd = ""

            if (stop_id == orig_code):
                etd = arrival_time

            if (stop_id == dest_code):
                eta = arrival_time

            if (eta != "" and etd != ""):
                date = self.__get_date_for_trip(trip_id)
                f_date = self.__format_date(date)

                ret.append({"transit_mode": "bus",
                            "etd": f_date + " " + etd,
                            "eta": f_date + " " + eta})
                eta = ""
                etd = ""

        return ret


if __name__ == "__main__":
    """An old school teest function
    """

    temp = GTFS()

    if (temp.schedules("2204", "2399")):
        print("Existing path: PASS")
    else:
        print("Existing path: FAIL")

    if (temp.schedules("", "")):
        print("Empty path: FAIL")
    else:
        print("Empty path: PASS")

    if (temp.schedules("00100", "11011")):
        print("Not existing path: FAIL")
    else:
        print("Not existing path: PASS")

    print(temp.schedules("2204", "2399"))
