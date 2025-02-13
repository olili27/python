from PIL import Image

img = Image.open("./design1.jpeg").convert("L")

w,h = img.size

chunkWidth = 10

border1 = 0
# def crop():
# for start in range(0, w, chunkWidth):
#     border1 += chunkWidth

#     slice = img.crop((start, 0, start + chunkWidth, h))
#     pixels = slice.getdata()
#     average = sum(pixels) / len(pixels)
#     minVal = min(pixels)
#     maxVal = max(pixels)
#     range = maxVal - minVal

#     if range >= (2 * minVal):
#         break

# croppedImage = img.crop((border1, 0, w, h))
# # croppedImage.show()

img2 = img.transpose(Image.FLIP_LEFT_RIGHT)  # flip image horizontally
# img2.show()
# w,h = img2.size
print(img2.size)

border2 = 0
for start in range(0, w, chunkWidth):
    border2 += chunkWidth

    slice = img2.crop((start, 0, start + chunkWidth, h))
    pixels = slice.getdata()
    average = sum(pixels) / len(pixels)
    minVal = min(pixels)
    maxVal = max(pixels)
    range = maxVal - minVal

    if range >= (2 * minVal):
        break

croppedImage = img2.crop((border2, 0, w, h))
croppedImage.show()





# def getVariance(slice : list):


# def findChunkWidth(image_length) -> int:
#     max_divisible_number = 10
#     start = 5
#     chunk_size = image_length
#     for i in range(start, max_divisible_number):
#         if((image_length % i) == 0):
#             chunk_size = image_length / i
#         else:
#             start = max_divisible_number
#             max_divisible_number = max_divisible_number * 2
#     # if(chunk_size > 20):

#     print('chunk_size:', chunk_size)
        
# findChunkWidth(w)

# img.show()

# print("height:", h, "width:", w)