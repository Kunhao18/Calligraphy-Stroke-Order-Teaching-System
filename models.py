import torch
import torch.nn as nn
import torch.nn.functional as F


class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()
        self.hidden_dim = 512
        self.output_dim = 128

        self.conv1 = nn.Conv2d(1, 6, kernel_size=(3, 3))
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, kernel_size=(5, 5))
        self.fc1 = nn.Linear(2704, self.hidden_dim)
        self.fc2 = nn.Linear(self.hidden_dim, self.output_dim)

    def forward(self, inputs):
        out = self.pool(F.leaky_relu(self.conv1(inputs)))
        out = self.pool(F.leaky_relu(self.conv2(out)))
        out = out.view(-1, 2704)
        out = F.leaky_relu(self.fc1(out))
        out = self.fc2(out)
        return out


class Classifier(nn.Module):
    def __init__(self, device):
        super(Classifier, self).__init__()
        self.save_path = 'model_dict/classifier.ckpt'

        self.encoder1 = Encoder()
        self.fc3 = nn.Linear(128, 2)

        self.device = device

    def get_encode(self, inputs):
        inputs = inputs.to(self.device)
        out = self.encoder1(inputs)
        return out

    def get_result(self, inputs, labels):
        inputs, labels = inputs.to(self.device), labels.to(self.device)
        out = torch.abs(inputs - labels)
        out = self.fc3(out)
        return out

    def forward(self, inputs, labels):
        inputs, labels = inputs.to(self.device), labels.to(self.device)
        out1 = self.encoder1(inputs)
        out2 = self.encoder1(labels)
        out = torch.abs(out1 - out2)
        out = self.fc3(out)
        return out
