# feature_engineering/feature_engineering.py

from pyspark.sql import SparkSession, functions as F

def create_product_features():
    """
    Create product-level features (purchase counts, price stats) for modeling.
    """

    spark = SparkSession.builder.getOrCreate()

    try:
        print("Loading events data from Bronze...")
        df = spark.table("retail_bronze.events")

        if df.count() == 0:
            raise ValueError("No events found in Bronze table.")

        purchase_df = df.filter(F.col("event_type") == "purchase")

        if purchase_df.count() == 0:
            raise ValueError("No purchase events found to engineer features.")

        product_features = (
            purchase_df.groupBy("product_id")
            .agg(
                F.count("*").alias("total_purchases"),
                F.avg("price").alias("avg_price"),
                F.max("price").alias("max_price"),
                F.min("price").alias("min_price"),
                F.stddev("price").alias("std_price"),
            )
        )

        if product_features.count() == 0:
            raise ValueError("Feature aggregation failed. No features created.")

        print(f"Created features for {product_features.count()} products.")

        print("Writing to Silver Delta table: retail_silver.product_features...")
        product_features.write.mode("overwrite").format("delta").saveAsTable("retail_silver.product_features")

        print("Feature engineering complete: retail_silver.product_features ready.")

    except Exception as e:
        print(f"Error during feature engineering: {str(e)}")
        raise

if __name__ == "__main__":
    create_product_features()
