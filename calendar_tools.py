from datetime import date, datetime

class UkrainianCalendar:
    def get_holiday_list(self):
        return [
            "01-01",  # Новий рік
            "07-01",  # Різдво
            "08-03",  # Міжнародний жіночий день
            "01-05",  # День праці
            "09-05",  # День Перемоги
            "28-06",  # День Конституції
            "24-08",  # День Незалежності
        ]

    def is_working_day(self, date_obj):
        holidays = self.get_holiday_list()
        if date_obj.weekday() >= 5:
            return False
        return date_obj.strftime("%d-%m") not in holidays

