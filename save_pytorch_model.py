import torch

# 예시 PyTorch 모델
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()

# 모델을 저장
torch.save(model.state_dict(), 'model.pth')

print("PyTorch 모델이 저장되었습니다.")
