import re
from PyPDF2 import PdfReader


def read_data_from_pdf(output_path):
    reader = PdfReader(output_path)
    num_pages = len(reader.pages)
    in_marks_section = False
    marks_data = []
    
    # Extract text from each page
    for page_num in range(2,3):
        page = reader.pages[page_num]
        text = page.extract_text()
        lines = text.splitlines()

        # Iterate through lines to find marks
        count_greater_700 = 0
        for line in lines:
            print(line)
            # Check if we are in the marks section
            if "Marks" in line:
                in_marks_section = True
                continue
            
            if in_marks_section:
                # Extract potential marks from the line
                words = line.split()
                for word in words:
                    if word.isdigit():
                        marks = int(word)
                        if marks >= 700:
                            count_greater_700 += 1
        print(f"count greater than 700 {count_greater_700}")
        # Find all instances of marks data using regex
        matches = re.findall(r'(\d+)\s+(\d+)', text)
        for match in matches:
            srlno, marks = map(int, match)
            # if marks > 700:
            #     print(match)
            marks_data.append((srlno, marks))

    return marks_data