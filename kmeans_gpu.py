﻿import numpy as np
import torch
from tqdm import tqdm


def setup_seed(seed):
    """
    setup random seed to fix the result
    Args:
        seed: random seed
    Returns: None
    """
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True


def initialize(X, num_clusters):  #X={Tensor：7650}
    """
    initialize cluster centers
    :param X: (torch.tensor) matrix
    :param num_clusters: (int) number of clusters
    :return: (np.array) initial state
    """
    num_samples = len(X) #num_samples = 7650
    indices = np.random.choice(num_samples, num_clusters, replace=False)  
    initial_state = X[indices]
    return initial_state


def kmeans(
        X,
        num_clusters,
        distance='euclidean',
        tol=1e-4,
        device=torch.device('cuda')
):
    """
    perform kmeans
    :param X: (torch.tensor) matrix
    :param num_clusters: (int) number of clusters
    :param distance: (str) distance [options: 'euclidean', 'cosine'] [default: 'euclidean']
    :param tol: (float) threshold [default: 0.0001]
    :param device: (torch.device) device [default: cpu]
    :return: (torch.tensor, torch.tensor) cluster ids, cluster centers
    """
    # print(f'running k-means on {device}..')
    if distance == 'euclidean':
        pairwise_distance_function = pairwise_distance
    elif distance == 'cosine':
        pairwise_distance_function = pairwise_cosine
    else:
        raise NotImplementedError

    # convert to float
    X = X.float()

    # transfer to device
    X = X.to(device)

    # initialize
    dis_min = float('inf')
    initial_state_best = None
    for i in range(20):
        initial_state = initialize(X, num_clusters)
        dis = pairwise_distance_function(X, initial_state).sum()
        if dis < dis_min:
            dis_min = dis
            initial_state_best = initial_state

    initial_state = initial_state_best
    iteration = 0
    while True:
        dis = pairwise_distance_function(X, initial_state)

        choice_cluster = torch.argmin(dis, dim=1)

        initial_state_pre = initial_state.clone()

        for index in range(num_clusters):
            selected = torch.nonzero(choice_cluster == index).squeeze().to(device)

            selected = torch.index_select(X, 0, selected)
            initial_state[index] = selected.mean(dim=0)

        center_shift = torch.sum(
            torch.sqrt(
                torch.sum((initial_state - initial_state_pre) ** 2, dim=1)
            ))

        iteration = iteration + 1

        if iteration > 500:
            break
        if center_shift ** 2 < tol:
            break

    return choice_cluster.cpu(), dis.cpu(), initial_state.cpu()


def kmeans_predict(
        X,
        num_clusters,
        distance='euclidean',
        tol=1e-4,
        device=torch.device('cuda')
):
    """
    perform kmeans
    :param X: (torch.tensor) matrix
    :param num_clusters: (int) number of clusters
    :param distance: (str) distance [options: 'euclidean', 'cosine'] [default: 'euclidean']
    :param tol: (float) threshold [default: 0.0001]
    :param device: (torch.device) device [default: cpu]
    :return: (torch.tensor, torch.tensor) cluster ids, cluster centers
    """
    # print(f'running k-means on {device}..')
    if distance == 'euclidean':
        pairwise_distance_function = pairwise_distance
    elif distance == 'cosine':
        pairwise_distance_function = pairwise_cosine
    else:
        raise NotImplementedError

    # convert to float
    X = X.float()

    # transfer to device
    X = X.to(device)

    # initialize
    dis_min = float('inf')
    initial_state_best = None
    for i in range(20):
        initial_state = initialize(X, num_clusters)
        dis = pairwise_distance_function(X, initial_state).sum() #
        if dis < dis_min:
            dis_min = dis
            initial_state_best = initial_state

    initial_state = initial_state_best
    iteration = 0
  
    while True:
        if X is None or initial_state is None:
            break

        dis = pairwise_distance_function(X, initial_state)
        choice_cluster = torch.argmin(dis, dim=1)

        initial_state_pre = initial_state.clone()

        for index in range(num_clusters):
            selected = torch.nonzero(choice_cluster == index).squeeze().to(device)

            if selected.numel() == 0:
                continue  #

            selected_points = torch.index_select(X, 0, selected)
            initial_state[index] = selected_points.mean(dim=0)

        center_shift = torch.sqrt(torch.sum((initial_state - initial_state_pre) ** 2)).item()

        # increment iteration
        iteration = iteration + 1

        if iteration > 500:
            break
        if center_shift ** 2 < tol:
            break

    return initial_state  #

#data1--X  data2--initial_state/cluster_centers
def pairwise_distance(data1, data2, device=torch.device('cuda')):
    # transfer to device
    data1, data2 = data1.to(device), data2.to(device)

    # N*1*M  7650*1*745
    A = data1.unsqueeze(dim=1)

    # 1*N*M 1*7*745
    B = data2.unsqueeze(dim=0)

    dis = (A - B) ** 2.0
    # return N*N matrix for pairwise distance
    dis = dis.sum(dim=-1).squeeze() 
    return dis


def pairwise_cosine(data1, data2, device=torch.device('cuda')):
    # transfer to device
    data1, data2 = data1.to(device), data2.to(device)

    # N*1*M
    A = data1.unsqueeze(dim=1)

    # 1*N*M
    B = data2.unsqueeze(dim=0)

    # normalize the points  | [0.3, 0.4] -> [0.3/sqrt(0.09 + 0.16), 0.4/sqrt(0.09 + 0.16)] = [0.3/0.5, 0.4/0.5]
    A_normalized = A / A.norm(dim=-1, keepdim=True)
    B_normalized = B / B.norm(dim=-1, keepdim=True)

    cosine = A_normalized * B_normalized

    # return N*N matrix for pairwise distance
    cosine_dis = 1 - cosine.sum(dim=-1).squeeze()
    return cosine_dis

