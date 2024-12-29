"""app.py"""

from data.raw.raw import extract_data_from_url
from models.models import insert_data_from_dataframe
from data.procesed.procesed import (
    bytes_to_dataframe,
    rename_columns,
    remove_columns,
    convert_columns_to_date,
    convert_columns_to_float,
)
# from models import insert_into_supabase
# from database import create_supabase_client


def main():
    """Main function to fetch, prepare and insert data into Supabase."""

    try:
        data = extract_data_from_url()
        df = bytes_to_dataframe(data)
        rename = rename_columns(df)
        dropper = remove_columns(rename, "Hora.de.publicación")
        dates = convert_columns_to_date(dropper, ["date"])
        floats = convert_columns_to_float(dates, "date")

        insert_data_from_dataframe(floats)

    except Exception as e:
        print("Fallo la creacion del cliente", {e})


if __name__ == "__main__":
    main()
