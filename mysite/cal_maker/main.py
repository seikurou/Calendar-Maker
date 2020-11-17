import argparse
from docx import Document
from docxcompose.composer import Composer
from datetime import date as Date
import os
from .src.monthlyLandscape import MonthlyLandscape
from .src.weeklyPortrait import WeeklyPortrait

OUTPUT_DIR = './Calendar-Maker/mysite/cal_maker/output/'
CALENDAR_TYPES = {'MonthlyLandscape.docx': MonthlyLandscape,
                    'WeeklyPortrait.docx': WeeklyPortrait}

def makeCalendarCollection(args):
    Calendar = CALENDAR_TYPES[args.template]
    currDate = Date(args.year, args.month, args.day)
    calendarCollection = []
    for i in range(args.cnt):
        calendarCollection.append(Calendar(currDate, **vars(args)))
        currDate = Calendar.nextDate(currDate)
    return calendarCollection

def mergeDocuments(documents):
    if not documents:
        return
    composer = Composer(documents[0])
    for i in range(1, len(documents)):
        composer.append(documents[i])
    return composer

def main(args):
    calendarCollection = makeCalendarCollection(args)
    docs = [x.makeDocument() for x in calendarCollection]
    composer = mergeDocuments(docs)
    composer.save(OUTPUT_DIR + args.filename)

def make_calendar(args):
    main(args)

if __name__ == "__main__":
    assert CALENDAR_TYPES
    parser = argparse.ArgumentParser(description='Create printable calendars.')
    parser.add_argument('--template', type=str, nargs=1, choices=CALENDAR_TYPES.keys(), default='MonthlyLandscape.docx',
                    help='Type of calendar',)
    parser.add_argument('--year', type=int, nargs=1, default=2020,
                                        help='Start year')
    parser.add_argument('--month', type=int, nargs=1, default=11,
                                        help='Start month')
    parser.add_argument('--day', type=int, nargs=1, default=1,
                                        help='Start day')
    parser.add_argument('--cnt', type=int, nargs=1, default=2,
                                        help='Number of calendars')
    parser.add_argument('--start_day', type=str, nargs=1, default=6,
                                        help='For monthly/weekly calendars, the day on which to start, default Sunday (6). Mon, Tues, Wed... is 0, 1, 2...',
                                        choices=[0, 1, 2, 3, 4, 5, 6])
    parser.add_argument('--filename', type=str, nargs=1, default='calendar.docx',
                                        help='Filename to save as')


    args = parser.parse_args()
    main(args)