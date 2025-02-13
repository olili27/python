from PIL import Image

img = Image.open("./design1.jpeg").convert("L")

w,h = img.size

chunkWidth = 10

border1 = 0

def recursive(border, chunkWidth, w, img, run, maxRuns):
    if run < maxRuns:
        for start in range(0, w, chunkWidth):
            border += chunkWidth

            slice = img.crop((start, 0, start + chunkWidth, h))
            pixels = slice.getdata()
            average = sum(pixels) / len(pixels)
            minVal = min(pixels)
            maxVal = max(pixels)
            data_range = maxVal - minVal
            print('range:', data_range, 'min', minVal, 'max', maxVal)


            if data_range >= ( minVal):
                print('final range:', data_range, 'min', minVal, 'max', maxVal)
                break

        croppedImage = img.crop((border, 0, w, h))
        croppedImage.show()
        img2 = croppedImage.transpose(Image.FLIP_LEFT_RIGHT)  # flip image horizontally
        recursive(border,chunkWidth,w,img2,run + 1,maxRuns)

recursive(border1,chunkWidth,w,img,1,3)




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