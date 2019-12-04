# pytorch-randaugment
Unofficial PyTorch Reimplementation of AutoAugment and RandAugment.

Code taken from https://github.com/DeepVoltaire/AutoAugment and https://github.com/jizongFox/uda
## How to install:
```bash
pip install randaugment
```
---

## How to use:
```python
from autoaugment import RandAugment, ImageNetPolicy
data = ImageFolder(rootdir, transform=transforms.Compose(
                        [
                            transforms.RandomCrop(32, padding=4, fill=128), # fill parameter needs torchvision installed from source
                            transforms.RandomHorizontalFlip(), 
                            RandAugment(),
                            #ImageNetPolicy(),
                            transforms.ToTensor(), 
                            Cutout(size=16), # (https://github.com/uoguelph-mlrg/Cutout/blob/master/util/cutout.py)
                            transforms.Normalize(...)
                        ])
)
loader = DataLoader(data, ...)
```


