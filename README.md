# Kaggle Competition Notebooks

A small archive of Kaggle competition/practice notebooks. The repository currently contains two notebooks and a saved CSV submission.

## Current contents

| File | Purpose |
|---|---|
| `Copy of podcast_listening_time.ipynb` | Notebook associated with a podcast-listening-time prediction competition |
| `Calories__Prediction.ipynb` | Calories-prediction notebook; confirm whether it belongs to the same competition before combining workflows |
| `submission.csv` | Saved submission output; verify which competition and notebook produced it before reusing |

## Results and context

The original project note records a rank of **2889 out of 3310** for the first podcast-listening-time competition. This is a historical self-reported result, not a current Kaggle leaderboard position.

## Recommended layout

For each competition, keep the notebook, project-specific README, requirements/versions, and submission file together. Do not overwrite a previous submission until you have confirmed its competition and expected schema.

If these notebooks belong to different competitions, the cleanest long-term setup is one repository per substantial competition, or one clearly named folder per competition with separate READMEs.

## Reproducing a notebook

1. Open the notebook and read its data-loading cells.
2. Download the dataset from the relevant Kaggle competition and place it in the expected local path.
3. Install the libraries used by the notebook.
4. Run from a clean kernel and confirm the generated submission columns match the competition's sample submission.

No claim is made that the notebooks currently execute end-to-end in a clean environment.

## Author

Kunal Goyal — [GitHub profile](https://github.com/KunalGoyal0601)
