### Environment
Python with `torch`, `timm`, `scikit-learn`, `numpy`, `scipy`, `pandas`, `matplotlib` and `wandb`.

`wandb` has to be installed even though it’s disabled, because it’s imported at the top of the training script. 

I’d pin timm to `0.9.x`, since the model imports timm.models.registry and timm.models.layers, which newer timm versions may have removed. That’s a guess from the imports.

### Get the data. 
The .pkl files are gitignored, so they aren’t in the repo.

`dataset/Dataset_May/README.md` links to a Google Drive folder of `.tar.bz2` archives. Extract them with `tar -jxvf <file>.tar.bz2` and you get one folder per scenario, each with 48 pickles.

### Lay out the folders. 
Put the extracted folders in `sub_sig_former/dataset/New_dataset_May/`. The loader expects `<root>/<prefix>/<prefix>_TP{tp}_D{d}_SR20_CF2360_I0.pkl`, and the `-x 1` runs need matching `...-Time-Freq.pkl` files. 

The 0521 script maps H to `Dataset_EIB_3F_Hallway_0521` and R to `Dataset_EIB_room328_to_Hallway_0521`. I found nothing in the repo that generates the `-Time-Freq` files or the `_0521` datasets, so you’ll need to find those from wherever you made them.

### Fix the model output. 
`sub_sig_former/sig_former_meta.py` has forward returning (x, y_f), but the training loop does criterion(model(data), target). That will crash. Either change forward to return x, or change the training and evaluate loops to output, _ = model(data).

### Run each condition twice, once without and once with the feature. 
Use a bash shell (Git Bash or WSL) in `sub_sig_former/script`. If you get \r errors, run `sed -i 's/\r$//' xcit_multifiles_0521.sh`.
