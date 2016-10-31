# Kinervo - Kinect & Servo system

![alt tag](http://aivarastumas.weebly.com/uploads/4/9/8/0/49800285/565978958.png)

# Kinervo tutorial
WARNING: We are going to be using Windows in this tutorial. <br />
WARNING: you need to know how to use Serial Monitor on Arduino IDE. <br />
WARNING: you need to know how to use servos on Arduino IDE. <br />

Let's send data from the Kinect straight to Arduino using Python and do some interesting stuff!

Part 1 - printing out OUR coordinates received by Kinect. <br />
Part 2 - sending our X coordinate to Arduino and pointing servo to that coordinate.

# PART 1

Let's do the following task:

        1. Kinect reads its sensor data
        2. If we are standing in front of the Kinect:
            Kinect prints out our coordinates
        Else:
            Nothing
        3. Repeats

In the end, our project should look like this (look at the servo's position while we move):

![alt tag](http://aivarastumas.weebly.com/uploads/4/9/8/0/49800285/285004249.png)
![alt tag](http://aivarastumas.weebly.com/uploads/4/9/8/0/49800285/790330456.png)
![alt tag](http://aivarastumas.weebly.com/uploads/4/9/8/0/49800285/623021031.png)

Kinect is normally being programmed in C/C++, but as we are using Python, we need to download several things:

        1. Windows Kinect SDK v1.8: http://www.microsoft.com/en-gb/download/details.aspx?id=40278
        2. pyKinect (Python library for Kinect): https://pypi.python.org/pypi/pykinect/1.0
        3. pip (used for installing pyKinect): https://bootstrap.pypa.io/get-pip.py (just save that text as "get-pip.py")

After downloading everything:

        1. Install the Windows Kinect SDK v1.8
        2. Then run in the terminal (to install pip):
            python get-pip.py
        3. Then run in the terminal (to install pyKinect):
            pip install pykinect

Done! Let's move on to coding.

Kinect's coordinate system is as follows:

![alt tag](http://aivarastumas.weebly.com/uploads/4/9/8/0/49800285/170839612.png)

In Kinect, all view of the camera is being sent by frames, so it's like taking pictures at our defined rate and sending them to us. <br />
Therefore, it depends on us what rate do we need. <br />
Let's test whether our Kinect returns our coordinates. Run this on VIDLE:

https://github.com/atumas-bananamilk/Kinervo/blob/master/part_1_code_1.py

Now you should see a lot of data being printed on the screen, and when you step in front of the camera, you should see that something changes. It prints out that skeleton changes from UNTRACKED to TRACKED.

Let's now print data only if we are standing in front of the camera:

https://github.com/atumas-bananamilk/Kinervo/blob/master/part_1_code_2.py

Simple, right? Let's now get our coordinates, if we are being tracked:

https://github.com/atumas-bananamilk/Kinervo/blob/master/part_1_code_3.py

Done! Now we only need to send our X coordinate to Arduino and make servo point to that coordinate

# PART 2

Let's do the following task:

        1. Kinect reads its sensor data
        2. If we are standing in front of the Kinect:
            Kinect sends 5 digits of our X coordinate to Arduino
        Else:
            Nothing
        3. Arduino converts X coordinate to degrees 4. Arduino points servo to the given direction

Let's get 5 digits from our X coordinate and send them to Arduino:

https://github.com/atumas-bananamilk/Kinervo/blob/master/part_2_code_1.py

Okay, let's move on to the Arduino IDE.
A few things to note:

        Kinect's X coordinate range is around -0.8 to 0.8.
        Servo's spin range is around 0 to 160 degrees.

So, to convert X's range to spin's range we use the formula:

        (X coordinate) *100+80 = (spin coordinate)

Then -0.8 becomes 0 degrees, 0.8 becomes 160 degrees.

Connection:

        Connect servo to the Arduino on pin 13.

Code (should not be hard to understand):

https://github.com/atumas-bananamilk/Kinervo/blob/master/part_2_code_2.ino

Done! <br />
If you've managed to make this work, I can assure you that you've just completed one of the hardest tutorials we have here! <br />
Congratulations!
