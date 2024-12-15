from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("NetflixEDA").getOrCreate()

df = spark.read.csv("/data/netflix_titles.csv", header=True, inferSchema=True)
df.show(5)  # Display the first 5 rows
# Print Schema
df.printSchema()

# Show basic statistics
df.describe().show()

# Count rows
print(f"Row count: {df.count()}")


# Group by Genre
df.groupBy("listed_in").count().orderBy("count", ascending=False).show()

# Yearly Trends
df.groupBy("release_year").count().orderBy("release_year").show()

# Stop Spark
spark.stop()
