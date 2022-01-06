"""
    ? 🎯  @author: Baimam Boukar JJ
    ? 🎯  @contact: (+237) 690535759
    ? 🎯  @email: baimamboukar@gmail.com
    ? 🎯  @github: www.github.com/baimamboukar
    ? 🎯  @linkedin: www.linkedin.com/in/baimamboukar

"""


class DataCleaner():
    """
        DATA CLEANER
        *! This class automates your daily csv and excel data cleaning tasks !*
    """

    def __init__(self, csv_file, excel_file, to_clean_column_index, to_replace, replace_with) -> None:
        """
        ✨✨✨ CONSTRUCTOR OF CLASS DATACLEANER✨✨✨

        🎯 Summary: Constructor of class datacleaner.This function will be automatically called whenever the class DataCleaner is instanciated
        📑 Arguments:
            📌 csv_file(String) :=> Path of the csv file to clean
            📌 excel_file(String):=> Path of the excel file to clean
            📌 to_clean_column_index(String):=> Index of the column to clean in the files
            📌 to_replace(String):=> String to replace in the column's data
            📌 replace_with(String):=> New value to assign to column's data
        """
        self.csv_file = csv_file
        self.excel_file = excel_file
        self.to_clean_column_index = to_clean_column_index
        self.to_replace = to_replace
        self.replace_with = replace_with

    def load_excel_file(self):
        """
        ✨✨✨ LOAD EXCEL FILE ✨✨✨

        🎯 Summary: This method will load the excel file using openpyxl and return the data
        📑 Arguments:
            📌 self(Object Reference) :=> Object reference of the class
        """
        import openpyxl
        return openpyxl.load_workbook(self.excel_file)

    def load_csv_file(self):
        """
        ✨✨✨ LOAD CSV FILE ✨✨✨

        🎯 Summary: This method will load the csv file using csv and return the data
        📑 Arguments:
            📌 self(Object Reference) :=> Object reference of the class
        """
        with open(self.csv_file, 'r') as f:
            import csv
            reader = csv.reader(f)
            data = list(reader)
        return data

    def clean_csv_file(self, data):
        """
        ✨✨✨ LOAD EXCEL FILE ✨✨✨

        🎯 Summary: This method cleans loaded csv file and returns the clean data
        📑 Arguments:
            📌 self(Object Reference) :=> Object reference of the class
            📌 data(List) :=> List of data to clean
        """
        for row in data:
            if(str(row[self.to_clean_column_index]).endswith(self.to_replace)):
                row[self.to_clean_column_index] = row[self.to_clean_column_index].replace(
                    self.to_replace, self.replace_with)
        return data

    def clean_excel_file(self, wb):
        """
        ✨✨✨ CLEAN EXCEL DATA ✨✨✨

        🎯 Summary: This method cleans the excel file and returns the clean data
        📑 Arguments:
            📌 self(Object Reference) :=> Object reference of the class
            📌 wb(Object) :=> Object of the excel file to clean
        """
        cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        # get the index of the cells to clean based on the provided column index
        index = cols[self.to_clean_column_index]
        # set the max row to clean
        maxrows = 30
        # get the range of cells to clean
        col = wb.active[index + "2:" + index + str(maxrows)]
        for cell in wb.active[index + "2:" + index + str(maxrows)]:
            for data in cell:
                email = str(data.value)
                if(email.endswith(self.to_replace)):
                    data.value = email.replace(
                        self.to_replace, self.replace_with)
        return wb

    def save_clean_excel(self, clean_sheet, file):
        """
        ✨✨✨ SAVE CLEAN EXCEL DATA ✨✨✨

        clean_sheet.save(file)Summary: This method writes the cleaned data to an excel file
        📑 Arguments:
            📌 self(Object Reference) :=> Object reference of the class
            📌 clean_sheet(Object) :=> Cleaned data to save
            📌 file(String) :=> Path of the excel file to write
        """
        clean_sheet.save(file)
        pass

    def save_clean_csv(self, file, data):
        """
        ✨✨✨ SAVE CSV CLEAN DATA ✨✨✨

        🎯 Summary: This method writes the cleaned data to a csv file
        📑 Arguments:
            📌 self(Object Reference) :=> Object reference of the class
            📌 file(String) :=> Path of the csv file to write
            📌 data(List) :=> Cleaned data to save

        """
        with open(file, 'w') as f:
            import csv
            writer = csv.writer(f)
            writer.writerows(data)


""" == == = DRIVER CODE == == =  """

if __name__ == "__main__":
    cleaner = DataCleaner("datasource/employee_database.csv",
                          "datasource/employee_database.xlsx", 3, "@helpinghands.cm", "@handsinhands.cm")
    loaded_csv_data = cleaner.load_csv_file()
    clean_csv_data = cleaner.clean_csv_file(loaded_csv_data)
    cleaner.save_clean_csv("cleandata/employee_database.csv", clean_csv_data)
    cleaner.load_excel_file()
    clean_excel_data = cleaner.clean_excel_file(cleaner.load_excel_file())
    cleaner.save_clean_excel(
        clean_excel_data, "cleandata/employee_database.xlsx")
