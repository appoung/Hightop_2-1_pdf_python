import requests
import img2pdf

from io import BytesIO


def download_images_and_create_pdf(base_url, start_page, end_page, pdf_filename):
    image_list = []

    for page_number in range(start_page, end_page + 1):
        image_url = f"{base_url}{page_number:03d}.jpg"

        # Download image
        response = requests.get(image_url)
        image_data = BytesIO(response.content)
        image_list.append(image_data)

    # Convert images to PDF
    pdf_bytes = img2pdf.convert(image_list)

    # Save PDF to file
    with open(pdf_filename, 'wb') as pdf_file:
        pdf_file.write(pdf_bytes)


# Example usage
base_url = "http://ebook.dongapublishing.com/ebook/catImage8/13/s"
start_page = 1
end_page = 240
pdf_filename = "output.pdf"

download_images_and_create_pdf(base_url, start_page, end_page, pdf_filename)
