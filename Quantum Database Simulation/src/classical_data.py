"""
This module generates salary data for men and women distributed across departments.
It finds the departments with equal pay. The generated data is then normalized to
be reused in the quantum simulation

Author: Ricard Santiago Raigada García
Date: 06/12/2024
Version: 0.0.1
"""
import pandas as pd
import numpy as np
from typing import List, Tuple
from sklearn.preprocessing import MinMaxScaler


def generate_normalized_inputs(
    seed: int=42,
    equal_department: int=2
    ) -> Tuple[List[List[int]], List[int]]:
    """
    Generate normalized input data for quantum simulation,
    and find the solution classically for demonstration and
    comparison purposes

    Args:
        seed (int, optional): sed for random number generation. Defaults to 42
        equal_department (int, optional): department to enforce equal pay. Defaults to 2

    Returns:
        Tuple[List[List[int]], List[int]]:
            normalized inputs for simulation
            list of departments with equal pay
    """
    np.random.seed(seed)
    man = np.random.randint(1000, 5000, 12)
    female = np.random.randint(1000, 5000, 12)
    Departments = np.tile([1, 2, 3, 4], 3)

    df = pd.DataFrame({
        "man": man,
        "female": female,
        "Department": Departments
    })

    df.loc[df["Department"] == equal_department, "female"] = df.loc[
        df["Department"] == equal_department, "man"
    ].values

    df_grouped = df.groupby("Department").sum().reset_index()
    df_grouped["Diferencia"] = df_grouped["man"] - df_grouped["female"]

    equal_departments = df_grouped[
        df_grouped["Diferencia"] == 0
        ][
            "Department"
            ].tolist()
    print("Department with equal pay:", equal_departments)

    inputs = []
    for Department in df["Department"].unique():
        man = df[df["Department"] == Department]["man"].values[:3]
        female = df[df["Department"] == Department]["female"].values[:3]
        vector = list(man) + list(female)
        inputs.append(vector)

    flattened = np.array(inputs).flatten()
    scaler = MinMaxScaler(feature_range=(1, 15))
    scaler.fit(flattened.reshape(-1, 1))
    normalized_inputs = [
        scaler.transform(np.array(vec).reshape(-1, 1)).flatten().round().astype(int).tolist()
        for vec in inputs
    ]
    return normalized_inputs, equal_departments
