import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('debayank2024/ai-impact-on-jobs-and-salaries-2020-2026', path='.', unzip=True)
