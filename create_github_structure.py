import os

# Define your top-level folders and subfolders
structure = {
    "onchain-analytics": [
        "cosmos-staking-analytics",
        "bsc-whale-tracking",
        "polygon-defi-liquidity",
        "arbitrum-token-flow"
    ],
    "offchain-analytics": [
        "offchain-crypto-exchange-metrics",
        "stablecoin-usage-by-region",
        "customer-segmentation-exchange"
    ],
    "blockchain-data-engineering": [
        "rpc-node-monitoring",
        "blockchain-data-pipelines",
        "thegraph-data-exploration",
        "dune-data-to-snowflake"
    ],
    "exploratory-analysis-and-visuals": [
        "stablecoin-price-volatility",
        "wallet-behavior-viz",
        "staking-vs-inflation-trends"
    ],
    "learning-and-templates": [
        "dbt-template-project",
        "graph-graphql-template",
        "superset-dashboard-template",
        "rpc-request-snippets"
    ]
}

# Create folders
for main_folder, subfolders in structure.items():
    os.makedirs(main_folder, exist_ok=True)
    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        
        # Create an empty README.md in each subfolder
        readme_path = os.path.join(subfolder_path, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# {subfolder}\n\nProject description coming soon!\n")

print("✅ Folder structure created successfully!")
