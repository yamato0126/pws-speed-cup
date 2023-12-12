def calculate_differing_rate(df_1, df_2):
    # Ensure the dimensions match
    if df_1.shape != df_2.shape:
        raise ValueError("CSV files have different dimensions")

    # Count the number of differing elements
    differing_elements_count = (df_1 != df_2).sum().sum()

    # Calculate the total number of elements
    total_elements = df_1.shape[0] * df_1.shape[1]

    # Calculate the differing rate
    differing_rate = (differing_elements_count / total_elements)

    return differing_rate
