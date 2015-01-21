import PIL
import os.path  
import PIL.ImageDraw  
import matplotlib.pyplot as plt

def frame_all_images(color=(0,0,0), wide=10):
    new_directory = os.path.join(os.getcwd(),'modified')
    pictures = os.path.join(os.getcwd(),'1.4.5 Images')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(pictures) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(pictures, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    for entry in file_list:
        absolute_filename = os.path.join(os.path.join(os.getcwd(),'1.4.5 Images'),str(entry))
        image = PIL.Image.open(absolute_filename)
        width, height = image.size
        rounded_mask = PIL.Image.new('RGBA', (width+wide*2, height+wide*2), (0,0,0,0))
        drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
        drawing_layer.polygon([(0,0),(wide,0),
                                (wide,height+wide*2),(0,height+wide*2)],
                                fill=color)
        drawing_layer.polygon([(0,0),(0,wide),
                                (width+wide,wide),(width+wide,0)],
                                fill=color)
        drawing_layer.polygon([(width+wide*2,0),(width+wide*2,height+wide*2),
                                (width+wide,height+wide*2),(width+wide,0)],
                                fill=color)
        drawing_layer.polygon([(0,height+wide*2),(width+wide*2,height+wide*2),
                                (width+wide*2,height+wide),(0,height+wide)],
                                fill=color)
        fig, axes = plt.subplots(1, 2)
        axes[0].set_xlim(0, width)
        axes[0].set_ylim(0, height)
        axes[1].set_xlim(0, width+wide*2)
        axes[1].set_ylim(0, height+wide*2)
        axes[0].imshow(image, interpolation='none')
        result = PIL.Image.new('RGBA', (width+wide*2,height+wide*2), (0,0,0,0))
        result.paste(image, (wide,wide))
        result.paste(rounded_mask, (0,0), mask=rounded_mask)
        axes[1].imshow(result, interpolation='none')
        fig.show()
        new_image_filename = os.path.join(new_directory,str(str(entry))+'.png')
        result.save(new_image_filename)


