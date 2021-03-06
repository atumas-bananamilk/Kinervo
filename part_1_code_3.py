import pykinect                                                             # Importing Python library for Kinect from pykinect
import nui                                                                  # Importing Python library for Kinect
import time

kinect = nui.Runtime()
kinect.skeleton_engine.enabled = True                                       # We will only be detecting our skeleton
                                                                            # (all other engines are disabled)
while (1==1):
    frame = kinect.skeleton_engine.get_next_frame()                         # Getting only 1 frame
    for skeleton in frame.SkeletonData:                                     # We check frame's skeleton data
        if skeleton.eTrackingState == nui.SkeletonTrackingState.TRACKED:    # Check if skeleton is set as TRACKED
            coordinates = str(skeleton.position)                            # skeleton.position returns our coordinates
            print coordinates

    time.sleep(0.1)                                                         # This is where we define the rate frames are being sent (0.1s)