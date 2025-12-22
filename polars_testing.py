import polars as pl

# Step 1: Create a sample DataFrame with a struct column
def create_nested_dataframe():
    data = {
        "motor_type": ["type_A", "type_B", "type_C", "type_A"],
        "motor_health": [
            {"type_A": {"status": "OK", "score": 85}, "type_B": {"status": "Fail", "score": 50}},
            {"type_B": {"status": "OK", "score": 90}, "type_C": {"status": "OK", "score": 75}},
            {"type_A": {"status": "Fail", "score": 40}, "type_C": {"status": "OK", "score": 80}},
            {"type_A": {"status": "OK", "score": 88}, "type_B": {"status": "Fail", "score": 55}},
        ],
    }
    return pl.DataFrame(data)

# Step 2: Combine columns and dynamically access the desired field
def process_combined_struct(df):
    # Combine the two columns into a single struct column
    df = df.with_columns(
        pl.struct(["motor_type", "motor_health"]).alias("combined_struct")
    )

    df = df.with_columns(
        pl.col("combined_struct").list.get(1).struct.field(df[0 , "combined_struct"]).struct
    )

    print(df)

    return df

# Step 3: Test the script
def test_script():
    df = create_nested_dataframe()
    print("Original DataFrame:")
    print(df)

    processed_df = process_combined_struct(df)
    print("\nProcessed DataFrame:")
    print(processed_df)

# Execute the script
if __name__ == "__main__":
    test_script()