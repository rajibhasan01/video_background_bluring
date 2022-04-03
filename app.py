import cv2
import time
import os

fps = 0;

def video_to_frames(input_loc, output_loc):
    global fps;
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("Number of FPS: ", fps)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break
    

if __name__=="__main__":

    input_loc = '/home/rajibhasan/Desktop/test_video/videos/test.mp4'
    output_loc = '/home/rajibhasan/Desktop/test_video/frames'
    video_to_frames(input_loc, output_loc);
    
    try:
        os.system("rembg p /home/rajibhasan/Desktop/test_video/frames /home/rajibhasan/Desktop/test_video/removed_bg_frames");
    except:
        print('could not execute command');
        
        
    image_folder = '/home/rajibhasan/Desktop/test_video/removed_bg_frames'
    video_name = '/home/rajibhasan/Desktop/test_video/video.mp4'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'MPEG')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
        
    
        