from torch.nn import Module, Parameter
import pandas as pd
import numpy as np
import torch

n_gene = 6
n_cancer = 10
dim_embed_gene = 20
dim_embed_cancer = 20


class SimGC(Module):
    def __init__(self, n_gene, n_cancer, dim_embed_gene, dim_embed_cancer):
        self.embed_gene = Parameter(torch.Tensor(n_gene, dim_embed_gene))
        self.embed_cancer = Parameter(torch.Tensor(dim_embed_cancer))

        # self.reset_parameters()

    def reset_parameters(self):
        self.embed_gene.data.normal_()
        self.embed_cancer.data.normal_()

    def forward(self):
        return torch.sigmoid(torch.mul(self.embed_gene, self.embed_cancer))


# device setting
device_name = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device_name)
device = torch.device(device_name)

# load data
data = pd.read_csv("data/D2_combined_gene_dep_scores.csv",
                   usecols=range(1, 713)).to_numpy()
data = torch.from_numpy(np.where(data<-0.5, 1, 0))
data.to(device)

# model setting
model = SimGC(data.shape[0], data.shape[1], dim_embed_gene, dim_embed_cancer)
model.to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)


for epoch in range(10):
    model.train()
    optimizer.zero_grad()

    z = model()
    loss =
