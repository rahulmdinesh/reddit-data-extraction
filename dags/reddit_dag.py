
from datetime import datetime

from airflow.decorators import dag, task
import pandas as pd

from utils.constants import REDDIT_CLIENT_ID, REDDIT_SECRET_KEY, OUTPUT_PATH, AWS_BUCKET_NAME
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3_bucket


DEFAULT_START_DATE = datetime(2025, 1, 1)

default_args = {
    "owner": "Rahul M Dinesh",
    "start_date": DEFAULT_START_DATE,
}

@dag(
    dag_id="etl_reddit_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
    tags=["reddit", "etl", "pipeline"],
)
def reddit_data_pipeline():

    @task(task_id="reddit_extraction")
    def extract_from_reddit(file_name: str, subreddit: str, time_filter: str, limit: int) -> str:
        print("Connecting to reddit")
        instance = connect_reddit(REDDIT_CLIENT_ID, REDDIT_SECRET_KEY, "Data Engineering Project")

        posts = extract_posts(instance, subreddit, time_filter, limit)
        post_df = transform_data(posts) if not isinstance(posts, list) else transform_data(pd.DataFrame(posts))

        file_path = f"{OUTPUT_PATH}/{file_name}.csv"
        load_data_to_csv(post_df, file_path)

        print("Wrote CSV to %s", file_path)
        return file_path

    @task(task_id="s3_upload")
    def upload_to_s3(file_path: str):
        s3 = connect_to_s3()
        create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
        upload_to_s3_bucket(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])

    from datetime import datetime as _dt

    postfix = _dt.now().strftime("%Y%m%d")
    file_name = f"reddit_{postfix}"

    csv_path = extract_from_reddit(file_name=file_name, subreddit="dataengineering", time_filter="day", limit=100)
    upload_to_s3(csv_path)

reddit_data_pipeline()
