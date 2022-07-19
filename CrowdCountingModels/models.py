import cv2
from PIL import Image
import numpy as np
import torch
from torchvision import transforms

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                ])


def msfanet(path, pretrained):
    # Simple preprocessing.

    # An example image
    # path = "./MSFANet/images/densecrowd1.jpg"
    img = Image.open(path).convert('RGB')
    height, width = img.size[1], img.size[0]
    height = round(height / 16) * 16
    width = round(width / 16) * 16
    img = cv2.resize(np.array(img), (width, height), cv2.INTER_CUBIC)
    img = transform(Image.fromarray(img))[None, :]

    model = pretrained.Model()
    # Weights are stored in the Google drive link.
    # The model are originally trained on a GPU but, we can also test it on a CPU.
    model.load_state_dict(torch.load("./MSFANet/Paper's_weights_UCF_QNRF/best_M-SFANet__UCF_QNRF.pth",
                                     map_location=torch.device('cpu')))

    # Evaluation mode
    model.eval()
    density_map = model(img)

    print(torch.sum(density_map).item())  # Est. count = 147.14852905273438
