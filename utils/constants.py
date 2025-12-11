import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

#Reddit Keys
REDDIT_SECRET_KEY = parser.get('reddit_api_keys', 'reddit_secret_key')
REDDIT_CLIENT_ID = parser.get('reddit_api_keys', 'reddit_client_id')

#AWS
AWS_ACCESS_KEY_ID = parser.get('aws_api_keys', 'aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws_api_keys', 'aws_secret_access_key')
AWS_REGION = parser.get('aws_api_keys', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws_api_keys', 'aws_bucket_name')

OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)