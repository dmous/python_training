# Learning Python
def main():
    print('Hello World!')

if __name__ == "__main__":
    main()

f = 0
print(f)
# produces error
print("this is a string" + 1)
print("this is a string " + str(1))

f = 0
def some_function():
    f = "define"
    print(f)

print(f)
some_function()

f = 0
def some_function():
    global f
    f = "define"
    print(f)

some_function()
print(f)

del f
print(f)
some_function()
print(f)

# Functions
def func1():
    print("I am a function")

func1()
print(func1())
print(func1)

def func2(arg1, arg2):
    print(arg1, " ", arg2)

def cube(x):
    return x**3

func2(10,20)
print(cube(3))

def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


print(multi_add(4, 5, 10, 15))


# Conditional structures
def main():
    x, y = 100, 100

    if x < y:
        st = "x is less than y"
    elif x > y:
        st = "x is greater than y"
    else:
        st = "x is equal to y"

    # conditional statement in one line
    stq = "x is less than y" if x < y else "x is greater than or equal to y"

    print(st)
    print(stq)


if __name__ == "__main__":
    main()


# Loops
def main():
    x = 0

    # The while loop
    # while x < 5:
    #     print(x)
    #     x += 1

    # The for loop
    # for i in range(5, 10):
    #     print(i)

    days = ["Mon", "Tue", "Wed", "Thur", "Fr", "Sat", "Sun"]
    for i, d in enumerate(days):
        # if d == "Wed":
            # break
        # if d == "Thur":
            # continue
        # print(d)

        print(i, d)

if __name__ == "__main__":
    main()

# Object - Oriented Programming
class myClass():
    def method1(self):
        print("Some string")

    def method2(self, someString):
        print("myClass method2 " + someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("another class method1")

    def method2(self, someString):
        print("anotherClass method2 ")


def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is another class method 2")

if __name__ == "__main__":
    main()

# Date and time
from datetime import date
from datetime import time
from datetime import datetime


def main():
    today = date.today()
    print("Today's date is: {0}".format(today))

    # Print out the individual components
    print("Today is the {0}, of the month {1} and year {2}".format(today.day, today.month, today.year))

    # Retrieve weekdays (0 for Monday and 6 for Sunday)
    print("Today's weekday # is {0}".format(today.weekday()))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Today's weekday # is {0}, which is a {1}".format(today.weekday(), days[today.weekday()]))

    # Datetime objects
    today_datetime = datetime.now()
    today_time = datetime.time(today_datetime)
    print("The current date and time is: {0}. Hence, the time is {1}".format(today_datetime, today_time))


if __name__ == "__main__":
    main()

# Date and time formatting
from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Datetime objects
    today_datetime = datetime.now()

    print(today_datetime.strftime("The current year is: %Y"))
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(today_datetime.strftime("Another way to format datetime: %a, %d %B, %Y"))

    # %c - locale's date and time, %x locale's date, %X locale's time
    print(today_datetime.strftime("Locale date and time: %c"))
    print(today_datetime.strftime("Locale date: %x"))
    print(today_datetime.strftime("Locale time: %X"))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(today_datetime.strftime("Current time: %I:%M:%S %p"))
    print(today_datetime.strftime("Current time (24-hour): %H:%M"))

if __name__ == "__main__":
    main()

# Time delta objects
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))
now = datetime.now()
print("Today is: {0}. \nOne year from now it will be: {1}!".format(now, str(now + timedelta(days=365))))
print("In 2 days and 3 weeks, it will be: {0}".format(str(now + timedelta(days=2, weeks=3))))

t = datetime.now()-timedelta(weeks=1)
print(t)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: {0}!".format(s))

today = date.today()
april_fools_day = date(today.year, 4, 1)
if april_fools_day < today:
    print("April Fool's Day already went by, {0} days ago...".format((today-april_fools_day).days))
    april_fools_day = april_fools_day.replace(year=today.year+1)
    # Calculate the days until the next April Fool's day
    time_to_afd = april_fools_day-today
    print("It is just {0} days until April Fool' day!".format(time_to_afd.days))

# Working with calendars
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2017, 1, 0, 0)
print(st)

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2017, 1, 0, 0)
print(st)

# HTML
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print(st)

for i in c.itermonthdays(2017, 8):
    print(i)

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2019, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    # Another format of printing with variables (instead of using the format function)
    print("%10s %2d" % (calendar.month_name[m], meetday))


# Working with files
def main():
    # Open a file and create if it does not exist
    f = open("textfile.txt", "w+")

    # Write to the file
    for i in range(10):
        f.write("This is line {0} \r\n".format(i))

    # Close the file
    f.close()


if __name__ == "__main__":
    main()


def adding_data():
    # Open the file and append data to it
    f = open("textfile.txt", "a")
    # Write to the file
    for i in range(11, 20):
        f.write("This is line {0} \r\n".format(i))

    # Close the file
    f.close()


if __name__ == "__main__":
    adding_data()


def read_data():
    # Open the file and append data to it
    f = open("textfile.txt", "r")

    if f.mode == "r":
        contents = f.read()
        print(contents)

    # Close the file
    f.close()


if __name__ == "__main__":
    read_data()


def read_datalines():
    # Open the file and append data to it
    f = open("textfile.txt", "r")

    if f.mode == "r":
        fl = f.readlines()
        for x in fl:
            print(x)

    # Close the file
    f.close()


if __name__ == "__main__":
    read_datalines()


# Path and files
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    print(os.name)
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Items is a file: " + str(path.isfile("textfile.txt")))
    print("Items is a directory: " + str(path.isdir("textfile.txt")))
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    t = time.ctime(path.getmtime("textfile.txt"))
    print("Modification date of the file is: {0}".format(t))
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the file has been modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been {0} since the file was last modified\nor, {1} seconds!".format(td, str(td.total_seconds())))


if __name__ == "__main__":
    main()

# Use file system shell methods
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

if path.exists("textfile.txt"):
    src = path.realpath("textfile.txt")
    # dst = src + ".bak"

    # shutil.copy(src, dst)
    # shutil.copystat(src, dst)

    # os.rename("textfile.txt", "new_textfile.txt")
    # os.rename("new_textfile.txt", "textfile.txt")

    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("textfile.txt")


# Working with Web Data
import urllib.request


def main():
    web_url = urllib.request.urlopen("http://www.google.com")
    print("The resulted code is: {0}".format(str(web_url.getcode())))
    # 200 means that we have connected successfully

    data = web_url.read()
    print(data)


if __name__ == "__main__":
    main()


# JSON data
import urllib.request
import json


def print_results(data):
    json_format = json.loads(data)

    if "title" in json_format["metadata"]:
        print(json_format["metadata"]["title"])
        counter = json_format["metadata"]["count"]
        print("{0} events recorded".format(str(counter)))

    for i in json_format["features"]:
        print(i["properties"]["place"])
    print("-----------\n")


def main():
    url_data = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"

    # Open the url and read the data
    web_url = urllib.request.urlopen(url_data)
    print("The resulted code is: {0}".format(str(web_url.getcode())))
    # 200 means that we have connected successfully

    if(web_url.getcode() == 200):
        data = web_url.read()
        print_results(data)


if __name__ == "__main__":
    main()