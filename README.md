# Enhancing Contrastive Graph Clustering with Reliable Sample Selection

### Overview

<p align = "justify"> 
• We propose a cross-view constrastive graph clustering framework, which fully exploits the inherent complementarity of attributes and structural information within the graph topology, and effectively avoids complex structure-level and attribute-level data augmentation.
• We design a reliable sample guided graph contrastive learning mechanism by constructing high-quality positive and negative sample pairs, effectively avoiding semantic drift and indiscriminative samples caused by introducing samples with misleading category information.
• To eliminate the semantic compatibility between graph contrastive learning and clustering tasks, we propose a simple yet effective self-optimizing module guided by reliable objective function. Extensive experiments on multiple datasets show that our proposed model could achieve state-of-the-art performance.




<div  align="center">    
    <img src="./assets/CCGC_model.png" width=80%/>
</div>

<div  align="center">    
    Figure 1: Overall framework of CCGC.
</div>



### Requirements

The proposed CCGC is implemented with python 3.7 on a NVIDIA 2080Ti GPU. 

Python package information is summarized in **requirements.txt**:

- torch==1.7.1
- tqdm==4.59.0
- numpy==1.19.2
- munkres==1.1.4
- scikit_learn==1.2.0





### Quick Start

python train.py



### Clustering Results

<div  align="center">    
    <img src="./assets/CCGC_result.png" width=100%/>
</div>
<div  align="center">    
    Table 1: Clustering results of our proposed CCGC and twelve baselines on six datasets.
</div>


<div  align="center">    
    <img src="./assets/CCGC_tsne.png" width=100%/>
</div>


<div  align="center">    
    Figure 2: 2D <i>t</i>-SNE visualization of six methods on two datasets.
</div>



### Citation

If you find this project useful for your research, please cite your paper with the following BibTeX entry.

```
@inproceedings{CCGC,
  title={Cluster-guided Contrastive Graph Clustering Network},
  author={Yang, Xihong and Liu, Yue and Zhou, Sihang and Wang, Siwei and Tu, Wenxuan and Zheng, Qun and Liu, Xinwang and Fang, Liming and Zhu, En},
  booktitle={Proceedings of the AAAI conference on artificial intelligence},
  volume={37},
  number={9},
  pages={10834--10842},
  year={2023}
}
```
