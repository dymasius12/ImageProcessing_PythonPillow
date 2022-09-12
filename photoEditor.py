from PIL import Image, ImageEnhance, ImageFilter
import os

#this is folder for unedited images
path = '/Users/dymas/development/Python/Image_Editor/PythonPillow_ImageEditor/Image_Editor/imgs' 


#this is for edited images
pathOut = '/Users/dymas/development/Python/Image_Editor/PythonPillow_ImageEditor/Image_Editor/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #sharpengin BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    #contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    #add more edits                                                                                                                                                                                                                                                                                                                                                                                                                                     
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

