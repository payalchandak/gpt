import hydra # type: ignore
from omegaconf import DictConfig, OmegaConf # type: ignore

@hydra.main(version_base=None, config_path=".", config_name="gpt")
def experiment(cfg): 
    gpt = hydra.utils.instantiate(cfg.gpt)
    _ = gpt.ask('What year is it?', verbose=True)

if __name__ == "__main__":
    experiment()