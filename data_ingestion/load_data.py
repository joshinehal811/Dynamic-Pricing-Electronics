# data_ingestion/load_data.py

from pyspark.sql import SparkSession

def load_events_to_bronze():
    """
    Load ecommerce events data into Bronze Delta table.
    """

    spark = SparkSession.builder.getOrCreate()

    try:
        print("Reading events.csv from DBFS...")
        df = (
            spark.read.option("header", True)
            .option("inferSchema", True)
            .csv("/FileStore/ecommerce_data/events.csv")
        )

        row_count = df.count()
        if row_count == 0:
            raise ValueError("No data found in events.csv")

        print(f"Loaded {row_count} rows.")

        print("Writing to Bronze Delta table: retail_bronze.events...")
        df.write.mode("overwrite").format("delta").saveAsTable("retail_bronze.events")

        print("Data ingestion complete: retail_bronze.events ready.")

    except Exception as e:
        print(f"Error during data ingestion: {str(e)}")
        raise

if __name__ == "__main__":
    load_events_to_bronze()
