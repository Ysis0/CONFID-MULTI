# Enhancing Contrastive Graph Clustering with Reliable Sample Selection

### Overview

<p align = "justify"> 
• We propose a cross-view constrastive graph clustering framework, which fully exploits the inherent complementarity of attributes and structural information within the graph topology, and effectively avoids complex structure-level and attribute-level data augmentation.
• We design a reliable sample guided graph contrastive learning mechanism by constructing high-quality positive and negative sample pairs, effectively avoiding semantic drift and indiscriminative samples caused by introducing samples with misleading category information.
• To eliminate the semantic compatibility between graph contrastive learning and clustering tasks, we propose a simple yet effective self-optimizing module guided by reliable objective function. Extensive experiments on multiple datasets show that our proposed model could achieve state-of-the-art performance.




<div  align="center">    
    <img src="./assets/model.png" width=80%/>
</div>

<div  align="center">    
    Figure 1: Overall framework of CONFID-MULTI.
</div>

### The clustering performance is reported by ten runs, including mean and standard deviation. The best and second-best results in the table are displayed in red and blue, respectively.

<div  align="center">    
    <img src="./assets/comparison.png" width=100%/>
</div>




```
