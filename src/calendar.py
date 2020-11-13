from datetime import date as Date, timedelta
from docx import Document

class Calendar:
    def __init__(self, date: Date):
        self._date = date
    
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

class MonthlyCalendar(Calendar):
    def __init__(self, date: Date, start_day: int=6):
        super().__init__(date)
        self._start_day = start_day
    
    @staticmethod
    def nextDate(date: Date) -> Date:
        if date.month == 12:
            return Date(date.year + 1, 1, 1)
        else:
            return Date(date.year, date.month + 1, 1)

class WeeklyCalendar(Calendar):
    def __init__(self, date: Date):
        super().__init__(date)
    
    @staticmethod
    def nextDate(date: Date) -> Date:
        return date + timedelta(days=7)

class YearlyCalendar(Calendar):
    def __init__(self, date):
        super().__init__(date)
    
    @staticmethod
    def nextDate(date: Date) -> Date:
        return Date(date.year + 1, date.month, 1)