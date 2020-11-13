import argparse
from docx import Document
from docxcompose.composer import Composer
from datetime import date as Date

CALENDAR_TYPES = {'MonthlyLandscape': MonthlyLandscape}

def makeCalendarCollection(args):
    Calendar = CALENDAR_TYPES[args.type]
    currDate = Date(args.year, args.month, args.day)
    calendarCollection = []
    for i in range(args.cnt):
        calendarCollection.append(Calendar(currDate))
        currDate = Calendar.nextDate(currDate)

def mergeDocuments(documents):
    if not documents:
        return
    composer = Composer(documents[0])
    for doc in range(1, len(documents)):
        composer.append(doc)
    return composer

def main(args):
    calendarCollection = makeCalendarCollection(args)
    composer = mergeDocuments(map(lambda x : x.makeDocument(), calendarCollection))
    composer.save(args.filename + '.docx')

if __name__ == "__main__":
    assert CALENDAR_TYPES
    parser = argparse.ArgumentParser(description='Create printable calendars.')
    parser.add_argument('--type', type=str, nargs=1, choices=CALENDAR_TYPES.keys(), default=CALENDAR_TYPES.keys()[0],
                    help='Type of calendar',)
    parser.add_argument('--year', type=int, nargs=1, default=2020,
                                        help='Start year')
    parser.add_argument('--month', type=int, nargs=1, default=1,
                                        help='Start month')
    parser.add_argument('--day', type=int, nargs=1, default=1,
                                        help='Start day')
    parser.add_argument('--cnt', type=int, nargs=1, default=1,
                                        help='Number of calendars')
    parser.add_argument('--startday', type=str, nargs=1, default=6,
                                        help='For monthly/weekly calendars, the day on which to start, default Sunday (6). Mon, Tues, Wed... is 0, 1, 2...',
                                        choices=[0, 1, 2, 3, 4, 5, 6])
    parser.add_argument('--filename', type=int, nargs=1, default='calendar',
                                        help='Filename to save as, not including .docx')


    args = parser.parse_args()
    main(args)