FROM apache/airflow:2.10.5
#RUN apt-get update && apt-get install -y nano
# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies, ensuring Airflow is installed with the same version
RUN pip install --no-cache-dir apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
