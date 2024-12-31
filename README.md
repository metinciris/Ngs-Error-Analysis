# NGS Mutation Analysis Tool

## Overview
This Python tool provides an efficient method for analyzing Next-Generation Sequencing (NGS) mutation data from multiple CSV files. The tool identifies common mutations, their occurrences, and the files in which they appear, helping researchers pinpoint potential errors in sequencing data.

## Features
- **Multi-file Input:** Select and analyze multiple CSV files simultaneously.
- **Flexible Analysis:** Groups mutations by gene, transcript, and protein to calculate occurrences across files.
- **Detailed Output:** Outputs mutation data in a human-readable text format, including:
  - Gene name
  - Mutation type
  - Protein variant
  - Total occurrences
  - Files containing the mutation
- **User-friendly Interface:** Interactive file selection and output location dialogs.

## Requirements
- Python 3.7+
- Required Python libraries:
  - `pandas`
  - `tkinter`

Install dependencies using pip:
```bash
pip install pandas
```

## How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ngs-mutation-analysis.git
   cd ngs-mutation-analysis
   ```

2. **Run the Script**
   Execute the tool from the terminal:
   ```bash
   python ngs_analysis.py
   ```

3. **Select Files**
   - A file selection dialog will open. Choose the CSV files containing NGS data.

4. **Save Results**
   - After analysis, specify a location to save the results as a `.txt` file.

## Output Format
The output file contains:

1. **List of Input Files:**
   ```
   1. Patient426
   2. Patient431
   3. Patient433
   ```

2. **Mutation Summary:**
   ```
   ALK | (9) |c.1500A>G | Protein: p.Q500Q | Occurrences: 9  |   Patient426, Patient431, Patient433, Patient435, Patient436, Patient438, Patient439, Patient440, Patient441
   ```

## Customization
Feel free to modify the script to adapt to different CSV formats or additional analysis requirements.

## Contributing
Contributions are welcome! Fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

