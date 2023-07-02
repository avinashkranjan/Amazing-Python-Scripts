import re
import csv
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def extract_education(resume_text):
    education_pattern = r"((?:Bachelor|Master|Ph\.?D|Diploma)[^.,]*\b(?:\.\b)?(?:[^.,\n]*\b(?:University|College|School|Institute)\b[^.,\n]*)?)"
    education_matches = re.findall(education_pattern, resume_text, re.IGNORECASE)
    return education_matches

def extract_experience(resume_text):
    experience_pattern = r"(?:(?:[A-Z][a-z]+\s+){1,3})?(?:(?:\d{4}\s?-\s?\d{4}|\d{4})\s)?(?:(?:Present|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[A-Za-z\s]+\d{4})"
    experience_matches = re.findall(experience_pattern, resume_text, re.IGNORECASE)
    return experience_matches

def extract_skills(resume_text, skills_list):
    skills_found = []
    for skill in skills_list:
        escaped_skill = re.escape(skill)
        if re.search(r'\b{}\b'.format(escaped_skill), resume_text, re.IGNORECASE):
            skills_found.append(skill)
    return skills_found


file_name = "resumes\Resume_12.pdf"
skills_file = "skills_list.csv"  # Path to the CSV file containing skills
i_f = open(file_name, 'rb')
res_mgr = PDFResourceManager()
ret_data = io.StringIO()
txt_converter = TextConverter(res_mgr, ret_data, laparams=LAParams())
interpreter = PDFPageInterpreter(res_mgr, txt_converter)
for page in PDFPage.get_pages(i_f):
    interpreter.process_page(page)
    resume_text = ret_data.getvalue()

# Extract educational and work experience
education = extract_education(resume_text)
experience = extract_experience(resume_text)

# Extract skills from CSV file
skills_list = []
with open(skills_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        skills_list.extend(row)

# Extract skills
skills = extract_skills(resume_text, skills_list)

# Print the extracted information
print("Educational Background:")
for edu in education:
    print(edu)

print("\nWork Experience:")
for exp in experience:
    print(exp)

print("\nSkills:")
for skill in skills:
    print(skill)

# Close the file and converter
i_f.close()
txt_converter.close()
