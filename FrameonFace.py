# attach a sunglass to another photo!



from PIL import Image

def paste_sunglasses(photo_path, sunglasses_path, output_path):

    face_width = 2000

    photo = Image.open(photo_path)
    sunglasses = Image.open(sunglasses_path)

    sunglasses_width = face_width // 1
    sunglasses = sunglasses.resize((sunglasses_width, sunglasses_width * sunglasses.height // sunglasses.width))

    paste_x = 1300
    paste_y = 1080

    photo.paste(sunglasses, (paste_x, paste_y), sunglasses)

    photo.save(output_path)

if __name__ == "__main__":
      photo_path = "face.jpg"
      sunglasses_path = "sunglasses.png"
      output_path = "my_photo_with_sunglasses.jpg"
      paste_sunglasses(photo_path, sunglasses_path, output_path)
