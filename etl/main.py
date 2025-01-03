"""main.py"""

import os
from dotenv import load_dotenv
from database.supabasedb import supabase_client
from database.supabase_insertion import insert_data_from_dataframe
from data.raw.raw import extract_data_from_url
from data.procesed.procesed import (
    bytes_to_dataframe,
    rename_columns,
    remove_columns,
    convert_columns_to_date,
    convert_columns_to_float,
    remove_duplicates,
)


def main():
    """Main function to fetch, prepare, and insert data into Supabase."""

    try:
        load_dotenv()

        table_name = os.getenv("SUPABASE_TABLE")

        data = extract_data_from_url()
        df = bytes_to_dataframe(data)
        rename = rename_columns(df)
        dropper = remove_columns(rename, "Hora.de.publicación")
        dates = convert_columns_to_date(dropper, ["date"])
        floats = convert_columns_to_float(dates, "date")
        duplicates = remove_duplicates(floats)

        insert_data_from_dataframe(duplicates, supabase_client(), table_name)

    except Exception as e:
        print("Failed to create the Supabase client", {e})


if __name__ == "__main__":
    main()
