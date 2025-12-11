# Data Pipeline to Extract Data from Reddit using Apache Airflow and upload to AWS S3 and analyze data using AWS Glue, Athena and Redshift

This project constructs an ETL Pipeline that is orchestrated using Apache Airflow, to extract data from Reddit and then upload it to AWS S3. After uploading the data, we analyze and visualize the data using tools like AWS Glue, Athena and Redshift

## Prerequisites

- AWS Account with valid access and secret keys
- Reddit Account with valid client and secret keys
- Docker
- Python 3

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

```bash 
git clone https://github.com/rahulmdinesh/reddit-data-extraction.git
cd reddit-data-extraction
```

2. Create a virtual environment

```bash 
python -m venv .venv  
```

3. Activate the virtual environment

```bash 
source .venv/bin/activate  
```

4. Install the dependencies
```bash
pip install -r requirements.txt
```

5. Add the required API keys to the `config/config.conf` file

6. Start the containers using Docker Compose
```bash
docker-compose up -d
```

7. Launch the Airflow Web UI to trigger DAG runs
```bash
open http://localhost:8080
```

## Screenshots

Apache Airflow Web UI:
<img width="1728" height="866" alt="image" src="https://github.com/user-attachments/assets/1b04810b-69df-4db0-84cc-4c001e42caf6" />

Data file uploaded to AWS S3 bucket:
<img width="3456" height="1736" alt="image" src="https://github.com/user-attachments/assets/3a145137-1a1e-4c0d-875d-fa781aa2de4f" />

Querying table using AWS Athena after AWS Glue Crawler Job
<img width="1728" height="906" alt="image" src="https://github.com/user-attachments/assets/eb1c063a-af4e-48b3-b7c7-8568137cb609" />
