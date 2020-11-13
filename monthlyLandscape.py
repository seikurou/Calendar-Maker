from docx import Document

class MonthlyLandscape(MonthlyCalendar):
    def __init__(self, date):
        super().__init__(date)