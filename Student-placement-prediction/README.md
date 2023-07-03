# Student Placement Prediction

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

<h2>Table of Contents</h2>
<ul>
    <li>Project Overview</li>
    <li>Installation</li>
    <li>Usage</li>
    <li>Features</li>
    <li>Technologies Used</li>


</ul>

<h2 >Project Overview</h2>
<p>
    This project is aimed at developing a web application that predicts the placement status of students based on various parameters. It utilizes the Python programming language and the Flask web framework to provide an
    interactive and user-friendly interface.
</p>

<h2 >Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/your-username/student-placement-prediction.git</code></pre>
    </li>
    <li>Change into the project directory:
        <pre><code>cd student-placement-prediction</code></pre>
    </li>
    <li>Create a virtual environment:
        <pre><code>python3 -m venv env</code></pre>
    </li>
    <li>Activate the virtual environment:
        <pre><code>source env/bin/activate</code></pre>
    </li>
    <li>Install the project dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the Flask application:
        <pre><code>python app.py</code></pre>
    </li>
    <li>Open your web browser and visit <a href="http://localhost:5000">http://localhost:5000</a> to access the
        application.</li>
</ol>

<h2 >Usage</h2>
<p>
    Upon accessing the web application, you will be presented with a user interface where you can enter the necessary
    details for prediction. Fill in the required fields, such as academic scores, skills, and personal information.
    Click on the "Predict" button to submit the form and receive the predicted placement status.
</p>

<h2 >Features</h2>
<ul>
    <li>Predicts the placement status of students based on input parameters</li>
    <li>User-friendly web interface for input and result display</li>
    <li>Handles various input data formats and provides appropriate error messages</li>
    <li>Interactive and responsive design for easy usage on different devices</li>
</ul>

<h2 >Technologies Used</h2>
<ul>
    <li>Python: Programming language used for the backend development and machine learning algorithms.</li>
    <li>Flask: Web framework used for building the web application.</li>
    <li>HTML/CSS: Markup and styling languages for creating the user interface.</li>
    <li>Bootstrap: CSS framework for responsive and visually appealing design.</li>
    <li>Machine Learning Libraries: Python libraries such as scikit-learn, pandas, and numpy used for data
        processing, model training, and prediction.</li>
</ul>


winscp - with help of this we can upload our file on aws

putty - it is a remote client, we take access of machine through ssh. Can open EC2's command prompt in putty

sudo apt-get update && sudo apt-get install python3-pip

pip install -r requirements.txt

screen -R deployment python3 app.py

AWS deployment - Amazon EC2 => ec2-52-15-92-145.us-east-2.compute.amazonaws.com
