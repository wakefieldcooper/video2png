import cv2
import os
import argparse 

def main():
    """Main processing loop that frames a video every X number of frames
    """
    try:
        if not os.path.exists('output'):
            os.makedirs('output')
    except OSError:
        print('Error: Creating Directory of Data')

    outputLocation = args.output
    # to read the video
    print('reading video')

    videoPath = args.input  # path to Video
    frame_set_no = args.frame_no
    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    print('Start framing')
    frameIndex = 0
    imageNo = 0
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_set_no)

    while(True):
        ret, frame = cap.read()
        frameIndex += 1
        if ret:
            if (frameIndex % 120 == 0):
                filename = outputLocation + '/{clip}_frame{frameNo}.png'.format(clip = videoPath.split('/')[-1][:-4], frameNo = str(imageNo)) #output path
                cv2.imwrite(filename, frame)
                imageNo += 1
                print("image: " + str(imageNo))
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("complete")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str,
                        default='data/input',
                        help='location of your input video file',
                        required=True)
    parser.add_argument('--output', type=str,
                        default='data/output',
                        help='Directory location you want your output pngs',
                        required=True)
    parser.add_argument('--frame_no', type=int,
                        default=100,
                        help='Every X number of frames to grab an image',
                        required=False)
    args = parser.parse_args()
    main()
