# Squirrel Behaviour Analysis Data Science Report

## Contributors

| Name | Email |
|------|-------|
| Eiyrea Nabilla binti Azmi | eiyreanabillabinti.azmi@student.unimelb.edu.au |
| Farrell Aurelio William | farrellaurelio.william@student.unimelb.edu.au |
| Farah Aulia Zahra Irawan | firawan@student.unimelb.edu.au |
| Keane Manuel | keane.manuel@student.unimelb.edu.au |

## Research Question

Which behavioural and environmental factors are most strongly associated with squirrel approaches toward humans in Central Park, and can we reliably predict this behaviour?

---

## Files

| File | Description |
|------|-------------|
| `A2_Squirrel_Analysis_v4.ipynb` | Main analysis notebook |
| `squirrel.csv` | 3,023 squirrel sighting records (31 variables) |
| `hectare.csv` | 700 hectare-level environmental records |
| `stories.csv` | 809 qualitative field notes (loaded but unused) |

Place all four files in the same folder before running.

---

## Setup

Python 3.9 or above is required. Install all dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

---

## How to Run

1. Place the notebook and all three CSVs in the same folder.
2. Launch Jupyter:
```bash
   jupyter notebook   # or: jupyter lab
```
3. Open `A2_Squirrel_Analysis_v4.ipynb`.
4. Run all cells in order: **Kernel → Restart & Run All**

> Do NOT run cells out of order — later cells depend on earlier ones.

Expected runtime: 5–20 seconds.

---

## Notebook Structure

| Section | Content |
|---------|---------|
| 0 | Imports and library setup |
| 1 | Load data |
| 2 | Exploratory Data Analysis (EDA) |
| 3 | Preprocessing (column removal, imputation, feature engineering, encoding, undersampling) |
| 4 | Correlation Analysis (Pearson, NMI, heatmap) |
| 5 | Supervised Learning (Decision Tree, KNN, confusion matrices, feature importance) |
| 6 | Clustering (KMeans k=4, Hierarchical, PCA, silhouette scores) |
| 7 | Summary table |

---

## Outputs

All figures are saved as `.png` files in the notebook directory.

**EDA**
- `eda_behaviour_rates.png` — Figure 1
- `eda_categorical.png` — Figure 2
- `eda_spatial.png` — Figure 3

**Preprocessing**
- `preprocessing_impact.png` — Figure 4

**Correlation**
- `correlation_with_target.png` — Figure 5
- `nmi_with_target.png` — Figure 6
- `correlation_heatmap.png` — Figure 7
- `behaviour_by_approach.png` — Figure 18

**Supervised Learning**
- `confusion_matrices.png` — Figure 8
- `decision_tree_viz.png` — Figure 9
- `knn_k_selection.png` — Figure 10
- `feature_importance_dt.png` — Figure 11

**Clustering**
- `elbow_plot.png` — Figure 12
- `silhouette_scores.png` — Figure 13
- `dendrogram.png` — Figure 14
- `cluster_profiles.png` — Figure 15
- `cluster_pca.png` — Figure 16
- `approach_by_cluster.png` — Figure 17

All printed numerical results correspond directly to values reported in `A2_Report_Final.pdf`.

---

## Notes

- Data file path is configurable via `DATA_DIR` at the top of Section 1 (default: `'.'`).
- All random operations use `random_state=42` for reproducibility.
- Clustering runs on the full dataset (n=3,023), not the balanced subset.
- The KNN Pipeline prevents data leakage by fitting the scaler only on training folds.
- `stories.csv` is loaded but not used — included for completeness.
