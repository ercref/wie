import requests
from datetime import datetime, timedelta
import os

# --- Configuration ---
OUTPUT_FILE = "scripts/prompt_context.md"
DAYS = 7
REQUEST_TIMEOUT = 15 # seconds
HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Before running your GitHub Action, update the values in this dictionary.

MANUAL_CLIENT_DIVERSITY_DATA = {
    "section_title": "Manually Updated Client Diversity Data",
    "source_checked": "clientdiversity.org (verified via execution-clients.com and Miga Labs)",
    "date_data_pulled": "2025-06-06",  # <-- UPDATE THIS WEEKLY (date you got the data)
    "data_as_of_date": "2025-06-06",  # <-- UPDATE THIS WEEKLY (date the data source refers to, if available)
    "key_staking_entity_share": {
        "entity_name": "Lido",
        "share_percentage": "25.84%",      # <-- UPDATE THIS WEEKLY
        "source_link": "https://dune.com/hildobby/eth2-staking"  # <-- UPDATE THIS LINK IF NEEDED
    },
    "consensus_clients_note": "Sourced from Miga Labs via clientdiversity.org",
    "consensus_clients": [
        "Lighthouse: 42.71%",
        "Prysm: 30.91%",
        "Teku: 13.86%",
        "Nimbus: 8.74%",
    ],
    "execution_clients_note": "Sourced from execution-clients.com",
    "execution_clients": [
        "Geth: 41%",
        "Nethermind: 38%",
        "Besu: 16%",
        "Erigon: 3%",
    ],
}

def fetch_recent_commits(repo_path_segment):
    """Fetches recent non-merge commits from a specific ethereum GitHub repo path segment."""
    since_date = (datetime.utcnow() - timedelta(days=DAYS)).isoformat() + "Z"



    url = f"https://api.github.com/repos/ethereum/{repo_path_segment}/commits"
    if repo_path_segment.upper() == "ERCS":
        url = "https://api.github.com/repos/ethereum/EIPs/commits"

    params = {"since": since_date}
    headers = {"Accept": "application/vnd.github.v3+json", **HTTP_HEADERS}
    commit_info_list = []
    try:
        response = requests.get(url, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        commits_data = response.json()
        for commit_entry in commits_data:
            commit_message = commit_entry['commit']['message']

            if not commit_message.lower().startswith('merge pull request') and \
               not commit_message.lower().startswith('merge branch'):
                first_line_of_message = commit_message.splitlines()[0]

                if len(first_line_of_message) > 120:
                    first_line_of_message = first_line_of_message[:117] + "..."
                commit_info_list.append(f"{first_line_of_message} ({commit_entry['html_url']})")
        if not commit_info_list:
            return [f"No recent non-merge commits found for {repo_path_segment} in the last {DAYS} days."]
    except requests.exceptions.RequestException as e:
        return [f"Error fetching commits for {repo_path_segment}: {e}"]
    except Exception as e:
        return [f"An unexpected error occurred fetching commits for {repo_path_segment}: {e}"]
    return commit_info_list

def main():
    """Main function to build the context file."""
    print("Starting context build...")

    eips_section_commits = fetch_recent_commits("EIPs")
    ercs_section_commits = fetch_recent_commits("ERCs")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Write the manually updated data

        f.write(f"## {MANUAL_CLIENT_DIVERSITY_DATA['section_title']} (Week of {MANUAL_CLIENT_DIVERSITY_DATA['date_data_pulled']})\n\n")
        f.write(f"**Source Checked:** {MANUAL_CLIENT_DIVERSITY_DATA['source_checked']}\n")
        f.write(f"**Date Data Pulled:** {MANUAL_CLIENT_DIVERSITY_DATA['date_data_pulled']}\n\n")

        # Write Lido data
        staking_data = MANUAL_CLIENT_DIVERSITY_DATA.get("key_staking_entity_share")
        if staking_data:
            f.write(f"### Key Staking Entity Share\n\n")
            f.write(f"* {staking_data['entity_name']} Share: {staking_data['share_percentage']}\n")
            f.write(f"* {staking_data['entity_name']} Dune Link: {staking_data['source_link']}\n\n")
            
        # Write Consensus Client data
        f.write(f"### Consensus Layer Client Diversity\n\n")
        for client in MANUAL_CLIENT_DIVERSITY_DATA['consensus_clients']:
            f.write(f"* {client}\n")
        f.write(f"_*Note: {MANUAL_CLIENT_DIVERSITY_DATA['consensus_clients_note']}*_\n\n")

        # Write Execution Client data
        f.write(f"### Execution Layer Client Diversity\n\n")
        for client in MANUAL_CLIENT_DIVERSITY_DATA['execution_clients']:
            f.write(f"* {client}\n")
        f.write(f"_*Note: {MANUAL_CLIENT_DIVERSITY_DATA['execution_clients_note']}*_\n\n")

        # Write dynamically fetched data
        f.write("## Recent EIP Commits (from GitHub `ethereum/EIPs`)\n\n")
        for line_item in eips_section_commits:
            f.write(f"- {line_item}\n")
        f.write("\n")


        f.write("## Recent ERC-Related Commits (from GitHub `ethereum/EIPs`)\n\n")
        for line_item in ercs_section_commits:
            f.write(f"- {line_item}\n")
        f.write("\n")

    print(f"Context file generated with manual client diversity data: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
