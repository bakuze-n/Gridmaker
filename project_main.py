from PIL import Image as PIL_Image, ImageChops as PIL_ImageChops, ImageOps as PIL_ImageOps
from pylibdmtx.pylibdmtx import decode, encode

def get_image():
    # can I replace this with a proper Tkinter GUI?
    img_input = input('Paste the path to your image here: ').strip().lower()
    if img_input:
        image = PIL_Image.open(img_input)
        return image
    else:
        print('Image could not be found.')
    
def get_barcode(input_image, barcode):
    # crop the part of the input_image with the barcode, for faster decoding
    left, upper, right, lower = (input_image.width-barcode.width), (input_image.height-barcode.height), (input_image.width), (input_image.height)
    cropped_image = input_image.crop((left, upper, right, lower))
    grayscale_image = PIL_ImageOps.grayscale(cropped_image)

    barcodes = decode(grayscale_image)
    if len(barcodes) == 1:
        # barcode gives a list of barcodes, each item contains data (in bytes) and info about the rectangular bounding box (x, y, width, height). I only need the data.
        barcode_bytes = barcodes[0][0]
        # convert bytes into string (bytes to utf-8)
        barcode_string = barcode_bytes.decode('utf-8')
        # separate resulting string into relevant elements
        b_cell_width, b_cell_height, b_rows, b_columns, b_border_thickness = barcode_string.split('.')
        return b_cell_width, b_cell_height, b_rows, b_columns, b_border_thickness
    
    else:
        # exception in case 0 or 2+ barcodes are found
        fill_word = '' if len(barcodes) == 0 else 'only '
        raise Exception(f'Found {len(barcodes)} barcodes, but expected {fill_word}1 barcode.')
    
def make_barcode(cell_width, cell_height, rows, columns, border_thickness, resize_factor=2):
    barcode_string = f'{cell_width}.{cell_height}.{rows}.{columns}.{border_thickness}'
    barcode_bytes = bytes(barcode_string, 'utf-8')
    barcode_encoded = encode(barcode_bytes)

    # turn encoded bytes into a barcode image (small, but large enough to still be read)
    barcode_image = PIL_Image.frombytes('RGB', (barcode_encoded.width, barcode_encoded.height), barcode_encoded.pixels)
    barcode_resized = barcode_image.resize(size=(int(barcode_image.width / resize_factor), int(barcode_image.height / resize_factor)), resample=0)

    return barcode_resized, barcode_string.split('.')

def make_grid(grid_image_details, barcode_image, border_color=(80,80,80,255), cell_color=(0,0,0,0)):
    # convert input variable (string) into local variables (int)
    g_cell_width, g_cell_height, g_rows, g_columns, g_border = map(int, grid_image_details)
    # make sure that the border is wide enough to fit the barcode, no matter its size
    grid_border = max(g_border, (barcode_image.width - 2), (barcode_image.height - 2))
    # total width & height of the output image
    grid_width = (g_columns * g_cell_width) + (grid_border * (g_columns + 1))
    grid_height = (g_rows * g_cell_height) + (grid_border * (g_rows + 1))

    # dimensions & color of the rectangle to draw grid cells on top of, and of the grid cell rectangles
    grid_image = PIL_Image.new('RGBA', (grid_width, grid_height), border_color)
    grid_cell = PIL_Image.new('RGBA', (g_cell_width, g_cell_height), cell_color)

    # draw transparent rectangles onto image, from left to right, top to bottom
    rows_drawn = 0
    while rows_drawn < g_rows:
        columns_drawn = 0
        while columns_drawn < g_columns:
            # get top-left and bottom-right xy to draw grid cells in using PIL.Image.paste()
            topleft_x = grid_border + (columns_drawn * grid_border) + (columns_drawn * g_cell_width)
            topleft_y = grid_border + (rows_drawn * grid_border) + (rows_drawn * g_cell_height)
            bottomright_x = grid_border + (columns_drawn * grid_border) + g_cell_width + (columns_drawn * g_cell_width)
            bottomright_y = grid_border + (rows_drawn * grid_border) + g_cell_height + (rows_drawn * g_cell_height)

            grid_image.paste(grid_cell, (topleft_x, topleft_y, bottomright_x, bottomright_y))

            columns_drawn += 1
        rows_drawn += 1

    return grid_image

def barcode_on_grid(grid_image, barcode_image):
    # puts the barcode on the bottom-right corner of the grid image

    #first calculate coordinates of barcode position based on grid_image width/height
    barcode_xy = ((grid_image.width - barcode_image.width + 1), (grid_image.height - barcode_image.height + 1))

    barcode_canvas = PIL_Image.new('RGBA', (grid_image.width, grid_image.height), color=(255,255,255,255))
    barcode_canvas.paste(barcode_image, barcode_xy)
    
    # below crops the image to the barcode dimensions? or at least masks it
    result = PIL_ImageChops.multiply(grid_image, barcode_canvas)
    return result

def main():
    '''
    Based on what the user wants to do, they can either create a grid or crop an existing grid.
    Change numbers in test_numbers to create a custom grid, and manually save the image shown in user_barcoded_grid.show() to save it to your folders.
    To create a grid, some numbers are needed: width/height of each rectangle (cell), amount of rows and columns, and the thickness of the grid (border)

    Work-in-progress, so some example numbers are still hard-coded into main() for easier testing.
    
    No functional image upload/saving yet (will be added with the GUI)
    '''
    # test numbers to build a grid from
    test_numbers = [448, 448, 2, 4, 40]
    cell_width, cell_height, rows, columns, border_thickness = test_numbers

    # make a data matrix barcode based on input numbers (necessary if the user wants to crop cells out of the grid later)
    user_barcode, user_barcode_string = make_barcode(cell_width, cell_height, rows, columns, border_thickness)

    # make a grid based on input numbers
    user_grid = make_grid(user_barcode_string, user_barcode, border_color=(70,70,70,255))

    # add the barcode to the grid. If the user wants to crop images out of the grid, this barcode is used to determine which areas to crop.
    user_barcoded_grid = barcode_on_grid(user_grid, user_barcode)

    # for testing purposes: show image of grid with barcode on it
    user_barcoded_grid.show()

    #
    print(get_barcode(user_barcoded_grid, user_barcode))

if __name__ == '__main__':
    main()
