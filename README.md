# An interface to query OpenAI's GPT model

The `GPT` class provides functionality to query GPT 4 in a chat interface while logging all conversations and automatically retrying after a RateLimitError from OpenAI. A demo for using `GPT` is provided in `run.py` and `run.ipynb`. 

You will need to a YAML file called `gpt.yaml` with the `openai` information filled in. Fill in the OpenAI infomration (such as API key) here. 

```YAML
gpt: 
  _target_: gpt4.GPT
  openai_api_type:  
  openai_api_base: 
  openai_api_version: 
  openai_api_key: 
  engine: largeGPT4
  temperature: 0.7
  system_prompt: You are a helpful assistant.
  log_dir: ${hydra:run.dir}
```

Use in a python script like this 

```python
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path=".", config_name="gpt")
def experiment(cfg): 
    gpt = hydra.utils.instantiate(cfg.gpt)
    _ = gpt.ask('What year is it?', verbose=True)

if __name__ == "__main__":
    experiment()
```

and in a jupyter notebook like this

```python
import hydra 
from omegaconf import OmegaConf
from gpt4 import GPT 

with hydra.initialize(version_base=None, config_path="."):
    cfg = hydra.compose(con fig_name="gpt", return_hydra_config=True, overrides=["gpt.log_dir=${hydra.run.dir}"])
    os.makedirs(cfg.gpt.log_dir, exist_ok=True)

gpt = hydra.utils.instantiate(cfg.gpt)
```