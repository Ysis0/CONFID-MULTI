import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--seed', type=int, default=0)
parser.add_argument("--dropout", type=float, default=0.0)
parser.add_argument('--show_training_details', type=bool, default=False)
parser.add_argument('--num_heads', type=int, default=4, help='Number of attention heads')
parser.add_argument('--t', type=int, default=2, help="Number of gnn layers")
parser.add_argument('--linlayers', type=int, default=1, help="Number of hidden layers")
parser.add_argument('--epochs', type=int, default=400, help='Number of epochs to train.')
parser.add_argument('--dims', type=int, default=500, help='feature dim')
parser.add_argument('--lr', type=float, default=1e-4, help='Initial learning rate.')
parser.add_argument('--dataset', type=str, default='cora', help='name of dataset.')
parser.add_argument('--cluster_num', type=int, default=7, help='number of cluster.')
parser.add_argument('--device', type=str, default='cuda', help='the training device')
parser.add_argument('--threshold', type=float, default=0.5, help='the threshold of high-confidence')
parser.add_argument('--tau_feat', type=float, default=1.0)
parser.add_argument('--tau_node', type=float, default=10.0)

# Hyperparameters for loss function
parser.add_argument('--alpha', type=float, default=0.5, help='trade-off of loss') #neg
parser.add_argument('--beta', type=float, default=0.1, help='trade-off of loss') #match
parser.add_argument('--sigma', type=float, default=1,help='trade-off of loss') #feat1
parser.add_argument('--gamma', type=float, default=1,help='trade-off of loss') #feat2

# clustering performance: acc, nmi, ari, f1
parser.add_argument('--acc', type=float, default=0)
parser.add_argument('--nmi', type=float, default=0)
parser.add_argument('--ari', type=float, default=0)
parser.add_argument('--f1', type=float, default=0)

args = parser.parse_args()
