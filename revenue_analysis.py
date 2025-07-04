{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "#one sample t-test\n"
      ],
      "metadata": {
        "id": "CUr6rQotKQDt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6Sjn7tMhJ8GC"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "from scipy import stats\n",
        "\n",
        "# Define the percentage changes for each company\n",
        "company_data = [\n",
        "    [4.75],\n",
        "    [32.20, 19.27, 6.15],\n",
        "    [4.96, 19.21, 9.93],\n",
        "    [27.80, 18.50, 5.49],\n",
        "    [102.61, 35.84, 10.04],\n",
        "    [8.77, -6.85, -3.46],\n",
        "    [31.45, 6.13, -0.80],\n",
        "    [28.16, 9.33, 8.62],\n",
        "    [45.79, 0.73, 1.90],\n",
        "    [46.15, 22.85],\n",
        "    [15.48, 4.81, 0.57],\n",
        "    [6.11, 7.75, 2.60],\n",
        "    [43.37, -9.94, 13.12]\n",
        "]\n",
        "\n",
        "# Hypothesized mean percentage change\n",
        "hypothesized_mean = 5\n",
        "\n",
        "# Perform a one-sample t-test for each company\n",
        "for i, changes in enumerate(company_data):\n",
        "    t_stat, p_value = stats.ttest_1samp(changes, hypothesized_mean)\n",
        "    print(f\"Company {i+1}: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}\")\n",
        "\n",
        "import numpy as np\n",
        "from scipy import stats\n",
        "\n",
        "# Define the percentage changes for each company\n",
        "company_data = [\n",
        "    [7.97, 10.84, 7.67],\n",
        "    [20.31, 7.85, 3.24],\n",
        "    [8.19, 30.02],\n",
        "    [101.21, 37.41, 15.48],\n",
        "    [15.94, 5.90, 0.79],\n",
        "    [23.31, 7.55, 6.04],\n",
        "    [31.45, 6.13, -0.80],\n",
        "    [40.40, 18.08, 14.50],\n",
        "    [52.53, -3.92, -1.29],\n",
        "    [37.50, 13.27, 5.21],\n",
        "    [18.83, 10.50, 5.16],\n",
        "    [15.78, 5.27, 1.72],\n",
        "    [69.74, 70.07, 31.07],\n",
        "    [35.98, 25, 11.47],\n",
        "    [44.37, 3.63, 0.15],\n",
        "    [21.38, 6.30, -0.75],\n",
        "    [19.79, 7.49, 1.75],\n",
        "    [4.95, 5.25, 5.16]\n",
        "]\n",
        "\n",
        "# Hypothesized mean percentage change\n",
        "hypothesized_mean = 5\n",
        "\n",
        "# Perform a one-sample t-test for each company\n",
        "for i, changes in enumerate(company_data):\n",
        "    t_stat, p_value = stats.ttest_1samp(changes, hypothesized_mean)\n",
        "    print(f\"Company {i+1}: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#welch's T-test\n"
      ],
      "metadata": {
        "id": "R2V7sc8PKFVM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pandas scipy\n",
        "pip install openpyxl\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "# Group data based on Celebrity Promotion\n",
        "celebrity_promo = df[df['Celebrity_Promotion'] == 1]  # Assuming 1 indicates celebrity promotion\n",
        "no_celebrity_promo = df[df['Celebrity_Promotion'] == 0]  # Assuming 0 indicates no celebrity promotion\n",
        "# Convert percentage strings to floats\n",
        "for year in ['year_1', 'year_2', 'year_3']:\n",
        "    df[year] = df[year].str.rstrip('%').astype(float)\n",
        "# Clean the datasets by dropping NaN values\n",
        "celebrity_promo_cleaned = celebrity_promo.dropna(subset=['year_1', 'year_2', 'year_3'])\n",
        "no_celebrity_promo_cleaned = no_celebrity_promo.dropna(subset=['year_1', 'year_2', 'year_3'])\n",
        "# Remove percentage signs and convert to float\n",
        "celebrity_promo_cleaned['year_1'] = celebrity_promo_cleaned['year_1'].str.replace('%', '').astype(float)\n",
        "celebrity_promo_cleaned['year_2'] = celebrity_promo_cleaned['year_2'].str.replace('%', '').astype(float)\n",
        "celebrity_promo_cleaned['year_3'] = celebrity_promo_cleaned['year_3'].str.replace('%', '').astype(float)\n",
        "\n",
        "no_celebrity_promo_cleaned['year_1'] = no_celebrity_promo_cleaned['year_1'].str.replace('%', '').astype(float)\n",
        "no_celebrity_promo_cleaned['year_2'] = no_celebrity_promo_cleaned['year_2'].str.replace('%', '').astype(float)\n",
        "no_celebrity_promo_cleaned['year_3'] = no_celebrity_promo_cleaned['year_3'].str.replace('%', '').astype(float)\n",
        "from scipy.stats import ttest_ind\n",
        "\n",
        "# Perform t-tests for each year\n",
        "for year in ['year_1', 'year_2', 'year_3']:\n",
        "    t_stat, p_value = ttest_ind(\n",
        "        celebrity_promo_cleaned[year],\n",
        "        no_celebrity_promo_cleaned[year],\n",
        "        equal_var=False  # Use Welch's t-test\n",
        "    )\n",
        "    print(f'{year} - t-statistic: {t_stat}, p-value: {p_value}')\n",
        "\n"
      ],
      "metadata": {
        "id": "qRW7I4SOKKQi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6VvnQsyJKK5v"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
