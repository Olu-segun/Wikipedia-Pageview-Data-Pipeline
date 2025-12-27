import pandas as pd
from extract_views import extract_company_views
import os
def transform_company_views():
    df["page_title"] = df["page_title"].str.replace("_", " ")
                
    """Filter company of interest from the dataframe"""
        companies = ["Apple", "Amazon", "Facebook", "Google", 
                             "Microsoft", "Tesla", "IBM", "Oracle"]
                
                """Filter company of interest from the dataframe"""
                companies_views = df[df["page_title"].isin(companies)][["page_title", "views"]]

                Summary = companies_views.groupby("page_title")["views"].sum().reset_index()
