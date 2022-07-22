import models
import torch

# test image
path = ""

print("Which model do you wish to use?")
print("For MSFANET enter m, for CAN enter c, for P2P enter p")
model = input()
if model == 'm':
    models.msfanet(path)

