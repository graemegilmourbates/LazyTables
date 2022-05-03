import os

class DataType:
    #STRING TYPES:
        #CHAR(size)
        #VARCHAR(size)
        #BINARY(size)
        #VARBINARY(size)
        #TINYBLOB
        #TINYTEXT
        #TEXT(size)
        #BLOB(size)
        #MEDIUMTEXT
        #MEDIUMBLOB
        #LONGTEXT
        #LONGBLOB
        #ENUM(val1, val2..)
        #SET(val1, val2..)
    #NUMERIC TYPES:
        #INT
        #TINTINT
        #SMALLINT
        #MEDIUMINT
        #BIGINT
        #FLOAT(M,D)
        #DOUBLE(M,D)
        #DECIMAL(M,D)
    #DATE TIME:
        #DATE in YYYY-MM-DD format
        #TIME in HH:MM:SS format
        #DATETIME in YYYY-MM-DD HH:MM:SS format
        #TIMESTAMP in YYYYMMDDHHMMSS
        #YEAR(M) stored as 2 digit or 4 digit year.

class LazyTable:
    fileDirectory = os.path.dirname(os.path.abspath(__file__))
    commandDirectory = os.path.abspath(os.getcwd())

    def gen_schema_file(database, destination=fileDirectory, tableName=self.name):
        """(string, string, string) -> void
        Given a database, directory and a name, this function will produce
        and sql schema file for a table with this objects properties.
        The table name will be pulled from self.name
        All of the columns will be formatted from self.columns
        """
        fileString = ""
        filePath = destination
        fileName = tableName

        createTablestr = ("CREATE TABLE IF NOT EXISTS `%s`.`%s`" %
            database, tableName )
        fileString = fileString + createTablestr
        #Iterate and add columns
        for column in self.columns:
            #format is:
            #`fieldname` datatype [optional parameters]

            columnstr = ("`%s` %s %s")

    def format_columns(columns):
        """(dictionary) -> void
        Given a dictionary representing sql table columns. This
        funciton will format the dictionary replacing user inputs
        with proper data types from the data type class.
        """
        pass

    def migrate_schema(database):
        """(string) -> void
        Migrates schema for table onto given database
        """
        pass

    def pull_entries(database):
        """(string) -> dictionary
        Pulls all entries from self titled table in database.
        Formats into json
        """
        pass

    def pass_columns():
        """(null) -> dictionary
        Outputs current columns.
        """
        pass

    def add_column(name, type):
        """(string, DataType) -> void
        Adds a new column.
        """
        pass

    def remove_column(name):
        """(string) -> void
        Removes column with given 'name'
        """
        pass

    def remove_entry(id):
        """(int) -> void
        given entry id, remove from self.entries
        """
        pass

    def add_entry(entry):
        """(dict) -> void
        Adds and entry to self.entries
        """
        pass

    def push_entries(database):
        """(string) -> void
        adds entries to database.
        """

    def __init__(self, name, columns={}):
        self.name=name
        self.columns=columns
        self.format_columns(self.columns)
        self.entries={}
