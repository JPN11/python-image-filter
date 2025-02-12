from PIL import Image, ImageFilter

def apply_filter(image_path, filter_name):
    image = Image.open(image_path)
    if filter_name == 'grey':
        image = image.convert('L')
    elif filter_name == 'sepia':
        image = image.convert('RGB')
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = int(r * 0.393 + g * 0.769 + b * 0.189)
                g = int(r * 0.349 + g * 0.686 + b * 0.168)
                b = int(r * 0.272 + g * 0.534 + b * 0.131)
                pixels[x, y] = (r, g, b)
    elif filter_name == 'invert':
        image = image.convert('RGB')
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = 255 - r
                g = 255 - g
                b = 255 - b
                pixels[x, y] = (r, g, b)
    elif filter_name == 'blur':
        image = image.filter(ImageFilter.GaussianBlur(radius=5))
    elif filter_name == 'reflect':
        width, height = image.size
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[width - x - 1, y] = (r, g, b)
    elif filter_name == 'sharpen':
        image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    elif filter_name == 'contour':
        image = image.filter(ImageFilter.CONTOUR)
    elif filter_name == 'detail':
        image = image.filter(ImageFilter.DETAIL)
    elif filter_name == 'edge':
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_name == 'emboss':
        image = image.filter(ImageFilter.EMBOSS)
    return image  # Return the image object instead of the output filename

def greyfilter(image_path):
    return apply_filter(image_path, 'grey')

def sepiafilter(image_path):
    return apply_filter(image_path, 'sepia')

def invertfilter(image_path):
    return apply_filter(image_path, 'invert')

def blurfilter(image_path):
    return apply_filter(image_path, 'blur')

def reflectfilter(image_path):
    return apply_filter(image_path, 'reflect')

def sharpenfilter(image_path):
    return apply_filter(image_path, 'sharpen')

def contourfilter(image_path):
    return apply_filter(image_path, 'contour')

def detailfilter(image_path):
    return apply_filter(image_path, 'detail')

def edgefilter(image_path):
    return apply_filter(image_path, 'edge')

def embossfilter(image_path):
    return apply_filter(image_path, 'emboss')
