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
    def gen_schema_file():
        pass

    def migrate_schema():
        pass

    def pull_columns():
        pass

    def add_column():
        pass

    def remove_column():
        pass

    def remove_entry():
        pass

    def add_entry():
        pass
