from math import floor
class  CalendarGenerator:
    def is_leap_year(self, year):
        if year%4==0 and year%100!=0 or year%400==0:
            return True
        else:
            return False
    def get_days_in_month(self, month,year):
        m30=[4,6,9,11]
        m31=[1,3,5,7,8,10,12]
        if month in m30:
            return 30
        elif month in m31:
            return 31
        elif self.is_leap_year(year)==True and month==2:
            return 29
        else:
            return 28
    def  get_start_day_of_month(self,month,year):
        start_1=(1+floor((13*(13+1))/5)+int(str(year)[2:])+floor((int(str(year)[2:]))/4)+5-21)%7
        start_2=(1+floor((13*(14+1))/5)+int(str(year)[2:])+floor((int(str(year)[2:]))/4)+5-21)%7
        start=(1+floor((13*(month+1))/5)+int(str(year)[2:])+floor((int(str(year)[2:]))/4)+5-20)%7
        week_day={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',0:'Sunday'}
        if month ==1:
            return start_1
        elif month ==2:
            return start_2
        else:
            return start
    def build_grid_string(self,start_day_index,total_days):
        self.start_day_index=self.get_start_day_of_month(1,2026)
        return self.start_day_index


print(CalendarGenerator().build_grid_string(1,31))