import torch

# Load the Depth Anything V2 model
depth_model = torch.hub.load('baegwangbin/Depth-Anything-V2', 'depth_anything_v2', pretrained=True)

print("Model loaded successfully!")
