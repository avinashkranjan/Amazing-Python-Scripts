# Resume Parser

The Resume Parser is a Python script that extracts relevant information such as educational background, work experience, and skills from a resume in PDF format.

## How It Works

The Resume Parser follows these steps to extract information from a resume:

1. The PDF file is opened and processed using the `pdfminer` library, which extracts the text content from each page of the PDF.

2. The extracted text is stored as a string.

3. Regular expressions are used to search for patterns and extract the educational background and work experience sections from the resume text. These regular expressions can be customized in the `extract_education` and `extract_experience` functions of the `newparser.py` file.

4. If a `skills_list.csv` file is provided, the script reads the file and creates a list of skills to search for in the resume. Each skill should be placed on a separate line in the CSV file.

5. The script searches for each skill in the resume text using case-insensitive matching. If a skill is found, it is added to the list of extracted skills.

6. The extracted educational background, work experience, and skills are displayed in the console output.

<img width="205" alt="image" src="https://github.com/mkswagger/Amazing-Python-Scripts/assets/34826479/3600c2f8-2fea-436d-8679-327e2ecdea81">


## Usage

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/mkswagger/Amazing-Python-Scripts/tree/master/Resume_parser
   
2. Place the resume PDF file you want to parse in the project directory.

3. Modify the `file_name` variable in the `newparser.py` file to match the name of your resume file.

4. Optionally, if you have a wide range of skills to extract, create a CSV file named `skills_list.csv` in the project directory. Each skill should be placed on a separate line.

5. Run the script:

   ```shell
   python newparser.py

The script will extract the educational background, work experience, and skills from the resume and display them in the console.
Feel free to customize the regular expressions and add additional extraction logic based on your specific requirements.

