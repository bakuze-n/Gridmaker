from pylibdmtx.pylibdmtx import decode, encode
from PIL import Image as PIL_Image, ImageChops as PIL_ImageChops

class ImageData:
    def __init__(self, cell_width, cell_height, rows, columns, border_thickness):
        self.cell_width, self.cell_height = cell_width, cell_height
        self.rows, self.columns = rows, columns
        self.border = border_thickness

        if True:
            self.barcode_encoded = self.encode_string()
            self.barcode_img = self.create_barcode()
            self.grid_img = self.draw_grid()
            self.barcode_grid_img = self.barcode_on_grid()

    def encode_string(self):
        # take input string, convert to bytes, and then encode for Data Matrix using pylibdmtx.encode()
        barcode_string = f'{self.cell_width} {self.cell_height} {self.rows} {self.columns} {self.border}'
        barcode_bytes = bytes(barcode_string, 'utf-8')
        barcode_encoded = encode(barcode_bytes, scheme='X12')

        return barcode_encoded

    def create_barcode(self, resize_factor=2):
        # create a PIL image from the properties of the encoded string. Crop for symmetrical whitespace, resize to be less intrusive.
        barcode_img = PIL_Image.frombytes('RGB', (self.barcode_encoded.width, self.barcode_encoded.height), self.barcode_encoded.pixels)
        # 🐍 any way to make the crop dynamic so it always removes the same amount of whitespace?
        barcode_img_cropped = barcode_img.crop((8,0,self.barcode_encoded.width-5, self.barcode_encoded.height-5))
        barcode_img_cropped_resized = barcode_img_cropped.resize((int(self.barcode_encoded.width/resize_factor), int(self.barcode_encoded.height/resize_factor)), resample=0)
        return barcode_img_cropped_resized
    
    def draw_grid(self, border_color=(80,80,80,255), cell_color=(0,0,0,0)):
        # use input self.border if it's wider than (square) barcode width. if not, use (barcode_image.width + 2)
        grid_border = max(self.border, (self.barcode_img.width + 2))
        # total width & height of the output image
        grid_width = (self.columns * self.cell_width) + (grid_border * (self.columns + 1))
        grid_height = (self.rows * self.cell_height) + (grid_border * (self.rows + 1))

        # dimensions & color of the rectangle to draw grid cells on top of, and of the grid cell rectangles
        grid_image = PIL_Image.new('RGBA', (grid_width, grid_height), border_color)
        grid_cell = PIL_Image.new('RGBA', (self.cell_width, self.cell_height), cell_color)

        # draw transparent rectangles onto image, from left to right, top to bottom
        rows_drawn = 0
        while rows_drawn < self.rows:
            columns_drawn = 0
            while columns_drawn < self.columns:
                # get top-left and bottom-right xy to draw grid cells in using PIL.Image.paste()
                topleft_x = grid_border + (columns_drawn * (grid_border + self.cell_width))
                topleft_y = grid_border + (rows_drawn * grid_border) + (rows_drawn * self.cell_height)
                bottomright_x = grid_border + self.cell_width + (columns_drawn * (grid_border + self.cell_width))
                bottomright_y = grid_border + self.cell_height + (rows_drawn * grid_border) + (rows_drawn * self.cell_height)

                grid_image.paste(grid_cell, (topleft_x, topleft_y, bottomright_x, bottomright_y))

                columns_drawn += 1
            rows_drawn += 1

        return grid_image

    def barcode_on_grid(self, margin=0):
        # xy-coords to paste barcode on bottom-right corner of grid image, with (margin = 1) pixel space between barcode and edge
        barcode_xy = (margin, (self.grid_img.height - self.barcode_img.height + margin))
        print(f'Barcode_XY: {barcode_xy}, grid: {self.grid_img.width}/{self.grid_img.height}')
        # put barcode on canvas of same size as grid image. Canvas is white so it is invisible after using .multiply() to combine
        barcode_canvas = PIL_Image.new('RGBA', (self.grid_img.width, self.grid_img.height), color=(255,255,255,255))
        barcode_canvas.paste(self.barcode_img, barcode_xy)
        
        # below crops the image to the barcode dimensions? or at least masks it
        barcode_on_grid_img = PIL_ImageChops.multiply(self.grid_img, barcode_canvas)
        return barcode_on_grid_img

user_image = ImageData(448,448,4,6,25)
user_image.barcode_grid_img.show()






























































         