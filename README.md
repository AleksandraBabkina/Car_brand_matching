# Car_brand_matching

## Description

This script is used for performing fuzzy matching between vehicle model data and categories in a database. The script retrieves data from an Oracle database, applies fuzzy string matching to identify models that are similar to predefined ones, and then updates the `CATEGORY` field in the database based on the matched models. Additionally, it generates SQL statements for updating the records and for retrieving records with missing categories.

## Functional Description

The script follows these main steps:
1. **Database Connection**: Establishes a connection to an Oracle database using SQLAlchemy and Oracle's `oracledb` module.
2. **Query Execution**: Executes SQL queries to retrieve vehicle model and category data from the database.
3. **Fuzzy Matching**: Uses the `fuzzywuzzy` library to perform fuzzy string matching to identify vehicle models from the database that closely match a set of predefined models.
4. **Data Update**: Updates the `CATEGORY` field in the database based on the fuzzy matching results.
5. **SQL Generation**: Generates SQL `UPDATE` statements for updating the category information in the database, and a `SELECT` query for fetching records with missing categories.
6. **Commit to Database**: The updated data is committed back to the database for persistence.

## Input Structure

1. **Database Connection**:
    - `username`: Username for the Oracle database connection.
    - `password`: Password for the Oracle database connection.
    - `dsn`: Data Source Name for the Oracle database.

2. **Predefined Model Data**: 
    - The predefined models and their associated categories are retrieved from the `category_mark_model` table in the database.

3. **Target Data**: 
    - The `al_babkina_bs_ts_2021_2024` table contains records that may have missing categories, which will be updated based on fuzzy matching.

## Technical Requirements

1. **Libraries**:
   - `SQLAlchemy`: For connecting to the Oracle database and executing queries.
   - `pandas`: For data manipulation and SQL query results handling.
   - `oracledb`: Oracle database driver for SQLAlchemy.
   - `fuzzywuzzy`: For performing fuzzy matching on vehicle model names.
   - `re`: Regular expressions (used indirectly by `fuzzywuzzy`).

2. **Oracle Database**: The script connects to an Oracle database containing the tables `category_mark_model` (for models and categories) and `al_babkina_bs_ts_2021_2024` (for records with possible missing categories).

## Usage

1. Modify the `username`, `password`, and `dsn` values to connect to your Oracle database.
2. Ensure that the database contains the tables `category_mark_model` (for models and categories) and `al_babkina_bs_ts_2021_2024` (for records with possible missing categories).
3. Run the script. It will:
    - Perform fuzzy matching to update the `CATEGORY` field based on model names.
    - Print SQL `UPDATE` statements for the updates.
    - Print a `SELECT` query for retrieving records with missing categories.
    - Commit the updated data back into the database.

## Example Output

The script will print SQL statements to update the records:
