import logging, boto3, sys, threading, requests, os, uuid
from botocore.exceptions import ClientError
from decouple import config

###################
access_key="AKIAUATJLZ6TPTG35KFW"
secret_key="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"
warehouse="s3a://parallelscore-staging/delta/videolake"
uploads="sonalysis-asset"
api_key="894291272153672"
api_secret="DNELrIT3lfziYb3u0HQsECDBv1E"
cloud_name="ogbanugot"
folder="sonalysis"
mongo_url="mongodb://sonauser:sona15230@api.sonalysis.io:27017/sonalysis"

###########



def check_str(obj):
    try:
        obj = obj.decode("utf-8")
    except (UnicodeDecodeError, AttributeError):
        pass
    return obj


def uploadS3_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    file_name = check_str(file_name)
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = "{0}.{1}".format(uuid.uuid4(), file_name.rsplit(".", 1)[-1])

    # Upload the file
    s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = "https://{0}.s3.amazonaws.com/{1}".format(
        uploads,
        object_name)

    try:
        s3_client.upload_file(file_name, uploads, object_name,
                              ExtraArgs={'ACL': 'public-read'},
                              Callback=ProgressPercentage(file_name))
    except ClientError as e:
        logging.error(e)
        return False
    return response


def uploadS3_fileObject(file, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        # object_name = "{0}_{1}".format(uuid.uuid4(),file.name)
        object_name = "{0}.{1}".format(uuid.uuid4(), file.name.rsplit(".", 1)[-1])

    # Upload the file
    s3_client = boto3.client('s3', access_key, aws_secret_access_key=secret_key)
    response = "https://{0}.s3.amazonaws.com/{1}".format(
        config("uploads"),
        object_name)

    try:
        s3_client.upload_fileobj(file, uploads, object_name,
                                 ExtraArgs={'ACL': 'public-read'},
                                 Callback=ProgressPercentage(file, True))
    except ClientError as e:
        logging.error(e)
        return False
    return response


def getpresignedurl(filename, bucket=uploads):
    s3_client = boto3.client('s3', access_key, secret_key)
    try:
        presigned_url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': filename},
                                                         ExpiresIn=100)
    except Exception as e:
        pass
    # print("[INFO] : The contents inside show_image = ", public_urls)
    return presigned_url


def uploadVideoS3(filename, fileobject=False):
    """This function is used to UPLOAD a video or file object to S3 and return object url."""
    if fileobject:
        object_url = uploadS3_fileObject(filename)
    else:
        object_url = uploadS3_file(filename)
    return {"object_url": object_url}


def downloadfromS3(media_url, save_directory):
    # print("\nDownloading video for processing.....")
    request = requests.get(media_url)

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    videoPath = f'{save_directory}/{media_url.rsplit("/", 1)[-1]}'

    with open(videoPath, 'wb') as f:
        f.write(request.content)
    # print("Done....")
    return videoPath


class ProgressPercentage(object):

    def __init__(self, filename, fileobject=False):
        if fileobject:
            self._filename = filename.name
            self._size = float(filename.size)
        else:
            self._filename = filename
            self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


if __name__ == "__main__":
    # response = uploadS3_file("psg_fcb_p.mp4")
    response = uploadS3_file(sys.argv[1])
    print(response)
