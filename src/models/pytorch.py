import torch
import torch.nn as nn
import torch.nn.functional as F
class PytorchBinary(nn.Module):
    def __init__(self, num_features):
        super(PytorchBinary, self).__init__()
        
        self.layer_1 = nn.Linear(num_features, 256)
        self.layer_out = nn.Linear(256, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = F.dropout(F.relu(self.layer_1(x)))
        x = self.sigmoid(self.layer_out(x))
        return (x)
    
def get_device():
    if torch.cuda.is_available():
             device = torch.device('cuda:0')
    else:
            device = torch.device('cpu') 
    return device


