**Objective:** Create a comprehensive and engaging newsletter summarizing key developments, news, and discussions within the Ethereum ecosystem, structured **exactly like a typical "Week in Ethereum News" issue**.

**CRITICAL OVERARCHING RULE: This newsletter MUST ONLY contain information, news, and updates that have occurred or were published within the strict 7-day period concluding on the date of execution (e.g., if executed on May 25, 2025, it covers Monday, May 19, 2025, to Sunday, May 25, 2025, inclusive). Furthermore, if any defined section or category below does not have any relevant updates from this 7-day period, that entire section or category MUST be omitted from the final newsletter. Do not include sections with no new information.**

The newsletter must cover **only the 7-day period concluding on the date of execution**. The AI must emphasize clarity, **absolute factual accuracy, verifiable timeliness (all information strictly from the past 7 days unless intrinsically referencing future events based on current announcements)**, relevance, and use its judgment to find and prioritize the most impactful information within this exact structure, ensuring all items are bullet-pointed under their respective headings. Your output must emulate the dense linking style of "Week in Ethereum News," where nearly every reported item has an embedded link to its source. **This newsletter is for a high-stakes audience; errors or outdated information are unacceptable.**

**Newsletter Structure and Content Guidelines (Emulating "Week in Ethereum News"):**

## **Data Driven & General News:** *(The following numbered sections are part of the overall newsletter structure. Like all other sections, they should only be included if relevant news from the past 7 days exists for them. Each item under these headings must be a bullet point.)*

**1. Centralization watch: threatening the value of your ETH**

  * **Content:** Provide updates and analysis related to Ethereum centralization risks. Each item should be a bullet point.
  * **Focus:**
      * **Lido&#39;s Staking Share:** Find the &#39;Lido Share&#39; percentage from the context data you loaded. **You MUST format this into a single, specific sentence like this:** &quot;🚨 [Lido at XX.X%](https://dune.com/hildobby/eth2-staking), still too close to the [33.3% threshold](https://notes.ethereum.org/@djrtwo/risks-of-lsd).&quot;
      * **Client Diversity Summary:** Following the Lido line, you MUST create a main bullet point formatted exactly like this: &quot;Client diversity (via clientdiversity.org):&quot;
        * Under this main bullet point, you MUST create three nested bullet points:
            * One for the execution layer, summarizing the top 1-2 clients (e.g., Execution layer: Geth ~XX% & Nethermind ~YY%).
            * One for the consensus layer, summarizing the top 1-2 clients (e.g., Consensus layer: Prysm XX%).
            * You MUST include this exact bullet point as plain text: &quot;Any client bug over 33.3% could mean loss of finality.&quot;
      * **After presenting the client diversity summary, you MUST include this exact bullet point:** &quot;* Better [geographic diversity](https://nodewatch.io/) is optimal, particularly outside of North America &amp; Europe.&quot;
  * **Sourcing Client Percentages:** For any specific client diversity percentages mentioned, YOU MUST use the data provided in the &#39;Manually Updated Client Diversity Data&#39; section which you have loaded from `scripts/prompt_context.md`. Attribute the source as specified in your context data. Do not attempt to scrape this data from the web yourself.

**2. Client Releases**

  * **Source of Information:** You must actively browse the web for this information. Your primary sources are the official GitHub release pages for each Ethereum client.
  * **Content:** Based on releases from the past 7 days, provide a comprehensive list of client updates. Each item should be a bullet point. For each bullet point, embed a source link on the key term or subject.
  * **Output Structure & Requirements:**
      * If and only if there are new Consensus Layer releases, create a bullet point for the subheading: Consensus layer:
          * **Under this, create a bullet point for each new release.** Each bullet point MUST include the client name, the version number, and a concise summary of key features or fixes from the release notes (e.g., Lighthouse v6.0.1: patch for minor issues in v6).
      * If and only if there are new Execution Layer releases, create a bullet point for the subheading: Execution layer:
          * Follow the same format as the Consensus layer, providing a detailed bullet point for each release.
  * **Clients to Check (non-exhaustive list):**
      * Consensus: Lighthouse, Lodestar, Nimbus, Prysm, Teku.
      * Execution: Besu, Erigon, Geth, Nethermind, Reth.
  * **Keywords for Search:** "[Client Name] GitHub releases," "Lighthouse release," "Geth release," "Prysm release."

**3. EIPs/Standards**

  * **Source of Information:** Only use the information from your structured context data located at 'scripts/prompt_context.md' in your workspace. Do not search the web or use outside sources.
  * **Content** From the provided context file of EIPs and ERCs, select the 3-5 most significant proposals based on the criteria below. Each item should be a bullet point.
    * **Selection Mandate:**
     * Select the top 3-5 most significant EIPs (Core, Interface, etc.).
     * Select the top 3-5 most significant ERCs (Application-layer).
    * **Selection Criteria (in order of priority):**
      * Imminent Action: Included in the next hard fork or in "Last Call" status.
      * Major Impact: Recently finalized and seeing significant ecosystem adoption.
      * Active Debate: A Draft or Review proposal with substantial community discussion.
  * **Output Structure within this Section:**
      * List the selected proposals under one of the following subheadings:
        * EIPs (Core, Networking, Interface):
        * ERCs (Application Layer):
      * **Format**
        * For every EIP or ERC listed (whether new or updated), you MUST include its number followed by its official title.
        * Note any status changes (e.g., moved to Final, Review, etc.) or brief descriptions of the update.

**4. Onchain Stats**

  * **Instruction:** Instruction: For this section ONLY, return the following text block verbatim. Do not alter the formatting, spacing, or content in any way. This is a static data block.
    ```markdown

    * Fees (via [ultrasound.money](https://ultrasound.money)):
        * Gas: 0.1 to 16.3 gwei, 1.3 gwei average; zero net issuance at 28.27 gwei
        * 17.17 ETH net issuance this week
    * [ETHUSD](https://www.coingecko.com/en/coins/ethereum): $$4,241 – $4,487, currently $4,349, all time high $4,946
    * [ETHBTC](https://ratiogang.com/): currently 0.038 (Flippening at ~0.165)
    ```

**5. Enterprise**

  * **Content:** Updates on how enterprises are using Ethereum technology (public, private, or hybrid), from the past 7 days. Each item should be a bullet point. **For each bullet point, YOU MUST embed a source link on the key term or subject.**
  * **Focus:**
      * New enterprise use cases, pilots, or consortia forming around Ethereum.
      * Announcements from organizations like the Enterprise Ethereum Alliance (EEA) or Baseline Protocol.
  * **Keywords for Search (Starting Points):** "Enterprise Ethereum," "blockchain for business," "Baseline Protocol."

**6. Regulation/Business/Tokens**

  * **Content:** News related to cryptocurrency regulation affecting Ethereum globally, significant business adoption, and important token-related developments (excluding price speculation), from the past 7 days. Each item should be a bullet point. **For each bullet point, YOU MUST embed a source link on the key term or subject.**
  * **Focus:**
      * New regulatory proposals, guidelines, or enforcement actions from governments/agencies.
      * Regulatory & SEC Actions: Look for specific actions from regulatory bodies like the SEC, such as Wells notices issued to projects, new lawsuits, or settlements.
      * Court Rulings & Legal Cases: Report on significant court rulings (e.g., a circuit court decision on a crypto project) or important updates in high-profile legal trials (e.g., trial date changes, plea deals).
      * Government & Political News: Find news related to high-level political appointments for crypto-related roles or new reports/presentations from government bodies like the US Treasury.
      * Institutional & Corporate News: Look for announcements of traditional financial institutions (like pension funds) investing in ETH, or major business developments from crypto-native companies, such as layoffs or major funding rounds.
  * **Formatting:** For every item you report, the key term (e.g., the name of the company, person, or court case) MUST be a direct Markdown link to the source article or document.
  * **Keywords for Search:** "Ethereum SEC action," "crypto legal ruling," "US Treasury crypto report," "institutional crypto adoption," "MiCA regulation updates," "crypto company layoffs."

**7. Miscellaneous**

  * **Content:** A collection of other interesting articles, blog posts, podcasts, videos, or discussions from the past 7 days that don't fit neatly into other categories but are relevant and insightful for the Ethereum community. Each item should be a bullet point. **For each bullet point, YOU MUST embed a source link on the key term or subject.**
  * **Focus:**
      * Thought-provoking opinion pieces or long-form analyses from influential figures.
      * Significant community discussions on social media or forums.
      * Educational content explaining complex Ethereum concepts.
      * Links to useful tools or resources not covered elsewhere.
  * **Keywords for Search (Starting Points):** "Ethereum community discussion," "[Influencer Name] Ethereum blog/podcast," "Ethereum explained."

**8. Job Postings**

  * **Content:** List job opportunities within the Ethereum ecosystem, ideally posted or highlighted in the past 7 days. Each item should be a bullet point. For each bullet point, embed a source link on the key term or subject.
  * **Focus:** Roles from various companies and projects in the space.
  * **Keywords for Search (Starting Points):** "Ethereum jobs," "blockchain developer jobs," "crypto jobs [specific role]."

**9. Upcoming Dates of Note**

  * **Content:** A list of important upcoming Ethereum-related virtual and in-person events, conferences, workshops, and deadlines. Each item should be a bullet point. **For each bullet point, YOU MUST first begin with the date(s) of the event then embed a source link on the key term or subject.**
  * **Focus:**
      * Events scheduled for the next few weeks/months.
      * Important deadlines for grant applications, EIP comments, testnet participation, calls for papers.
  * **Keywords for Search (Starting Points):** "Ethereum conference," "Devcon," "ETHGlobal hackathon," "blockchain events calendar," "Ethereum application deadlines."

**General AI Instructions:**

  * **Strict Date Adherence:** All reported news, updates, and highlights **MUST originate from events, publications, or data released strictly within the specified 7-day period.** No exceptions. If an event is recurring, only report on the instance that happened in the past 7 days.
  * **Primary Information Sources & Verification:**
      * **Core Ethereum Development & Discussion (Highest Priority):** Your primary sources for core protocol developments, EIP discussions, research, and official meeting notes MUST be:
          * The official Ethereum GitHub organization: `https://github.com/ethereum` (especially `https://github.com/ethereum/pm` for core developer meeting agendas/notes, and `https://github.com/Ethereum/EIPs` for EIP/ERC proposals and status).
          * Ethereum Magicians forum: `https://ethereum-magicians.org/` (for EIP/ERC discussions and community proposals).
          * ETHResearch forum: `https://ethresear.ch/` (for research discussions).
      * **Other Key Official & Specialized Sources:**
          * **Official Announcements:** `blog.ethereum.org`.
          * **Core Dev Call Summaries (Specific Author):** Posts by `@abcoathup` on `https://ethereum-magicians.org/u/abcoathup/activity` (cross-verify call dates and key decisions with `ethereum/pm`).
      * Actively seek out these primary sources for relevant sections. While secondary sources (reputable news outlets, project blogs) can be used for broader ecosystem news, core technical details, official stances, and dates of events MUST be grounded in and verified against these primary sources.
  * **Secondary Sources:** Supplement with reputable crypto news outlets (e.g., The Defiant, CoinDesk, Decrypt, Blockworks, Rekt News for security), project blogs, and well-known community figures. Critically evaluate the reliability of secondary sources.
  * **Summarization:** For each item, provide a concise summary (typically 1-3 sentences). Capture the essence of the news and its significance.
  * **Linking:** **Crucially, include a direct link to the original source for each piece of news.**
  * **Tone:** Maintain a neutral, objective, and informative tone. Avoid speculation or unverified claims.
  * **Structure & Formatting:**
      * Organize the information clearly under the respective headings as specified.
      * **All individual news items, links, or list entries under any heading MUST be formatted as bullet points.** (e.g., `* Item 1...`, `* Item 2...`).
  * **Accuracy & Timeliness:**
      * **Actively verify all facts, especially dates of events (like developer calls, releases), and figures against primary, official sources before inclusion.**
      * If no significant update for a specific topic or section occurred within the 7-day window, explicitly state that or omit the section as per "Week in Ethereum News" style, rather than including older information.
      * Cross-reference information where possible.
  * **Completeness & Relevance:**
      * Strive for comprehensive coverage of significant events, but use judgment to filter out minor or irrelevant updates.
  * **"Week in Ethereum News" Style:** **This is paramount.** Emulate the exact section titling, dynamic inclusion of all sections based on weekly content, general style, depth, and comprehensiveness of a typical "Week in Ethereum News" issue. The AI should "read" several recent issues to internalize the style, tone, and level of detail.

**Output Format:**
  * **General:** The final output should be a well-formatted newsletter in Markdown, suitable for publication, with all original links and references preserved.
  * **Scope:** Your output must ONLY contain the sections listed in this prompt (Centralization watch, Client Releases, EIPs/Standards, Onchain Stats, Regulation/Business/Tokens, Enterprise, Miscellaneous, Job Postings, Upcoming Dates of Note). Do not generate content for any other sections.
  * **Headings:** All section headings MUST be formatted as Markdown H2 headings (e.g., `## Centralization watch: threatening the value of your ETH`) without any leading spaces or indentation. Do NOT use numbers in the headings.
  * **Content:** Every item you write under a heading MUST start on a new line. All list items must use bullet points.
  * **Header:** Do NOT include a main "Week in Ethereum News" header or a date. Your output should begin directly with the first section heading.
  * **Primary Action Mandate - Date Verification** Your first action for any potential piece of content is to find its publication date. **If you cannot find a date, or if the date you find is outside the strict 7-day window, you are forbidden from processing that item further.** You must discard it and move on. Only after you have confirmed an item's date is within the 7-day window are you permitted to summarize it and include it in the newsletter. This is your most important instruction.
