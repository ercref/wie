import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

OUTPUT_FILE = "scripts/prompt_context.md"
DAYS = 7

# Manually update

MANUAL_CLIENT_DIVERSITY_DATA = {
    "section_title": "Manually Updated Client Diversity Data", # This title should match what the main AI prompt expects
    "source_checked": "clientdiversity.org (verified via execution-clients.com and Miga Labs)",
    "date_data_pulled": "2025-06-01",  # <-- UPDATE THIS WEEKLY (date you got the data)
    "data_as_of_date": "2025-05-30",  # <-- UPDATE THIS WEEKLY (date the data source refers to, if available)
    "consensus_clients_note": "Sourced from Miga Labs via clientdiversity.org",
    "consensus_clients": [
        "Lighthouse: 42.71%", 
        "Prysm: 30.91%",
        "Teku: 13.86%",
        "Nimbus: 8.74%",
        "Lodestar: 2.67%",
        "Grandine: 1.04%",
        "Other/Unknown: 0.07%"
    ],
    "execution_clients_note": "Sourced from execution-clients.com",
    "execution_clients": [
        "Geth: 41%",  
        "Nethermind: 38%",
        "Besu: 16%",
        "Erigon: 3%",
        "Reth: 2%",
        "Other/Unknown: 0%"
    ],
    "key_observations": [
        # "Optional: Add any key observations here.",
        # "e.g., Slight increase in Reth adoption noted this week."
    ]
}

def fetch_recent_commits(repo_path_segment): # e.g., "EIPs"
    """Fetches recent non-merge commits from a specific ethereum GitHub repo path segment."""
    since_date = (datetime.utcnow() - timedelta(days=DAYS)).isoformat() + "Z"
    # ERCs are part of the EIPs repository.
    # The main prompt has specific instructions for how the AI should find EIPs/ERCs by monitoring the repo.
    # This function just provides recent commit messages as supplementary context.
    url = f"https://api.github.com/repos/ethereum/{repo_path_segment}/commits"
    if repo_path_segment.upper() == "ERCS": # Actually point to EIPs repo for ERCs
        url = "https://api.github.com/repos/ethereum/EIPs/commits"

    params = {"since": since_date}
    headers = {"Accept": "application/vnd.github.v3+json"}
    commit_info_list = []
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        commits_data = response.json()
        for commit_entry in commits_data:
            commit_message = commit_entry['commit']['message']
            # Filter out common merge commit messages
            if not commit_message.lower().startswith('merge pull request') and \
               not commit_message.lower().startswith('merge branch'):
                first_line_of_message = commit_message.splitlines()[0]
                # Truncate if too long
                if len(first_line_of_message) > 120:
                    first_line_of_message = first_line_of_message[:117] + "..."
                commit_info_list.append(f"{first_line_of_message} ({commit_entry['html_url']})")
        if not commit_info_list:
            return [f"No recent non-merge commits found for {repo_path_segment} in the last {DAYS} days."]
    except requests.exceptions.RequestException as e:
        return [f"Error fetching commits for {repo_path_segment}: {e}"]
    except Exception as e: # Catch other potential errors like JSON decoding
        return [f"An unexpected error occurred fetching commits for {repo_path_segment}: {e}"]
    return commit_info_list

def format_manual_client_diversity_for_context():
    """Formats the manually defined client diversity data for the context file."""
    data_dict = MANUAL_CLIENT_DIVERSITY_DATA
    lines = []
    # The main prompt already expects a specific heading for this section.
    # This script will write the content under that heading.
    lines.append(f"**Source Checked:** {data_dict['source_checked']}")
    lines.append(f"**Date Data Pulled:** {data_dict['date_data_pulled']}")
    if data_dict.get('data_as_of_date'):
        lines.append(f"**Data \"As Of\" Date (if available from source):** {data_dict['data_as_of_date']}")
    
    lines.append("\n**Consensus Layer Client Diversity:**")
    for client_stat in data_dict['consensus_clients']:
        lines.append(f"* {client_stat}")
    if data_dict.get('consensus_clients_note'):
        lines.append(f"* *Note: {data_dict['consensus_clients_note']}*")
    
    lines.append("\n**Execution Layer Client Diversity:**")
    for client_stat in data_dict['execution_clients']:
        lines.append(f"* {client_stat}")
    if data_dict.get('execution_clients_note'):
        lines.append(f"* *Note: {data_dict['execution_clients_note']}*")

    if data_dict.get('key_observations') and data_dict['key_observations']:
        lines.append("\n**Key Observations/Changes this Week:**")
        for obs in data_dict['key_observations']:
            lines.append(f"* {obs}")
    return lines

def main():
    # Fetch EIPs and ERCs commit messages (ERCs are within EIPs repo)
    # Note: The main AI prompt has detailed instructions for sourcing EIP/ERC info
    # directly from GitHub PRs and status changes. These commit lists are supplementary.
    eips_section_commits = fetch_recent_commits("EIPs")
    # The ERCs section will also list commits from ethereum/EIPs.
    # The main AI prompt should handle distinguishing actual ERC updates.
    ercs_section_commits = fetch_recent_commits("ERCs") # Still fetches from EIPs, contextually for "ERC-related" commits

    manual_client_diversity_output_lines = format_manual_client_diversity_for_context()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # This heading should match EXACTLY what your main AI prompt (Section 7)
        # expects to find in the {{context}}
        f.write(f"## {MANUAL_CLIENT_DIVERSITY_DATA['section_title']} (Week of {MANUAL_CLIENT_DIVERSITY_DATA['date_data_pulled']})\n\n")
        for line_item in manual_client_diversity_output_lines:
            f.write(f"{line_item}\n")
        f.write("\n\n") # Add some space before the next section

        f.write("## Recent EIP Commits (from GitHub `ethereum/EIPs`)\n\n")
        for line_item in eips_section_commits:
            f.write(f"- {line_item}\n")
        f.write("\n")

        # Clarifying that ERCs are also from the EIPs repo.
        f.write("## Recent ERC-Related Commits (from GitHub `ethereum/EIPs`)\n\n")
        for line_item in ercs_section_commits:
            f.write(f"- {line_item}\n")
        f.write("\n")
    
    print(f"Context file generated with manual client diversity data: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
