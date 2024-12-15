# Assignemnt_3_2021173 
using docker to run spark
## step 1: pull spark image 
docker pull apache/spark-py
## step 2: Start Docker container:
Run the Docker container with the mounted volume: (dataset is from kaggle (netflix movies and tv))

docker run -it -v /home/zainab/Downloads:/data apache/spark-py
## step 3 test if pyspark available
python -c "from pyspark.sql import SparkSession"
## step 4 create eda_netflix.py file and run it 
spark-submit /home/zainab/Downloads/eda_netflix.py (run using this command)
or either cann directly run python script 

check spark_173.odt file for result






