import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

OUTPUT_FILE = "scripts/prompt_context.md"
DAYS = 7


def fetch_recent_commits(repo):
    since = (datetime.utcnow() - timedelta(days=DAYS)).isoformat() + "Z"
    url = f"https://api.github.com/repos/ethereum/{repo}/commits"
    params = {"since": since}
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    commits = response.json()
    return [
        f"{c['commit']['message'].splitlines()[0]} ({c['html_url']})"
        for c in commits
    ] or ["No recent commits"]


def extract_client_diversity():
    url = "https://clientdiversity.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        return ["Client diversity data unavailable."]

    rows = table.find_all("tr")
    data = []
    for row in rows[1:]:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if len(cols) >= 2:
            name, share = cols[0], cols[1]
            data.append(f"{name} {share}")
    return data if data else ["Client diversity data parsing failed."]


def main():
    eips = fetch_recent_commits("EIPs")
    ercs = fetch_recent_commits("ERCs")
    clients = extract_client_diversity()

    with open(OUTPUT_FILE, "w") as f:
        f.write("## Client Diversity (via clientdiversity.org)\n\n")
        for line in clients:
            f.write(f"- {line}\n")
        f.write("\n")

        f.write("## EIPs (Ethereum improvement proposals)\n\n")
        for line in eips:
            f.write(f"- {line}\n")
        f.write("\n")

        f.write("## ERCs (application layer)\n\n")
        for line in ercs:
            f.write(f"- {line}\n")
        f.write("\n")

if __name__ == "__main__":
    main()
