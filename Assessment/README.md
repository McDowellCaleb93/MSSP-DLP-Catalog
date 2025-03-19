## Overview

The script reads an Excel file with multiple sheets. For each sheet that contains the required columns (\`Category\`, \`Client Config\`, and \`Recommendation\`), it:
- **Normalizes and Capitalizes Data:** Converts category names to title case and client configuration/recommendation values to lower case.
- **Calculates a Category Summary:** Groups data by category to compute the number of matching controls against total controls.
- **Special Handling:** Applies extra logic for the \"Attack Surface Reduction\" category on the **MDE** sheet.
- **Aggregates Scores:** Computes overall and per-sheet compliance scores.
- **Generates an HTML Report:** Produces a responsive report with color-coded scores, summary tables, an executive summary, and recommended next steps.

---

## Features

- **Data Normalization:** Ensures consistent formatting by capitalizing category names and lowercasing configuration values.
- **Category Summary Calculation:** Computes matching control counts per category.
- **Special Case Handling:** Implements unique logic for the \"Attack Surface Reduction\" category in the MDE sheet.
- **Dynamic HTML Report:** Creates an HTML file featuring:
  - Overall and per-sheet compliance scores.
  - Color-coded sections based on score thresholds.
  - Detailed summary tables.
  - Predefined narrative sections for an Executive Summary and Recommended Next Steps.
- **Customizable Styling:** Uses CSS (with Google Fonts) for a professional and easily modifiable layout.

---

## Getting Started

### Prerequisites

- **Python 3.x**  
- **Pandas:**  
  Install via pip if not already installed:
  \`\`\`bash
  pip install pandas
  \`\`\`

### Files

- **\`MDR Delta Assessment 2.0-Vault.xlsx\`**  
  The Excel workbook containing the assessment data. Ensure it is in the same directory or update the file path in the script.

- **\`ExecutiveReport.html\`**  
  The output file where the generated HTML report will be saved.

---

## How to Use

1. **Prepare Your Excel File:**  
   Ensure the Excel file has the required columns: \`Category\`, \`Client Config\`, and \`Recommendation\`.

2. **Run the Script:**  
   Execute the script by running:
   \`\`\`bash
   python <your_script_name>.py
   \`\`\`
   This will process the Excel file and generate \`ExecutiveReport.html\`.

3. **View the Report:**  
   Open \`ExecutiveReport.html\` in your web browser to view the report.

---

## Code Structure

- **\`calculate_category_summary(df, category_col, client_col, recommendation_col)\`**  
  Processes each DataFrame to compute the number of matching controls per category and handles special formatting for the MDE sheet.

- **\`determine_score_color(percentage)\`**  
  Returns a specific color code based on the compliance percentage:
  - **Red:** ≤50%
  - **Gold (Softer Yellow):** 51% to 69%
  - **Green:** ≥70%

- **\`generate_html_report(excel_file_path, output_file_path)\`**  
  Reads the Excel workbook, processes each sheet, aggregates results, and generates the final HTML report with CSS styling and narrative sections.

---

## Customization

- **Styling:**  
  Modify the CSS in the <style> tag within the generated HTML for a customized look.

- **Data Handling:**  
  Adjust column names or special-case logic in the \`calculate_category_summary\` function if your data structure changes.

- **Report Content:**  
  The Executive Summary and Recommended Next Steps are currently hardcoded. Edit these sections to match your organization's messaging as needed.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to open issues or contribute to enhance the functionality of this report generator. Enjoy generating insightful and visually appealing executive reports for your security assessments!" > README.md
