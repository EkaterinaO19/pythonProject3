import shutil
import os

def clean_allure_results(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

if __name__ == "__main__":
    clean_allure_results("allure-results")