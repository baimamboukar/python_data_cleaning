class Autopytion:
    def __init__(self, file):
        self.file = file

    @staticmethod
    def read_file(self):
        """
            ///******READS THE CSV FILE******///
        """
        with open('data/employees_database.csv', 'r') as f:
            import csv
            reader = csv.reader(f)
            data = list(reader)
        return data

    @staticmethod
    def update_emails_in_file(data, to_replace, replace_with):
        for row in data:
            if(str(row[3]).endswith(to_replace)):
                row[3] = row[3].replace(to_replace, replace_with)
        return data

    def report(self):
        """
            ///******REPORT******///
        """
        print("reports")

    @staticmethod
    def write_csv(data):
        with open('data/employees_database.csv', 'w') as f:
            import csv
            writer = csv.writer(f)
            writer.writerows(data)


data = Autopytion.read_file('data/employees_database.csv')
updated_data = Autopytion.update_emails_in_file(
    data, '@helpinghands.cm', '@handsinhands.cm')
Autopytion.write_csv(updated_data)
