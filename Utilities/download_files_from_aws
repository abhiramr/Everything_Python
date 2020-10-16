import boto3
import os

# Never do this unless you're using it to validate data on a trusted system. 
# This kind of value setting is extremely irresponsible. 
os.environ['AWS_DEFAULT_REGION']="region"
os.environ["AWS_SECRET_ACCESS_KEY"]="aws_secret_access_key"
os.environ["AWS_ACCESS_KEY_ID"]="aws_access_key_id"
os.environ['BUCKET_NAME']='bucket_name'
# I've behaved very irresponsibly

cloud_storage_path = '<bucket_name>/<sub_folder_path>'

def download_objects_from_folder(prefix,dest_folder):
    try:
        s3_ = boto3.resource('s3')
        bucket_ = s3_.Bucket(os.environ['BUCKET_NAME'])
        objects = my_bucket.objects.filter(Prefix=prefix)
        print("Objects = {}".format(objects))
        for obj in objects:
            path, filename = os.path.split(obj.key)
            print(filename)
            bucket_.download_file(obj.key, os.path.join(dest_folder,str(filename) ))
    except Exception as e:
        print(e)

list_of_contents = download_objects_from_folder(os.path.join(cloud_storage_path, "some_prefix"),"/tmp/some_destination_folder_that_exists")
