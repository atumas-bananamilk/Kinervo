import pykinect                                         # Importing Python library for Kinect from pykinect
import nui                                              # Importing Python library for Kinect
import time

kinect = nui.Runtime()
kinect.skeleton_engine.enabled = True                   # We will only be detecting our skeleton
														# (all other engines are disabled)
while (1==1):
    frame = kinect.skeleton_engine.get_next_frame()     # Getting only 1 frame
    for skeleton in frame.SkeletonData:                 # We check frame's skeleton data
        print skeleton

    time.sleep(0.1)                                     # This is where we define the rate frames are being sent (0.1s)