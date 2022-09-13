from pepe_semantics import config

import gdown

_GIDS_PATHS = (
    config.BERTWEET_WEIGHTS_PATHS,
    config.GIF_ID_TO_INFERRED_FEATURE_PATHS,
    config.GIF_ID_TO_GIPHY_ID_PATHS,
)


def main():
    for gdrive_id, save_fpath in _GIDS_PATHS:
        save_fpath.resolve().parent.mkdir(exist_ok=True, parents=True)
        gdown.download(id=gdrive_id, output=str(save_fpath), quiet=False)

if __name__ == "__main__":
    main()
