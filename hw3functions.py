
from PySide6.QtGui import QPixmap, QColor

def greyscale(pixmap):
    qimage = pixmap.toImage()
    for x in range(qimage.width()):
        for y in range(qimage.height()):
            pixel_color = qimage.pixelColor(x, y)
            average = (pixel_color.red() + pixel_color.green() + pixel_color.blue()) // 3
            qimage.setPixelColor(x, y, QColor(average, average, average))
    
    return QPixmap.fromImage(qimage)

def neg(pixmap):
    qimage = pixmap.toImage()
    for x in range(qimage.width()):
        for y in range(qimage.height()):
            pixel_color = qimage.pixelColor(x, y)
            r, g, b = 255 - pixel_color.red(), 255 - pixel_color.green(), 255 - pixel_color.blue()
            qimage.setPixelColor(x, y, QColor(r, g, b))
    
    return QPixmap.fromImage(qimage)

def sepia(pixmap):
    qimage = pixmap.toImage()
    for x in range(qimage.width()):
        for y in range(qimage.height()):
            pixel_color = qimage.pixelColor(x, y)
            r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
            new_r = min(255, int(0.393 * r + 0.769 * g + 0.189 * b))
            new_g = min(255, int(0.349 * r + 0.686 * g + 0.168 * b))
            new_b = min(255, int(0.272 * r + 0.534 * g + 0.131 * b))
            qimage.setPixelColor(x, y, QColor(new_r, new_g, new_b))
    
    return QPixmap.fromImage(qimage)

def thumbnail(pixmap):
    image = pixmap.toImage()
    new_width = image.width() // 2
    new_height = image.height() // 2
    qimage = QPixmap(new_width, new_height).toImage()
    
    for x in range(new_width):
        for y in range(new_height):
            pixel_color = image.pixelColor(x * 2, y * 2)
            qimage.setPixelColor(x, y, pixel_color)
    
    return QPixmap.fromImage(qimage)
