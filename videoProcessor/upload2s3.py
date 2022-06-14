import Upload


def upload(team1, team2, minimap_video, objd_video,jsy,com,goals):
    team1_img, team2_img = Upload.uploadVideoS3(team1)["object_url"], Upload.uploadVideoS3(team2)["object_url"]
    minimap = Upload.uploadVideoS3(minimap_video)["object_url"]
    objd = Upload.uploadVideoS3(objd_video)["object_url"]
    js= Upload.uploadVideoS3(jsy)["object_url"]
    co=Upload.uploadVideoS3(com)["object_url"]
    try:
        goal = Upload.uploadVideoS3(goals)["object_url"]
    except:
        goal = ""
    return team1_img, team2_img, minimap, objd,js,co,goal


def upload_simple(e):
    f = Upload.uploadVideoS3(e)["object_url"]
    return f