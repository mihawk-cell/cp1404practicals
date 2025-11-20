import datetime

FULL_COMPLETION = 100


class Project:
    def __init__(self, name="", start_date="", priority=int, cost=float, completion=0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost:,.2f}, {self.completion}"

    def is_complete(self):
        """Verify if the project is completed."""
        return int(self.completion) == FULL_COMPLETION

    def __lt__(self, other):
        """Less than, used for sorting project - by priority."""
        return self.priority <= other.priority

    def compared_date(self, input_date):
        """Compare the user_input date with project start date."""
        input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y")
        return self.start_date >= input_date

    def update_percentage(self, value):
        """Update the project completion percentage."""
        self.completion = value

    def update_priority(self, value):
        """Update the project priority."""
        self.priority = value

