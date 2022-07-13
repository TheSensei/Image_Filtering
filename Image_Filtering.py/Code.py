from re import A
from PIL import *
from PIL import Image
from PIL import ImageFilter

def black_and_white(original):
    pic_gray = original.convert('L')
    pic_gray.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\black_and_white.jpg')

def blur(original):
    pic_blured = original.filter(ImageFilter.BLUR)
    pic_blured.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\blur.jpg')

def rotate(original):
    pic_up = original.transpose(Image.ROTATE_180)
    pic_up.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\rotate.jpg')

def contour(original):
    pic_contour = original.filter(ImageFilter.CONTOUR)
    pic_contour.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\contour.jpg')

def detail(original):
    pic_detail = original.filter(ImageFilter.DETAIL)
    pic_detail.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\detail.jpg')    

def edge_enhance(original):
    pic_edge_enhance = original.filter(ImageFilter.EDGE_ENHANCE)
    pic_edge_enhance.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\edge_enhance.jpg')

def edge_enhance_more(original):
    pic_edge_enhance_more = original.filter(ImageFilter.EDGE_ENHANCE_MORE)
    pic_edge_enhance_more.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\edge_enhance_more.jpg')

def emboss(original):
    pic_emboss = original.filter(ImageFilter.EMBOSS)
    pic_emboss.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\emboss.jpg')

def find_edges(original):
    pic_find_edges = original.filter(ImageFilter.FIND_EDGES)
    pic_find_edges.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\find_edges.jpg')

def smooth(original):
    pic_smooth = original.filter(ImageFilter.SMOOTH)
    pic_smooth.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\smooth.jpg')

def sharpen(original):
    pic_sharpen = original.filter(ImageFilter.SHARPEN)
    pic_sharpen.save('C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\sharpen.jpg')

with Image.open("C:\\Users\\USER\\Desktop\\Python\\Image_Filtering.py\\Forest_Painting.jpg") as original:
    edit = input('Enter the filter you want:\n')
    if edit == 'black and white':
        black_and_white(original)
    elif edit == 'blur':
        blur(original)
    elif edit == 'rotate':
        rotate(original)
    elif edit == 'contour':
        contour(original)
    elif edit == 'detail':
        detail(original)
    elif edit == 'edge enhance':
        edge_enhance(original)
    elif edit == 'edge enhance more':
        edge_enhance_more(original)
    elif edit == 'emboss':
        emboss(original)
    elif edit == 'find edges':
        find_edges(original)
    elif edit == 'smooth':
        smooth(original)
    elif edit == 'sharpen':
        sharpen(original)
    else:
        print('No such filtering')
    original.show()