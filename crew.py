from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapegraphScrapeTool  # Or SeleniumScraper for dynamic sites
import pandas as pd
import json

# Initialize the scraping tool (replace with API key/config if needed)
scrape_tool = ScrapegraphScrapeTool(api_key="sgai-490a3886-1044-481a-96a6-c3f48b709af4")

# Agent 1: Data Collector
scraper_agent = Agent(
    role="Data Collector",
    goal="Scrape products and prices from polymarket.com, prediction-market.com, and kalshi.com",
    backstory="Expert in web scraping and data extraction.",
    tools=[scrape_tool],
    verbose=True
)

# Define scraping task
scrape_task = Task(
    description="Scrape product data from gambling websites.",
    expected_output="JSON product data.",
    agent=scraper_agent,
)

def unify_and_identify_products(scraped_json):
    # Implement product matching logic here
    # Output JSON unified product list with confidence scores
    # Placeholder - customize matching logic
    unified = []
    # Example structure:
    # [{
    #   'product_name': 'Example Product',
    #   'prices': {'polymarket': 1.2, 'prediction-market': 1.3, 'kalshi': 1.1},
    #   'confidence': 0.95
    # }]
    return unified

# Agent 2: Product Identifier
product_identifier_agent = Agent(
    role="Product Identifier",
    goal="Identify and unify products across scraped sites.",
    backstory="Expert in product matching and data processing.",
    verbose=True
)

identify_task = Task(
    description="Match and unify products scraped from different sources.",
    expected_output="Unified product JSON with confidence scores.",
    agent=product_identifier_agent,
)

def to_csv(unified_products):
    # Convert unified product list to CSV format string
    df = pd.DataFrame(unified_products)
    return df.to_csv(index=False)

# Agent 3: Data Rearranger
data_rearranger_agent = Agent(
    role="Data Rearranger",
    goal="Format unified data and output CSV file.",
    backstory="Expert in data formatting and CSV generation.",
    verbose=True
)

rearrange_task = Task(
    description="Format product data into a CSV.",
    expected_output="CSV formatted product list.",
    agent=data_rearranger_agent,
)

# Create Crew and workflow process
def create_crew():
    crew = Crew(
        agents=[scraper_agent, product_identifier_agent, data_rearranger_agent],
        tasks=[scrape_task, identify_task, rearrange_task],
        process=Process.sequential,
        verbose=True
    )
    return crew
