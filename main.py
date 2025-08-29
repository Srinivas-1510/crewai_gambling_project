from crew import create_crew
from crew import unify_and_identify_products, to_csv  # Corrected import


def main():
    crew = create_crew()
    scrape_results = crew.kickoff()  # Output JSON scraped data

    # Identify and unify products
    unified_products = crew.tasks[1].agent.run(unify_and_identify_products(scrape_results))
    print("Unified Products:", unified_products)

    # Rearrange and generate CSV
    csv_data = crew.tasks[2].agent.run(to_csv(unified_products))
    print("Generated CSV:")
    print(csv_data)

    # Save to file
    with open('unified_gambling_products.csv', 'w') as f:
        f.write(csv_data)

    print("CSV saved as unified_gambling_products.csv")

if __name__ == "__main__":
    main()