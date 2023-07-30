
### Air Object Detector

Install with Pypi:

pip3 install pyransac3d
Take a look:
Example 1 - Planar RANSAC
import pyransac3d as pyrsc

points = load_points(.) # Load your point cloud as a numpy array (N, 3)

plane1 = pyrsc.Plane()
best_eq, best_inliers = plane1.fit(points, 0.01)
Results in the plane equation Ax+By+Cz+D: [0.720, -0.253, 0.646, 1.100]

Example 2 - Spherical RANSAC
Loading a noisy sphere's point cloud with r = 5 centered in 0 we can use the following code:

import pyransac3d as pyrsc

points = load_points(.) # Load your point cloud as a numpy array (N, 3)

Documentation & other links
The documentation is this Ṕage.
Source code in the Github repository.
Pypi pakage installer
You can find the animations you see in the documentation on branch Animations. It needs Open3D library to run. The Animation branch is not regularly maintained, it only exists to create some cool visualizations ;D
License
Apache 2.0

Citation
Did this repository was useful for your work? =)
Contributing is awesome!
See CONTRIBUTING

Contact
Developed with heart by the internet

Mainteiner: Leonardo Mariga

Did you like it? Remember to click on 🌟 button.
