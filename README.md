Description:
In a Data Warehouse, upstream sends out data that needs to be stored in different tables.
These tables can have multiple attributes having different types of data.
Also, in every release there are attribute changes happening in the metadata as per business communications.
For anyone to get the latest details of a table and its content, a Metadata sheet needs to be maintained by the Modeller of the Data Warehouse.
In our project, these details were maintained in an Excel sheet and were having some drawbacks:
    1. As the size of excel sheet increased, the process became slow as it was not able to handle huge amount of data.
    2. Filtering down of required data was comparatively slower.
So, we came up with an idea of moving all the Metadata details to a Database, and create a GUI using python to handle the upcoming changes in data.
This program has below functionalities:
    1. Insert new attribute and table details
    2. Delete old records
    3. Update old records
    4. Duplicate records cannot be inserted
Advantages:
    1. Quick and easy maintenance of Metadata details
    2. Secured user access
    3. Simple visualization of records
Tools used:
Python and SQL
Packages used in Python:
Tkinter and sqlite3
