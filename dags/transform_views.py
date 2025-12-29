import pandas as pd

def transform_company_views(df):
    
    if df is None:
        raise ValueError("Input DataFrame is None. Extract step failed.")
    
    """Define companies of interest"""
    companies = ["Apple", "Amazon", "Facebook", "Google", "Microsoft", "Tesla", "IBM", "Oracle"]
    
    """Filter rows where page_title matches one of the companies of interest"""
    companies_views = df[df["page_title"].isin(companies)][["page_title", "views"]]
     
    """Summarize views by company of interest"""
    summary = companies_views.groupby("page_title")["views"].sum().reset_index()
    
    return summary
    

