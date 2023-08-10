# BMI Calculator Project

This is a simple BMI (Body Mass Index) Calculator web application built using Python and Flask. It allows users to calculate their BMI based on their weight and height, and it provides an interpretation of the BMI category.

## Project Structure

The project consists of the following files:

- `app.py`: This is the main Python script that contains the Flask application. It handles the server-side calculations and serves the web pages.
- `templates/`: This folder contains the HTML templates used for rendering the user interface. It includes two templates:
  - `index.html`: The main page of the BMI calculator where users can enter their weight and height.
  - `result.html`: The result page that displays the calculated BMI, its interpretation, and additional information about BMI categories.
- `styles.css`: The CSS file responsible for styling the user interface of the BMI calculator.

## BMI Categories

The BMI calculator provides interpretation for BMI categories as follows:

- Underweight: less than 18.5
- Normal weight: 18.5 - 24.9
- Overweight: 25 - 29.9
- Obese: 30 or greater