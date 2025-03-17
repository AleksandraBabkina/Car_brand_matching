# Car_brand_matching
## Description
This script is designed to match car model names between two datasets, performing fuzzy matching and updating relevant categories based on matched data. It pulls data from an Oracle database, applies fuzzy matching to identify similar car model names, and then updates categories for matching entries. This process helps standardize and enrich data by ensuring that car models from one dataset are correctly linked to their categories from another dataset. The script enhances the quality and consistency of automotive-related data for further analysis or reporting.

## Functional Description
The script performs the following key operations:
1. Retrieves car model data from two distinct datasets.
2. Compares the car models from both datasets using fuzzy string matching algorithms to find the closest matches.
3. Identifies the corresponding categories for matched models.
4. Updates the category column for each matching entry.
5. Outputs the SQL update commands for applying these changes to the database.
6. Generates queries for reviewing the updated data.
7. Ensures that both exact and fuzzy matches are handled appropriately, improving data accuracy.

## How It Works
1. The script connects to an Oracle database and retrieves car model information from two specific tables: one for a list of car categories and models, and another for raw model data.
2. It uses the fuzzy matching library (Fuzzywuzzy) to compare car model names between the two datasets.
3. For each match found, it assigns the correct category to the model.
4. The script generates SQL statements that can be used to update the database with the correct category information for each matched model.
5. It displays the SQL statements and other relevant queries for validation and further processing.
6. Finally, the script outputs SQL queries for selecting the updated records.

## Input Structure
To run the script, the following inputs are required:
1. **Database Credentials**: Username, Password, and DSN (Data Source Name) for connecting to the Oracle database.
2. **Model Data**: The car models to be matched along with their categories from two different tables in the database.

## Technical Requirements
To run the script, the following are necessary:
1. Python 3.x
2. Required Python libraries:
   - SQLAlchemy
   - Pandas
   - Fuzzywuzzy
   - Oracle DB (oracledb)
3. An Oracle Database with the following tables:
   - `diasoft_test.v_category_mark_model` (contains car models and their categories)
   - `al_babkina_bs_ts_2021_2024` (contains car models to be updated)

## Usage
1. Modify the database credentials (username, password, DSN) to connect to your Oracle database.
2. Define the query for retrieving the necessary data (both car models and categories).
3. Run the script. It will:
   - Match car models from both datasets using fuzzy matching.
   - Identify and update the relevant categories.
   - Output SQL update commands for applying changes to the database.

## Example Output
The script will output:
1. SQL UPDATE statements to update the category for matched car models.
2. SQL SELECT queries to review the records where the car models have been matched and updated.
3. It will print the models and their assigned categories for reference.

Example of SQL Output:
```sql
UPDATE al_babkina_bs_ts SET CATEGORY = 'SUV' WHERE BRAND_MODEL = 'Toyota Highlander';
UPDATE al_babkina_bs_ts SET CATEGORY = 'Sedan' WHERE BRAND_MODEL = 'Honda Accord';
