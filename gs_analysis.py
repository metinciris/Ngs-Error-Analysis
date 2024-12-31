import pandas as pd
from tkinter import Tk, filedialog
import os

def analyze_ngs_errors():
    # Set up Tkinter to select files
    root = Tk()
    root.withdraw()
    root.update()
    file_paths = filedialog.askopenfilenames(title="Select CSV files for NGS analysis", filetypes=[("CSV files", "*.csv")])
    if not file_paths:
        print("No files selected. Exiting.")
        root.destroy()
        return

    root.destroy()

    # Read and analyze data
    combined_data = []

    for file_path in file_paths:
        df = pd.read_csv(file_path)
        if {'Gene Symbol', 'Transcript Variant', 'Protein Variant', 'Case Samples With Variant'}.issubset(df.columns):
            extracted_data = df[
                ['Gene Symbol', 'Transcript Variant', 'Protein Variant', 'Case Samples With Variant']
            ].copy()
            extracted_data['Source File'] = os.path.basename(file_path).replace(".csv", "")
            combined_data.append(extracted_data)

    if not combined_data:
        print("No valid data found in the selected files.")
        return

    # Combine all extracted data into one DataFrame
    combined_df = pd.concat(combined_data, ignore_index=True)

    # Group by Gene Symbol, Transcript Variant, and Protein Variant to count occurrences
    mutation_summary = (
        combined_df.groupby(['Gene Symbol', 'Transcript Variant', 'Protein Variant'])
        .agg(
            TotalPatients=('Case Samples With Variant', 'sum'),
            Occurrences=('Case Samples With Variant', 'count'),
            FilesContainingMutation=("Source File", lambda x: ", ".join(sorted(set(x))))
        )
        .reset_index()
    )

    # Prepare text output
    output_lines = []
    file_names = [os.path.basename(fp).replace(".csv", "") for fp in file_paths]
    for idx, file_name in enumerate(file_names, start=1):
        output_lines.append(f"{idx}. {file_name}")

    output_lines.append("\nMutation Summary:")
    for _, row in mutation_summary.iterrows():
        mutation_info = (
            f"{row['Gene Symbol']} | ({row['Occurrences']}) |{row['Transcript Variant']} | Protein: {row['Protein Variant']} | "
            f"Occurrences: {row['Occurrences']}  |   {row['FilesContainingMutation']}"
        )
        output_lines.append(mutation_info)

    # Write to a text file
    output_file = filedialog.asksaveasfilename(
        title="Save analysis results as", 
        defaultextension=".txt", 
        filetypes=[("Text files", "*.txt")]
    )

    if output_file:
        with open(output_file, "w") as f:
            f.write("\n".join(output_lines))
        print(f"Analysis complete. Results saved to {output_file}")
    else:
        print("No output file selected. Exiting.")

if __name__ == "__main__":
    analyze_ngs_errors()
