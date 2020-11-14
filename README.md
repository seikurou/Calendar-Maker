# Calendar-Maker

Inspired by <a href="https://calendarsthatwork.com" target="_blank">Calendars That Work</a>

Allows you to create printable calendars in the docx format.

```
usage: main.py [-h] [--template {MonthlyLandscape.docx,WeeklyPortrait.docx}]
               [--year YEAR] [--month MONTH] [--day DAY] [--cnt CNT]
               [--start_day {0,1,2,3,4,5,6}] [--filename FILENAME]
main.py: error: unrecognized arguments: asd
PS C:\Users\edmon\Desktop\Calendar-Maker> python .\main.py -h
usage: main.py [-h] [--template {MonthlyLandscape.docx,WeeklyPortrait.docx}]
               [--year YEAR] [--month MONTH] [--day DAY] [--cnt CNT]
               [--start_day {0,1,2,3,4,5,6}] [--filename FILENAME]

Create printable calendars.

optional arguments:
  -h, --help            show this help message and exit
  --template {MonthlyLandscape.docx,WeeklyPortrait.docx}
                        Type of calendar
  --year YEAR           Start year
  --month MONTH         Start month
  --day DAY             Start day
  --cnt CNT             Number of calendars
  --start_day {0,1,2,3,4,5,6}
                        For monthly/weekly calendars, the day on which to
                        start, default Sunday (6). Mon, Tues, Wed... is 0, 1,
                        2...
  --filename FILENAME   Filename to save as
  ```
