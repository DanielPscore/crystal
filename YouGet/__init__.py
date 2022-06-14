import os

def download(link, filename = 'output', path_location = 'videos', fileformat = '.mp4'):
    "you-get --itag=18 -o videos -O trial 'https://www.youtube.com/watch?v=jNQXAC9IVRw'" #download as .mp4

    if fileformat == '.mp4':
        data = "you-get --itag=18 -o {0} -O {1} {2}".format(path_location, filename, link)
    else:
        data = "you-get -o {0} -O {1} {2}".format(path_location, filename, link)

    try:
        os.system(data)
        return path_location+"/"+filename+fileformat, True
    except Exception as e:
        print(e)
        print("Something went wrong, Ensure you-get is installed on your system")

        return "", False
