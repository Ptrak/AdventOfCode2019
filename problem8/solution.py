
def get_count(search_int: int, layer):
    count = 0
    for i, row in enumerate(layer):
        for j, column in enumerate(row):
            if column == search_int:
                count += 1
    return count

f = open('image.txt', 'r')
image_raw = f.readline().rstrip()
f.close()

image_width  = 25
image_height = 6

# calculate layers
pixels           = len(image_raw)
pixels_per_layer = image_width * image_height
total_layers     = int(pixels/pixels_per_layer)

# layer, row, column
print("Width: {} Height: {}: Layers: {}".format(image_width, image_height, total_layers))
image_arr = [[[0 for _ in range(image_width)] for _ in range(image_height)] for _ in range(total_layers)]
print("Layers: {} Rows: {} Columns: {}".format(len(image_arr), len(image_arr[0]), len(image_arr[0][0])))
current_layer = 0
current_row = 0
current_column = 0
for i, pixel in enumerate(image_raw):

    #print("Adding {} to [{}][{}][{}]".format(pixel, current_layer, current_row, current_column))
    image_arr[current_layer][current_row][current_column] = int(pixel)
    current_column += 1

    # reset to beginning of row and increment row
    if (current_column > 0 and current_column % image_width == 0) :
        current_column = 0
        current_row += 1

    # reset to beginning of image and increment layer
    if current_row > 0 and current_row % image_height == 0 :
        current_row = 0
        current_layer += 1

print("total Layers", pixels/pixels_per_layer)

# find the layer with the fewest 0 digits
zero_count = -1
zero_layer = 0
layer_id = 0
for i, layer in enumerate(image_arr):
    zeros = get_count(0, layer)
    print("{} 0s found in Layer {}".format(zeros, i))
    if zero_count == -1 or zeros < zero_count:
        zero_layer = layer
        zero_count = zeros
        layer_id = i

print("Layer with most 0s {} with {} total 0s".format(layer_id, zero_count))
ones = get_count(1, zero_layer)
twos = get_count(2, zero_layer)
print("Total 1s: {} Total 2s: {} Multiplied: {}".format(ones, twos, ones*twos))

# layer 0 is frontmost layer 99 is back-most
final_image = [[0 for _ in range(image_width)]for _ in range(image_height)]
for i, row in enumerate(final_image):
    for j, column in enumerate(row):
        final_image[i][j] = 2
for i, layer in enumerate(image_arr):
    for j, row in enumerate(layer):
        for k, column in enumerate(row):
            current_pixel = final_image[j][k]
            if current_pixel == 2:
                print("Replacing {} with {} ".format(current_pixel, image_arr[i][j][k]))
                final_image[j][k] = image_arr[i][j][k]

print(final_image)





