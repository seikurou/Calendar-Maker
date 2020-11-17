from datetime import date as Date, timedelta
from docx import Document

TEMPLATE_PATH = './Calendar-Maker/mysite/cal_maker/templates/'

class Calendar:
    def __init__(self, date: Date, template: str):
        self._date = date
        self._template = template

    @staticmethod
    def nextDate(date: Date) -> Date:
        """
        Returns a `date` representing a date that appears in the next calendar.
        For example, a monthly calendar with a month of January should return a
        `date` with a `month` of February of the same `year`, with an arbitrary `day`.
        """
        return date

    def makeDocument(self) -> Document:
        """
        Returns a docx `Document` containing a single calendar of the specified parameters
        for this particular Calendar object. This method should be overridden by the appropriate
        child class to handle the appropriate calendar template.
        """
        return Document()

    @staticmethod
    def nextDay(date: Date) -> Date:
        return date + timedelta(days=1)

    @staticmethod
    def prevDay(date: Date) -> Date:
        return date - timedelta(days=1)

class MonthlyCalendar(Calendar):
    def __init__(self, date: Date, template: str, start_day: int=6):
        super().__init__(date, template)
        self._start_day = start_day

    @staticmethod
    def nextDate(date: Date) -> Date:
        if date.month == 12:
            return Date(date.year + 1, 1, 1)
        else:
            return Date(date.year, date.month + 1, 1)

class WeeklyCalendar(Calendar):
    def __init__(self, date: Date, template: str, start_day: int=6):
        super().__init__(date, template)
        self._start_day = start_day
        self.setStartEndDate()

    def setStartEndDate(self) -> None:
        date = self._date
        while date.weekday() != self._start_day:
            date = Calendar.prevDay(date)
        self._date_start = date
        self._date_end = date + timedelta(days=6)

    @staticmethod
    def nextDate(date: Date) -> Date:
        return date + timedelta(days=7)

class YearlyCalendar(Calendar):
    def __init__(self, date, template: str):
        super().__init__(date, template)

    @staticmethod
    def nextDate(date: Date) -> Date:
        return Date(date.year + 1, date.month, 1)