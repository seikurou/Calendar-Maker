# Calendar-Maker

Inspired by <a href=calendarsthatwork.com>Calendars That Work</a>

Allows you to create printable calendars in the docx format.

```
usage: main.py [-h] [--type {MonthlyLandscape}] [--year YEAR] [--month MONTH]
               [--day DAY] [--cnt CNT] [--startday {0,1,2,3,4,5,6}]
               [--filename FILENAME]

Create printable calendars.

optional arguments:
  -h, --help            show this help message and exit
  --type {MonthlyLandscape}
                        Type of calendar
  --year YEAR           Start year
  --month MONTH         Start month
  --day DAY             Start day
  --cnt CNT             Number of calendars
  --startday {0,1,2,3,4,5,6}
                        For monthly/weekly calendars, the day on which to
                        start, default Sunday (6). Mon, Tues, Wed... is 0, 1,
                        2...
  --filename FILENAME   Filename to save as, not including .docx
  ```
