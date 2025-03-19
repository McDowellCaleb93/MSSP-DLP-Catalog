import pandas as pd

def calculate_category_summary(df, category_col, client_col, recommendation_col):
    """
    Process the DataFrame to compute summary statistics for each category.
    
    - Normalizes text in the specified columns.
    - Creates a new column 'Match' indicating if the client configuration matches the recommendation.
    - Groups by category and computes the number of matches and total counts.
    - Applies special handling for the 'Attack Surface Reduction' category if the sheet name is 'MDE'.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        category_col (str): Column name for categories.
        client_col (str): Column name for client configuration.
        recommendation_col (str): Column name for recommendations.
    
    Returns:
        pd.DataFrame: A summary DataFrame with aggregated values.
    """
    # Normalize text formatting
    df[category_col] = df[category_col].astype(str).str.title()
    df[client_col] = df[client_col].astype(str).str.lower()
    df[recommendation_col] = df[recommendation_col].astype(str).str.lower()

    # Create a boolean column where True indicates a match between Client Config and Recommendation
    df['Match'] = df[client_col] == df[recommendation_col]
    summary = df.groupby(category_col)['Match'].agg(['sum', 'count']).reset_index()

    # Special handling for MDE sheet's Attack Surface Reduction category
    if hasattr(df, 'name') and 'MDE' in df.name and 'Attack Surface Reduction' in df[category_col].values:
        asr_audit_count = df[(df[category_col] == 'Attack Surface Reduction') & (df[client_col] == 'audit')].shape[0]
        asr_block_count = df[(df[category_col] == 'Attack Surface Reduction') & (df[client_col] == 'block')].shape[0]
        summary['Summary'] = summary.apply(
            lambda x: f"{asr_audit_count} in Audit, {asr_block_count} in Block" 
                      if x[category_col] == 'Attack Surface Reduction' 
                      else f"{x['sum']}/{x['count']} Controls Satisfied", axis=1)
    else:
        summary['Summary'] = summary.apply(lambda x: f"{x['sum']}/{x['count']} Controls Satisfied", axis=1)
    
    summary.fillna("N/A", inplace=True)
    return summary

def determine_score_color(percentage):
    """
    Returns a color code based on the provided percentage.
    
    - ≤50%: Red (Material Red: #D32F2F)
    - 51% to 69%: Amber (Material Amber: #FFA000)
    - ≥70%: Green (Material Green: #388E3C)
    
    Parameters:
        percentage (float): The percentage score.
        
    Returns:
        str: A hexadecimal color code.
    """
    if percentage <= 50:
        return "#D32F2F"  # Professional red
    elif 51 <= percentage <= 69:
        return "#FFA000"  # Professional amber
    else:
        return "#388E3C"  # Professional green

def generate_html_report(excel_file_path, output_file_path):
    """
    Generates an executive HTML report from an Excel workbook.
    
    The function reads each sheet from the Excel file, computes summary statistics for each category,
    and produces an HTML file with styled tables and narrative sections.
    
    Parameters:
        excel_file_path (str): Path to the input Excel file.
        output_file_path (str): Path to save the generated HTML report.
    """
    # Load Excel workbook and each sheet as a DataFrame
    excel_data = pd.ExcelFile(excel_file_path)
    sheet_names = excel_data.sheet_names
    sheets_data = {sheet: pd.read_excel(excel_data, sheet_name=sheet) for sheet in sheet_names}

    summary_data = {}
    total_matches = 0
    total_rows = 0

    for sheet, data in sheets_data.items():
        data.name = sheet  # Store sheet name for special handling
        required_cols = {'Client Config', 'Recommendation', 'Category'}
        if required_cols.issubset(data.columns):
            summary = calculate_category_summary(data, 'Category', 'Client Config', 'Recommendation')
            # For MDE sheet, exclude Attack Surface Reduction from overall scoring
            if sheet == 'MDE':
                summary_to_score = summary[summary['Category'] != 'Attack Surface Reduction']
            else:
                summary_to_score = summary
            sheet_matches = summary_to_score['sum'].sum()
            sheet_total = summary_to_score['count'].sum()
            percentage = (sheet_matches / sheet_total) * 100 if sheet_total > 0 else 0
            summary_data[sheet] = {
                'summary': summary,
                'matches': sheet_matches,
                'total': sheet_total,
                'percentage': percentage
            }
            total_matches += sheet_matches
            total_rows += sheet_total

    overall_match_score = total_matches
    match_percentage = (overall_match_score / total_rows) * 100 if total_rows > 0 else 0
    overall_score_color = determine_score_color(match_percentage)

    # Construct HTML report with improved styling and layout
    html_report = f"""
    <html>
    <head>
        <title>Executive Report</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

            body {{
                font-family: 'Roboto', Arial, sans-serif;
                background-color: #f5f5f5;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background-color: #fff;
                padding: 40px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
            .header-left {{
                font-size: 20px;
                font-weight: bold;
                color: #555;
                position: absolute;
                top: 20px;
                left: 20px;
            }}
            h1 {{
                color: #2C3E50;
                text-align: center;
                font-size: 36px;
                margin-bottom: 10px;
            }}
            h2 {{
                color: {overall_score_color};
                text-align: center;
                font-size: 28px;
                margin-top: 0;
                border-bottom: 2px solid {overall_score_color};
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            .industry-score {{
                text-align: center;
                font-size: 18px;
                color: #777;
                margin-bottom: 30px;
            }}
            h3 {{
                color: #2C3E50;
                font-size: 24px;
                margin-top: 40px;
            }}
            .section {{
                margin-bottom: 40px;
            }}
            .section p {{
                font-size: 16px;
                line-height: 1.6;
                margin: 10px 0;
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
                font-size: 16px;
            }}
            th {{
                background-color: {overall_score_color};
                color: #fff;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            tr:hover {{
                background-color: #e0f7fa;
            }}
            .section-header {{
                padding: 10px;
                font-size: 20px;
                color: #fff;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="header-left">Vault Insurance</div>
        <div class="container">
            <h1>Executive Report</h1>
            <h2>Overall Score: {match_percentage:.2f}%</h2>
            <div class="industry-score">Average Industry Score: 54.97%</div>
    """

    # Add section summaries for each sheet
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
        html_report += "</table>"

    # Append the narrative sections
    html_report += """
            <div class="section">
                <h3>Executive Summary</h3>
                <p>
                    The primary objective of the recent assessment and TPE engagement was to ensure that your Microsoft services 
                    are being utilized to their fullest potential. After a thorough analysis of your environment, we can confidently 
                    confirm that all the recommended tools have been effectively implemented. While most of your configurations align 
                    closely with our best practices, there are some deviations. However, these differences do not necessarily indicate 
                    suboptimal controls, as they have been thoughtfully implemented to align with Vault's specific business objectives.
                </p>
                <p>
                    During our discussions with your team, it was evident that most controls have been established with a clear intent 
                    to support these objectives. However, there were a few areas identified that required additional attention and 
                    enhancement, particularly in relation to Microsoft Defender for Cloud and Entra ID.
                </p>
                <p>
                    Within the scope of the TPE engagement, we successfully completed the deployment of policies to both servers and VDI, 
                    improved device segregation within Entra, and corrected log forwarding from containers to the appropriate Sentinel Workspace. 
                    These improvements enable more granular and tailored security controls, specifically designed for different device types and 
                    locations, rather than a one-size-fits-all approach.
                </p>
                <p>
                    The scores provided in the attached document reflect the extent to which your controls align with Armor's best practices. 
                    Further details on the identified deltas can be found in the Delta Assessment.
                </p>
            </div>

            <div class="section">
                <h3>Recommended Next Steps</h3>
                <p>
                    In light of your expressed concerns and the evolving security and threat landscape, we strongly recommend that your 
                    organization deepen its investment in Microsoft Purview. This strategy not only enhances the protection of your internal 
                    data against exfiltration or malicious misuse but also positions your company to effectively adopt AI in the future.
                </p>
                <p>
                    Additionally, leveraging Entra ID's new suite of permissions and monitoring tools is advisable, given that shadow IT 
                    remains a significant issue, affecting 72% of the clients we currently serve.
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    # Write the final HTML report to file
    with open(output_file_path, 'w') as file:
        file.write(html_report)

# Example usage:
if __name__ == "__main__":
    generate_html_report('MDR Delta Assessment 2.0-Vault.xlsx', 'ExecutiveReport.html')
