#Importing libraries
from pdf2image import convert_from_path
import os
import os.path
from PIL import Image


#Iterating through each page inj the pdf file
def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    for index, image in enumerate(images):
        image.save(f'output6/{pdf_path}-{index}.jpg')

#Using the library in the module to convert pdf to png
def convert():
    convert_pdf_to_images('tags_1100-1199_12.0cm_n4.pdf')
   
#Function to crop the images    
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


#Main fucntion (converting pdf to png and then cropping png files 
#and replacing it with cropped files)
if __name__ == "__main__":
    convert()
    
    f = r'C:\Users\Aaron\.spyder-py3\output6'
    
    for file in os.listdir(f):
        f_img = f+"/"+file
        img = Image.open(f_img)
        im_new = crop_center(img, 1050, 1050)
        im_new.save(f_img, quality=100)

        
    
