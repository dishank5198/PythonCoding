class Time:
    def __init__(self, hours: int, mins: int):
        self.hours = hours
        self.mins = mins
        self.final_hrs = 0
        self.final_minis = 0

    def add_time(self, hrs, minis):
        final_min = self.mins + minis
        remainder_min = final_min % 60
        final_hrs = self.hours + hrs
        final_hrs = final_hrs + (final_min)//60
        self.final_hrs = final_hrs
        self.final_minis = remainder_min
        print(f"Final time is {{final_hrs}} Hours and {{final_min}} Mins".format(final_hrs = final_hrs, final_min=remainder_min))

    def total_mins(self):
        t_minis = (self.final_hrs * 60) + self.final_minis
        print("Total Miniutes are: "+str(t_minis))


final_time = Time(5,45)
final_time.add_time(3,45)
final_time.total_mins()