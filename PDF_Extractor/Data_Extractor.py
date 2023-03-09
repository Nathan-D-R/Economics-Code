import csv
import io
import os
import PyPDF2

# Change these to match the PDF file and output CSV file
# Get pdf_path from user
pdf_path = input("Enter the path to the PDF file: ")
# Name the csv the same as pdf replacing .pdf with .csv
csv_path = os.path.splitext(pdf_path)[0] + '.csv'

# These are the keys we want to extract from the PDF
keys = [
    'Team',
    'Principal Owner',
    'Year Established',
    'Current Value ($/Mil)',
    'Percent Change From Last Year',
    'Stadium',
    'Facility Cost ($/Mil)',
    'Facility Financing',
    'Percentage of Stadium Publicly Financed',
    'Most Recent Purchase Price ($/Mil)',
    'NAMING RIGHTS',
    'UPDATE'
]

# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Loop over each page in the PDF
    data = []
    for page_num in range(pdf_reader.getNumPages()):

        # Get the current page
        pdf_page = pdf_reader.getPage(page_num)

        # Extract the text from the page
        page_text = pdf_page.extractText()

        # Create a StringIO object to read the text
        page_stream = io.StringIO(page_text)

        # Loop over each line in the page
        row = {}
        for line in page_stream:

            # Check if the line has a colon
            if ':' in line:

                # Split the line into key and value
                key, value = line.split(':', 1)

                # Clean up the key and value
                key = key.strip()
                value = value.strip()

                # Check if the key matches one we want, but if it isn't, try
                # adding an s and try again
                if key in keys:
                    row[key] = value
                elif key + 's' in keys:
                    row[key + 's'] = value

        # Add the row to the data list
        data.append(row)

# Write the data to a CSV file
with open(csv_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)
