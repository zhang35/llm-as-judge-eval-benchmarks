---
language:
- en
size_categories:
- 1K<n<10K
tags:
- agents
- web
- llm
task_categories:
- robotics
configs:
- config_name: annotations
  default: true
  data_files:
  - split: full
    path: data/annotations.csv
---

<div align="center">

# AgentRewardBench

| [**💾Code**](https://github.com/McGill-NLP/agent-reward-bench) |[**📄Paper**](https://arxiv.org/abs/2504.08942) | [**🌐Website**](https://agent-reward-bench.github.io) | 
| :--: | :--: | :--: |
| [**🤗Dataset**](https://huggingface.co/datasets/McGill-NLP/agent-reward-bench) | [**💻Demo**](https://huggingface.co/spaces/McGill-NLP/agent-reward-bench-demo) |  [**🏆Leaderboard**](https://huggingface.co/spaces/McGill-NLP/agent-reward-bench-leaderboard) | 

<br>

**[AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://arxiv.org/abs/2504.08942)**  
*[Xing Han Lù](https://xinghanlu.com/), [Amirhossein Kazemnejad*](https://kazemnejad.com/), <br>[Nicholas Meade](https://ncmeade.github.io/), [Arkil Patel](https://arkilpatel.github.io/), [Dongchan Shin](https://scholar.google.com/citations?user=QzZOkfIAAAAJ&hl=en), [Alejandra Zambrano](https://www.linkedin.com/in/alejandra-zambrano-a71092196/), <br>[Karolina Stańczak](https://kstanczak.github.io/), [Peter Shaw](https://www.ptshaw.com/), [Christopher J. Pal](https://sites.google.com/view/christopher-pal), [Siva Reddy](https://sivareddy.in/)*  
*\*Core Contributor*

</div>


![Image showing an example](https://agent-reward-bench.github.io/assets/primary.png)


## Loading dataset

You can use the `huggingface_hub` library to load the dataset. The dataset is available on Huggingface Hub at `McGill-NLP/agent-reward-bench`.

```python
from huggingface_hub import snapshot_download

# Download the dataset to ./trajectories/
snapshot_download(
    repo_id="McGill-NLP/agent-reward-bench",
    repo_type="dataset",
    local_dir="./trajectories/"
)
```

<details>
<summary>Click to see the folder structure</summary>

```
trajectories/
├── cleaned/
│   ├── assistantbench/
│   │   ├── GenericAgent-<LLM>/
│   │   │   ├── GenericAgent-<LLM>_on_<benchmark>.<split>/
│   │   │   |   ├── <benchmark>.<split>.0.json
│   │   │   |   ├── ...
│   │   │   ├── ...
|   |   ├── ...
│   ├── visualwebarena/
│   │   ├── ...
│   ├── webarena/
│   │   ├── ...
│   ├── workarena/
│   │   ├── ...
├── judgments/
│   ├── <benchmark>/
│   │   ├── GenericAgent-<LLM>/
│   │   │   ├── <judge>/
│   │   │   |   ├── <benchmark>.<split>.0.json
│   │   │   |   ├── ...
│   ├── ...
├── screenshots/
│   ├── <benchmark>/
│   │   ├── GenericAgent-<LLM>/
│   │   │   ├── <benchmark>.<split>.0/
│   │   │   |   ├── screenshot_step_0.png
│   │   │   |   ├── ...
│   │   │   ├── ...
│   │   ├── ...
│   ├── visualwebarena/
│   │   ├── ...
│   ├── ...
```
</details>

## Terms of Use

By downloading this Dataset, you agree to comply with the following terms of use:
- Restrictions: You agree not to use the Dataset in any way that is unlawful or would infringe upon the rights of others.
- Acknowledgment: By using the Dataset, you acknowledge that the Dataset may contain data derived from third-party sources, and you agree to abide by any additional terms and conditions that may apply to such third-party data.
- Fair Use Declaration: The Dataset may be used for research if it constitutes "fair use" under copyright laws within your jurisdiction. You are responsible for ensuring your use complies with applicable laws.

Derivatives must also include the terms of use above.