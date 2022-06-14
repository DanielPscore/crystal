import kfp
import kfp.components as comp



# First function
def inf(image_path: str, output_string: comp.OutputPath(str)):
    import ObjectDetection as objd
    import cv2
    # from Communication import *
    from Upload import upload_simple
    import YouGet
    # Download image
    path = YouGet.download(image_path,"test", objd.config.workin_dir+"/Data", ".jpeg")
    # read and inference
    img = cv2.imread(path)
    r = objd.person(img)
    inf = objd.plot_many_box(img, r["bb"], label=["person"] * len(r["bb"]))
    cv2.imwrite("inf.jpeg", inf)
    url = upload_simple("inf.jpeg")

    # producer.publish_message({"inference":url})
    # Create Artifact : S3 path to uploded inf
    with open(output_string, 'w') as writer:
        writer.write(url)

# 2nd function
def print_url(url: comp.InputPath(str)):

    #print url
    with open(url, 'r') as reader:
        line = reader.readline()
        print(line)


# Link to your container image
base_img = "ultralytics/yolov5:latest"  # Change to your registry's URI

# Create first OP
make_inf = kfp.components.create_component_from_func(inf, base_image=base_img)

# Create second OP
do_print = kfp.components.create_component_from_func(print_url, base_image=base_img)


@kfp.dsl.pipeline( name='Sonalysis Object Detection', description='Sonalysis Object Detection')
def inf_upload(image_path):
    # Call the first OP
    first_task = make_inf(image_path)

    # Call the second OP and pass the first task's outputs
    second_task = do_print(first_task.outputs['output_string'])

