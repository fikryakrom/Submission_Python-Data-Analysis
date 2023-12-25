# Submission Dicoding "Belajar Data Analytics dengan Python"

## Description

Project ini bertujuan untuk menganalisis ***Bike Sharing Datasets*** dengan visualisasi data berbasis cloud melalui [streamlit](https://streamlit.io/)

## Data Sources
Kaggle Bike Sharing Datasets > [Download](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/data)

## Directory Structure

```
├── dashboard
│   └── dashboard.py
├── data
│   ├── Readme.txt
│   ├── day.csv
|   └── hour.csv
├── README.md
├── notebook.ipynb
└── requirements.txt
```

## Installation

1. Clone The Repo

   ```shell
   git clone https://github.com/fikryakrom/Submission_Python-Data-Analysis.git
   ```

2. Installing Libraries
    ```bash
    pip install streamlit
    pip install -r requirements.txt
    ```

3. Kaggle Configuration
    ```bash
    !mkdir ~/.kaggle
    !touch ~/.kaggle/kaggle.json
    
    api_token = {"username":"username","key":"api-token"}
    
    import json
    
    with open('/root/.kaggle/kaggle.json', 'w') as file:
    json.dump(api_token, file)
    
    !chmod 600 ~/.kaggle/kaggle.json
    ```
    **Note**: Get your api_token here:
   [Kaggle API Token](https://www.kaggle.com/settings/account)

## Usage
1. Local Access:
    ```bash
    cd dashboard
    streamlit run dashboard.py
    ```

2. Cloud Access: [Project Data Analytics](https://data-analytics-project.streamlit.app/)

## Issues & Contribution
- For further issues or contribution, visit this [link](https://github.com/fikryakrom/Submission_Python-Data-Analysis/issues)
- Or [contact me](fikryakrom@gmail.com)

### Adios!