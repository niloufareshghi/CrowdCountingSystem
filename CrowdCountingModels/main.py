import models
from MSFANet.models import M_SFANet_UCF_QNRF
import torch

# test image
path = "./MSFANet/images/densecrowd1.jpg"

print("Which model do you wish to use?")
print("For MSFANET enter m, for CAN enter c, for P2P enter p")
model = input()
if model == 'm':
    models.msfanet(path, M_SFANet_UCF_QNRF)
elif model == 'c':
    models.can(path)
elif model == 'p':
    models.p2pnet()
