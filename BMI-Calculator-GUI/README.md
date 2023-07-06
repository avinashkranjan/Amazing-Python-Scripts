# BMI GUI Calculator

A graphical user interface (GUI) application that calculates your Body Mass Index (BMI) for assessing your health and fitness.

## Demo Image

![Screenshot (1849)](https://github.com/mkswagger/Amazing-Python-Scripts/assets/34826479/c1407272-733e-4997-98de-b42d4406f59b)



## Functionality
- Enter Weight: Use the slider to select your weight in kilograms.
- Enter Height: Input your height in meters square in the provided text field.
- Calculate BMI: Click the "Click to Check Your BMI" button to calculate your BMI.
- Display Result: The calculated BMI value will be displayed below the button.
- BMI Table: Refer to the BMI table on the right side for interpretation of the calculated BMI.
## Libraries Used
The following libraries were used in the implementation of this BMI calculator:

- Tkinter: Tkinter is the standard GUI toolkit for Python. It provides a set of Python bindings to the Tk GUI toolkit, allowing us to create graphical user interfaces.
- math: The math library provides mathematical functions and constants. It is used in this calculator to perform the BMI calculation and round the result to two decimal places.

## How it Works
1. **Input Weight and Height**: Enter your weight in kilograms (kg) using the provided slider. Then, input your height in meters (mts) in the text field.

2. **BMI Calculation**: The application calculates the BMI using the formula: BMI = weight / (height * height). The BMI value is calculated based on the weight and height inputs provided.

3. **BMI Result**: The calculated BMI value is displayed on the screen. The result is rounded to two decimal places.

4. **BMI Chart**: You can refer to the BMI chart to interpret your calculated BMI value and assess your health and fitness level.

## BMI Chart
The BMI chart provides a general guideline for interpreting BMI values:

- Underweight: BMI less than 18.5
- Normal weight: BMI between 18.5 and 24.9
- Overweight: BMI between 25 and 29.9
- Obesity Level I: BMI between 30 and 34.9
- Obesity Level II: BMI between 35 and 39.9
- Obesity Level III: BMI greater than or equal to 40

Note: The BMI calculation is a basic indicator and does not take into account factors such as muscle mass and distribution of fat. Consult a healthcare professional for a comprehensive evaluation of your health.

## How to Use

1. Clone the repository: `git clone https://github.com/your-username/bmi-calculator.git`
2. Navigate to the project directory: `cd bmi-calculator`
3. Install the required dependencies (Tkinter is usually included with Python).
4. Run the application: `python bmi_calculator.py`
5. Use the slider to select your weight in kilograms.
6. Enter your height in meters in the provided text field.
7. Click the "Click to Check Your BMI" button to calculate your BMI.
8. The calculated BMI value will be displayed below the button.
9. Refer to the BMI chart to interpret your BMI value and assess your health and fitness level.



## Requirements
- Python (version 3.x)
- Tkinter (usually included with Python)


