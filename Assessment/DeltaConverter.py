import pandas as pd

def calculate_category_summary(df, category_col, client_col, recommendation_col):
    # Ensure the columns are treated as strings and capitalize them
    df[category_col] = df[category_col].astype(str).str.title()  # Capitalize each word in the category
    df[client_col] = df[client_col].astype(str).str.lower()
    df[recommendation_col] = df[recommendation_col].astype(str).str.lower()

    df['Match'] = df[client_col] == df[recommendation_col]
    summary = df.groupby(category_col)['Match'].agg(['sum', 'count']).reset_index()

    # Special handling for MDE sheet's Attack Surface Reduction category
    if 'MDE' in df.name and 'Attack Surface Reduction' in df[category_col].values:
        asr_audit_count = df[(df[category_col] == 'Attack Surface Reduction') & (df[client_col] == 'audit')].shape[0]
        asr_block_count = df[(df[category_col] == 'Attack Surface Reduction') & (df[client_col] == 'block')].shape[0]
        summary['Summary'] = summary.apply(lambda x: f"{asr_audit_count} in Audit, {asr_block_count} in Block" 
                                             if x[category_col] == 'Attack Surface Reduction' 
                                             else f"{x['sum']}/{x['count']} Controls Satisfied", axis=1)
    else:
        summary['Summary'] = summary.apply(lambda x: f"{x['sum']}/{x['count']} Controls Satisfied", axis=1)
    
    # Replace NaN with "N/A" in the summary
    summary.fillna("N/A", inplace=True)
    
    return summary

def determine_score_color(percentage):
    if percentage <= 50:
        return "#FF4C4C"  # Red
    elif 51 <= percentage <= 69:
        return "#FFD700"  # Softer Yellow (Gold)
    else:
        return "#4CAF50"  # Green

def generate_html_report(excel_file_path, output_file_path):
    excel_data = pd.ExcelFile(excel_file_path)
    sheet_names = excel_data.sheet_names
    sheets_data = {sheet: pd.read_excel(excel_data, sheet_name=sheet) for sheet in sheet_names}

    summary_data = {}
    total_matches = 0
    total_rows = 0

    for sheet, data in sheets_data.items():
        data.name = sheet  # Assign the sheet name to the DataFrame for later use
        if 'Client Config' in data.columns and 'Recommendation' in data.columns and 'Category' in data.columns:
            summary = calculate_category_summary(data, 'Category', 'Client Config', 'Recommendation')
            # Exclude Attack Surface Reduction from scoring
            if sheet == 'MDE':
                summary_to_score = summary[summary['Category'] != 'Attack Surface Reduction']
            else:
                summary_to_score = summary
            sheet_matches = summary_to_score['sum'].sum()
            sheet_total = summary_to_score['count'].sum()
            summary_data[sheet] = {
                'summary': summary,
                'matches': sheet_matches,
                'total': sheet_total,
                'percentage': (sheet_matches / sheet_total) * 100 if sheet_total > 0 else 0
            }
            total_matches += sheet_matches
            total_rows += sheet_total

    overall_match_score = total_matches
    match_percentage = (overall_match_score / total_rows) * 100 if total_rows > 0 else 0
    overall_score_color = determine_score_color(match_percentage)

    html_report = f"""
    <html>
    <head>
        <title>Executive Report</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

            body {{
                font-family: 'Roboto', Arial, sans-serif;
                color: #333333;
                background-color: #f7f7f7;
                margin: 20px;
                padding: 0;
            }}
            h1 {{
                color: #FF7F00;
                text-align: center;
                font-size: 32px;
                margin-bottom: 40px;
            }}
            h2 {{
                color: {overall_score_color};
                border-bottom: 2px solid {overall_score_color};
                padding-bottom: 10px;
                margin-bottom: 20px;
                font-size: 24px;
                text-align: center;
            }}
            .industry-score {{
                font-size: 18px;
                color: black;
                text-align: center;
                margin-top: -15px;
                margin-bottom: 30px;
            }}
            h3 {{
                color: #000000; /* Black color for these sections */
                font-size: 20px;
                margin-top: 40px;
            }}
            .section {{
                margin-bottom: 40px;
            }}
            .section p {{
                margin-left: 20px;
                font-size: 16px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #FF7F00;  /* Orange color */
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            tr:hover {{
                background-color: #e6f7ff;
            }}
            .header-left {{
                text-align: left;
                font-size: 18px;
                font-weight: bold;
                color: black;
                position: absolute;
                top: 20px;
                left: 20px;
            }}
            .section-header {{
                background-color: {overall_score_color};
                color: white;
                padding: 10px;
                margin-bottom: 10px;
                font-size: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="header-left">Vault Insurance</div>
        <h1>Executive Report</h1>
        <h2>Overall Score: {match_percentage:.2f}%</h2>
        <div class="industry-score">Average Industry Score: 54.97%</div>
    """

    for sheet, data in summary_data.items():
        sheet_percentage = data['percentage']
        sheet_color = determine_score_color(sheet_percentage)
        html_report += f"""
        <div class="section-header" style="background-color:{sheet_color};">
            {sheet} Summary ({sheet_percentage:.2f}%)
        </div>
        <table>
            <tr>
                <th>Category</th>
                <th>Summary</th>
            </tr>
        """
        for _, row in data['summary'].iterrows():
            html_report += f"""
            <tr>
                <td>{row['Category']}</td>
                <td>{row['Summary']}</td>
            </tr>
            """
        html_report += """
            </table>
        </div>
        """

    # Adding the additional sections for "Executive Summary" and "Recommended Next Steps"
    html_report += """
        <div class="section">
            <h3>Executive Summary</h3>
            <p>  </div>

        <div class="section">
            <h3>Recommended Next Steps</h3>
            <p> </div>
    </body>
    </html>
    """

    with open(output_file_path, 'w') as file:
        file.write(html_report)

# Example usage:
generate_html_report('MDR Delta Assessment 2.0-Vault.xlsx', 'ExecutiveReport.html')
