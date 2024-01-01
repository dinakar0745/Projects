import openpyxl
from barcode import Code128
from barcode.writer import ImageWriter
import os

def generate_barcode(roll_number, output_path):
    # Generate barcode
    code = Code128(roll_number, writer=ImageWriter(), add_checksum=False)
    barcode_path = os.path.join(output_path, f'{roll_number}.png')
    code.save(barcode_path)

def generate_barcodes_from_excel(excel_file, output_path):
    # Check if the output directory exists, create it if not
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Load Excel workbook
    try:
        wb = openpyxl.load_workbook(excel_file)
    except FileNotFoundError:
        print(f"Error: Excel file '{excel_file}' not found.")
        return

    # Assuming the roll numbers are in the first sheet (you can modify this based on your sheet structure)
    sheet = wb.active

    # Iterate through rows and generate barcodes
    for row in sheet.iter_rows(min_row=2, values_only=True):
        roll_number = str(row[0])  # Assuming roll number is in the first column
        generate_barcode(roll_number, output_path)

if __name__ == "__main__":
    excel_file_path = "C:\\Users\\Dinak\\Desktop\\Projects\\barcode\\test.xlsx"
    output_directory = "C:\\Users\\Dinak\\Desktop\\Projects\\barcode\\test"

    generate_barcodes_from_excel(excel_file_path, output_directory)
