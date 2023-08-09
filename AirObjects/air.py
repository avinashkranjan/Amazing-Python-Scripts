import cv2
from InitCaffe import *

# Open video
# cap = cv2.VideoCapture('NASA_video1.mp4') # video with airplane.

# patch_size = 15 # Size of image patch to extract around featuns points
patch_size = 25  # Size of image patch to extract around feature points


count = 0  # Loop counter to control frequency of object recognition
objfreq = 5  # Frequence of object recognition
# NumCorners = 50 # Number of corners to extract in a given frame
NumCorners = 10  # Number of corners to extract in a given frame
'''
# fourcc = cv2.cv.CV_FOURCC(*'XVID')
# out = cv2.VideoWriter('result.avi', fourcc, 20.0, (450,170))
# Read each frame of video and do object recognition at specified frequency
while(cap.isOpened()):
    carNum = 0 # Number of cars detected
    # Read frame
    ret, frame = cap.read()
    # Resize each frame to a smaller size for speed
    frame = cv2.resize(frame,(500, 300), interpolation = cv2.INTER_CUBIC)
    #frame = frame[260:450,200:700]
    # Implement object recognition at specified frequency
    if count%objfreq == 0:
'''
# frame = cv2.imread('patch8901.png')
frame = cv2.imread('frame184.png')
# frame = cv2.imread('patch1.png')
if 1:
    if 1:
        # Convert to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find corners in gray scale image
        corners = cv2.goodFeaturesToTrack(gray, NumCorners, 0.01, 100)
        print 'The corners are:', corners
        corners = np.int0(corners)

        # For each corner found, extract a patch and classify patch
        for j, i in enumerate(corners):
            x, y = i.ravel()
            # cv2.circle(frame,(x,y),3,255,-1)
            print 'The x pos of the corner is: ', x
            print 'The y pos of the corner is: ', y
            print 'The i of the corners is: ', i
            print 'The j of the corners is: ', j
            # Define size of patch in image coordinates
            xstart = x - patch_size
            xend = x + patch_size
            ystart = y - patch_size
            yend = y + patch_size

            # clip image patch based on image size
            xlen = frame.shape[1]
            ylen = frame.shape[0]

            if xend > xlen:
                xend = xlen
            if xstart < 0:
                xstart = 0

            if yend > ylen:
                yend = ylen
            if ystart < 0:
                ystart = 0

            cv2.rectangle(frame, (xstart, ystart),
                          (xend, yend), (255, 0, 0), 2)
            # Extract the image patch from each frame in the video
            img_patch = frame[ystart:yend, xstart:xend]

            # Transform image to use caffe library
            transformed_image = transformer.preprocess('data', img_patch)

            # copy the image data into the memory allocated for the net
            net.blobs['data'].data[j, :, :, :] = transformed_image

        # perform classification
        output = net.forward()

        # Go through image patch for each corner and find if there are any airplanes
        Position = []
        for i, j in enumerate(corners):
            x, y = j.ravel()
            output_prob = output['prob'][i]

            # sort top five predictions from softmax output
            # top_inds = output_prob.argsort()[::-1][:5]  # reverse sort and take five largest items
            # reverse sort and take five largest items
            top_inds = output_prob.argsort()[::-1][:10]
            print 'The classes are:', top_inds
            # print 'predicted class is:', output_prob.argmax()
            # print 'output label:', labels[output_prob.argmax()]
            # print 'prob', output_prob[top_inds[0]]

            # If airlane, record position to draw bounding box

            # Airplane label ids in caffe database
            AirplaneLabels = [895, 404, 405, 812]
            # 437,566,556,570,706,735,752,818,830,848
            # VehicleLabels = [867,717,675,757,569,734,751,817,864,656] # Car, truck, van label ids in caffe database
            # for k in range (0,5):
            for k in range(0, 10):
                if (top_inds[k] in AirplaneLabels):
                    if output_prob[top_inds[0]] > 0.0:
                        print 'Shown class is:', top_inds[k]
                        print 'output label:', labels[top_inds[k]]
                        print 'prob', output_prob[top_inds[k]]
                        Position.append((x, y))
#                        carNum = carNum + 1
                   #     break
        # Draw rectangles around each airplane
        # print 'The number of cars detected are:', carNum
        print 'The number of frame is:', count+1
        for pos in Position:
            xpos = pos[0]
            ypos = pos[1]
            cv2.rectangle(frame, (xpos-patch_size, ypos-patch_size),
                          (xpos+patch_size, ypos+patch_size), (0, 255, 0), 2)
           # break
        # out.write(frame)
        cv2.imshow('frame', frame)
        cv2.waitKey()
    # Show image frame on screen
    count = count + 1
    # out.write(frame)
    # cv2.imshow('frame',frame)
    # cv2.waitKey()
'''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count > cap.get(7)/2:
        break
'''
# out.release()
cap.release()
cv2.destroyAllWindows()
