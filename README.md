# Evasive PDF Malware Classifier

A machine learning project for detecting malicious PDF files using structural and content-based features.

## 📋 Project Overview

This project implements a machine learning pipeline to classify PDF files as either **malicious** (1) or **benign** (0) based on 20 structural features. The models are trained on an evasive PDF dataset containing 500,000 samples, specifically designed to test classifier robustness against evasion techniques.

## 📊 Dataset

**Source:** [Evasive PDF Samples on Kaggle](https://www.kaggle.com/datasets/fouadtrad2/evasive-pdf-samples)

**Dataset Statistics:**
- **Total Samples:** 500,000 PDFs
- **Malicious Samples:** 450,000 (90%)
- **Benign Samples:** 50,000 (10%)
- **Features:** 20 numerical features per sample

**Key Features:**
- Structural attributes: `pdfsize`, `pages`, `obj`, `stream`, etc.
- Content indicators: `JS`, `Javascript`, `OpenAction`, `Acroform`
- Obfuscation markers: `OBS_JS`, `OBS_Javascript`, etc.

## 🏗️ Project Structure

```
├── data/                    # Dataset files
├── notebooks/               # Jupyter notebooks for analysis
├── src/                     # Source code
│   ├── preprocessing.py     # Data cleaning and feature engineering
│   ├── models.py           # Model implementations
│   └── evaluation.py       # Performance evaluation
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 📈 Data Preprocessing

### Steps Performed:
1. **Missing Value Handling**: No missing values found in the dataset
2. **Feature Removal**: Removed redundant features (`endobj`, `endstream`) and low-variance features (`OBS_*` columns)
3. **Class Imbalance Handling**: Applied SMOTE (oversampling) and RandomUnderSampler techniques
4. **Train-Test Split**: 80-20 split with random state for reproducibility

### Final Feature Set (14 features):
- `pdfsize`, `pages`, `title characters`, `images`
- `obj`, `stream`, `xref`, `trailer`, `startxref`
- `JS`, `Javascript`, `OpenAction`, `Acroform`
- `class` (target variable)

## 🤖 Models Implemented

Three supervised learning algorithms were implemented and evaluated:

- 1. Decision Tree Classifier
- 2. K-Nearest Neighbors (KNN)
- 3. Neural Network (MLP)

## 📊 Results

### Performance Metrics (on full feature set):

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Decision Tree** | 99.83% | 99.92% | 99.90% | 99.91% |
| **KNN (k=5)** | 99.39% | 99.76% | 99.56% | 99.66% |
| **Neural Network** | 99.87% | 99.91% | 99.95% | 99.93% |

### Feature Importance Analysis:
The best performing features identified were:
1. `obj` (number of objects)
2. `pdfsize` (file size)
3. `pages` (page count)
4. `stream` (stream objects)
5. `Javascript` (JavaScript content)
6. `Acroform` (AcroForm presence)

## 🎯 Key Findings

1. **High Performance**: All models achieved >99% accuracy, with Neural Networks performing best
2. **Feature Reduction**: The 6 best features achieved comparable performance to the full feature set
3. **Imbalance Impact**: SMOTE oversampling improved minority class recall significantly
4. **Structural Dominance**: PDF structural features were more predictive than content-based features

## 📈 Visualizations

The project includes comprehensive visualizations:
- Class distribution pie charts
- Feature distribution histograms
- Correlation heatmaps
- Pair plots for best features
- Confusion matrices for each model

## 🔮 Future Work

Potential improvements and extensions:
2. **Ensemble Methods**: Combine models for improved robustness
3. **Deep Learning**: Experiment with CNN architectures on raw PDF bytes
4. **Feature Engineering**: Extract additional semantic features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
