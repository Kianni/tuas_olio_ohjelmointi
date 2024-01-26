# File: listOfYears.py
# Author: Kirill Nikolaev
# Description: takes a list of date type objects as its argument. The function should return a new list, 
# which contains the years in the original list from earliest to latest

from typing import List
from datetime import datetime

def list_years(dates: List[datetime]) -> List[int]:
    # Extract the year from each date and sort the list
    years = sorted(date.year for date in dates) # reverse=True for descending order
    return years

date1 = datetime(2019, 1, 13)
date2 = datetime(1908, 7, 14)
date3 = datetime(1017, 9, 1)

print(list_years([date1, date2, date3]))