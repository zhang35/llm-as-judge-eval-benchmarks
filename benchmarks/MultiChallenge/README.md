---
license: cc-by-4.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- multi-turn
- evaluation
- benchmark
- llm
pretty_name: MultiChallenge
size_categories:
- n<1K
dataset_info:
  features:
  - name: question_id
    dtype: string
  - name: axis
    dtype: string
  - name: conversation
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: target_question
    dtype: string
  - name: pass_criteria
    dtype: string
  - name: num_turns
    dtype: int32
  splits:
  - name: test
    num_bytes: 2126003
    num_examples: 266
  download_size: 975319
  dataset_size: 2126003
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
---

# MultiChallenge

MultiChallenge is a benchmark for evaluating large language models on multi-turn conversations. It tests whether models can maintain context, follow instructions, and reason correctly across extended dialogues.

## Dataset Description

- **Size:** 266 examples
- **Split:** test
- **Language:** English

## Evaluation Axes

| Axis | Description |
|------|-------------|
| `INFERENCE_MEMORY` | Tests whether the model can recall and reason over information from earlier turns |
| `INSTRUCTION_RETENTION` | Tests whether the model continues to follow instructions given in earlier turns |
| `SELF_COHERENCE` | Tests whether the model's responses remain internally consistent across turns |
| `RELIABLE_VERSION_EDITING` | Tests whether the model can reliably edit/update content across turns |

## Dataset Structure

Each example contains:

- **`question_id`**: Unique identifier for the question
- **`axis`**: The evaluation axis being tested
- **`conversation`**: List of conversation turns (role + content)
- **`target_question`**: The evaluation question to assess model performance
- **`pass_criteria`**: Expected answer for the evaluation question
- **`num_turns`**: Number of turns in the conversation

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("ScaleAI/MultiChallenge", split="test")
print(dataset[0])
```
