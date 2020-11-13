from datetime import date as Date, timedelta
from docx import Document

class Calendar:
    def __init__(self, date):
        self._date = date
    
    def nextDate(date):
        return date
    
    def makeDocument():
        return Document()

class MonthlyCalendar(Calendar):
    def __init__(self, date):
        super().__init__(date)
    
    def nextDate(date):
        if date.month == 12:
            return Date(date.year + 1, 1, 1)
        else:
            return Date(date.year, date.month + 1, 1)

class WeeklyCalendar(Calendar):
    def __init__(self, date):
        super().__init__(date)
    
    def nextDate(date):
        return date + timedelta(days=7)

class YearlyCalendar(Calendar):
    def __init__(self, date):
        super().__init__(date)
    
    def nextDate(date):
        return Date(date.year + 1, date.month, 1)