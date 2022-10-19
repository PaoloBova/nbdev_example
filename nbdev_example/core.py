# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['generate_crd']

# %% ../nbs/00_core.ipynb 8
def generate_crd(config:dict={}):
    "Generate a model of a Collective-risk dilemma, using any specifed config options."
    game = {}
    game['parameters'] = {}
    game['parameters']['n'] = config.get('n', 2)
    game['parameters']['b'] = config.get('b', 1)
    game['parameters']['d'] = config.get('d', -10)
    game['parameters']['pr'] = config.get('pr', 0.5)
    return game
