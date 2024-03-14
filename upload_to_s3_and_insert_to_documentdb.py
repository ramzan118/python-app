
#(upload_to_s3_and_insert_to_documentdb.py):
# Import necessary libraries
import boto3
import pymongo
import os
import datetime

# Function to upload file to S3 bucket
def upload_to_s3(file_path, bucket_name, object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_path, bucket_name, object_name)
        print("File uploaded successfully to S3 bucket!")
        return True
    except Exception as e:
        print(f"Error uploading file to S3 bucket: {e}")
        return False

# Function to insert metadata into DocumentDB
def insert_to_documentdb(file_name, file_size, upload_time):
    # Connect to DocumentDB
    client = pymongo.MongoClient(os.environ['MONGODB_URI'])
    db = client[os.environ['MONGODB_DATABASE']]
    collection = db[os.environ['MONGODB_COLLECTION']]
    try:
        document = {
            'filename': file_name,
            'size': file_size,
            'upload_time': upload_time
        }
        collection.insert_one(document)
        print("Metadata inserted into DocumentDB successfully!")
        return True
    except Exception as e:
        print(f"Error inserting metadata into DocumentDB: {e}")
        return False

# Main function to upload file to S3 and insert metadata into DocumentDB
def main():
    # File path
    file_path = os.environ['FILE_PATH']
    
    # S3 bucket details
    bucket_name = os.environ['S3_BUCKET_NAME']
    object_name = os.path.basename(file_path)
    
    # Upload file to S3
    if upload_to_s3(file_path, bucket_name, object_name):
        # Get file metadata
        file_size = os.path.getsize(file_path)
        upload_time = datetime.datetime.now()
        
        # Insert metadata into DocumentDB
        insert_to_documentdb(object_name, file_size, upload_time)

# Execute main function
if __name__ == "__main__":
    main()

