def compare_dataframes(df_ans, df_o_r):
    # Ensure the dimensions match
    if df_ans.shape != df_o_r.shape:
        raise ValueError("CSV files have different dimensions")

    # Count the number of differing elements
    differing_elements_count = (df_ans != df_o_r).sum().sum()

    # Calculate the total number of elements
    total_elements = df_ans.shape[0] * df_ans.shape[1]

    # Calculate the differing rate
    differing_rate = (differing_elements_count / total_elements)

    return differing_rate
