Hough Line Transform
--------------------
The Hough Line Transform is a transform used to detect straight lines.
To apply the Transform, first an edge detection pre-processing is desirable.

Implementation
--------------
Detect the road surface in the video - this is a segmentation task, find all pixels in the image which are road; it will help here to have three classes to segment: road, not-road, and sky.
Find the horizon (this is roughly where your road/not-road and sky classes meet
Use a simple edge detector  to differentiate the edges between road and non-road
Apply a Hough Transform on the edges to draw "lines" for the edge of the road
Find where the road-lines meet at the horizon

A road dataset which contained 250 images was downloaded from the California Institute of Technology website. These images were run as a video to test the lane detection algorithm. All the images are read from the folder and checked for edges. Canny edge detection algorithm was used for edge detection. On finding edges, I needed to find out the straight lines by checking the continuity of the pixel values. The feature extraction technique called Hough Transform was made use of for this. This is used to find imperfect instances of objects within a certain class of shapes by a voting procedure. This voting procedure is carried out in a parameter space, from which object candidates are obtained as local maxima in an accumulator space that is explicitly constructed by the algorithm for computing the Hough transform. Third party library functions from OPENCV were used for this.
