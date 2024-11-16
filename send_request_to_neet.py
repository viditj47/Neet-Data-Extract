import requests
import re
from PyPDF2 import PdfReader
from read_neet_data_from_pdf import read_data_from_pdf

def download_pdf(url, output_path,center_number,file_name):
    headers = {
        "Accept": "application/pdf"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF downloaded successfully: {output_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")
        return 1
    
    marks_data = read_data_from_pdf(output_path)

    total_marks = 0 
    marks_list = []  
    print(type(marks_data[0])) 
    marks_above_700 = 0
    marks_above_650 = 0
    marks_above_600 = 0
    marks_above_500 = 0
    for srlno, marks in marks_data:
        total_marks+= marks
        marks_list.append(marks)
        type(marks)
        if marks > 700:
            marks_above_700 += 1
            print(f"Srlno: {srlno}, Marks: {marks}")
         
        if marks > 650:
            marks_above_650 += 1

        if marks > 600:
            marks_above_600 += 1

        if marks > 500:
            marks_above_500 += 1
        

    print("****************************************************************************************")
    print(f"Average Marks at Center Number {center_number} is : {total_marks/len(marks_data)}")
    print(f"Maximum Marks at center {center_number} is: {max(marks_list)}")
    print(f"Minimum Marks at center {center_number} is: {min(marks_list)}")
    print(f"Marks Above 700 at center {center_number} is: {marks_above_700}")
    print(f"Marks Above 650 at center {center_number} is: {marks_above_650}")
    print(f"Marks Above 600 at center {center_number} is: {marks_above_600}")
    print(f"Marks Above 500 at center {center_number} is: {marks_above_500}")

    
    # Open the file in write mode and write the content
    with open(file_name, "a") as file:
        file.write("****************************************************************************************\n")
        file.write(f"Average Marks at Center Number {center_number} is : {total_marks/len(marks_data)}\n")
        file.write(f"Maximum Marks at center {center_number} is: {max(marks_list)}\n")
        file.write(f"Minimum Marks at center {center_number} is: {min(marks_list)}\n")
        file.write(f"Marks Above 700 at center {center_number} is: {marks_above_700}\n")
        file.write(f"Marks Above 650 at center {center_number} is: {marks_above_650}\n")
        file.write(f"Marks Above 600 at center {center_number} is: {marks_above_600}\n")
        file.write(f"Marks Above 500 at center {center_number} is: {marks_above_500}\n")




staring_center_number = 392304
total_center = 1
output_file = "output.pdf"
file_name = "sikar_Neet_Data.txt"
for center_number in range(staring_center_number, staring_center_number+total_center):
    pdf_url = "https://neetfs.ntaonline.in/NEET_2024_Result/" + str(center_number) +".pdf"
    download_pdf(pdf_url, output_file,center_number, file_name)