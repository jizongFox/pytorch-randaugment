import requests
from PIL import Image

from randaugment.randaugment import RandAugment,Cutout

url = "https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
img = Image.open(requests.get(url, stream=True).raw)
img=img.resize((256,256))
random_transform = RandAugment()
cutout = Cutout(size=30)
for i in range(5):
    img_ = random_transform(img)
    img_ = cutout(img_)
    img_.show()
