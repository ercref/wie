**Objective:** Create a comprehensive and engaging newsletter summarizing key developments, news, and discussions within the Ethereum ecosystem, structured **exactly like a typical "Week in Ethereum News" issue**.

**CRITICAL OVERARCHING RULE: This newsletter MUST ONLY contain information, news, and updates that have occurred or were published within the strict 7-day period concluding on the date of execution (e.g., if executed on May 25, 2025, it covers Monday, May 19, 2025, to Sunday, May 25, 2025, inclusive). Furthermore, if any defined section or category below does not have any relevant updates from this 7-day period, that entire section or category MUST be omitted from the final newsletter. Do not include sections with no new information.**

The newsletter must cover **only the 7-day period concluding on the date of execution**. The AI must emphasize clarity, **absolute factual accuracy, verifiable timeliness (all information strictly from the past 7 days unless intrinsically referencing future events based on current announcements)**, relevance, and use its judgment to find and prioritize the most impactful information within this exact structure, ensuring all items are bullet-pointed under their respective headings. Your output must emulate the dense linking style of "Week in Ethereum News," where nearly every reported item has an embedded link to its source. **This newsletter is for a high-stakes audience; errors or outdated information are unacceptable.**

**Newsletter Structure and Content Guidelines (Emulating "Week in Ethereum News"):**
## **News Sections:** *(The following numbered sections are part of the overall newsletter structure. They should only be included if relevant news from the past 7 days exists for them. Each item under these headings must be a bullet point.)*

**6. Layer 2**

  * **Source of Information:** You must actively browse the web for this information. Primary sources are official project blogs (e.g., Arbitrum, Optimism, Base, Starknet), developer posts on X (formerly Twitter), and reputable crypto news outlets covering L2s.
  * **Content:** Based on developments from the past 7 days, report on significant technical and ecosystem developments related to Layer 2s. Your goal is to report on specific technical milestones, new features, and notable project launches, not just TVL or activity statistics. Each item should be a bullet point.
  * **Focus:**
      * Rollup Milestones & Proving Systems: Report on any L2 achieving a new "stage" of decentralization (e.g., Stage 1 or 2 rollup status) or updates to their proving systems (e.g., launching new fault proofs or validity provers).
      * New Features & Developer Tools: Look for new user or developer features that improve the L2's functionality, such as forced transaction inclusion mechanisms, new developer tools, or economic model changes.
      * Ecosystem Growth: Announce the launch of significant new L2 chains or public testnets, noting their underlying technology (e.g., OP Stack, ZK Stack, new VMs).
      * Research & Innovative Designs: Summarize any new or significant design proposals for rollups or L2 architecture coming from researchers or developers.
  * **Keywords for Search (Starting Points):** "Layer 2 Ethereum updates," "L2 fault proofs," "L2 rollup stages," "new Layer 2 launch," "L2 new virtual machine," "blob usage," "L2 new features."

**7. Stuff for Developers**

  * **Source of Information:** You must actively browse the web. Your primary sources are official project GitHub repositories (especially release pages), developer blogs, and posts on X (formerly Twitter) from prominent dev tool teams (Foundry, Hardhat, OpenZeppelin, etc.) and well-known developers.
  * **Content:** Based on developments from the past 7 days, report on specific updates to developer tools, new open-source libraries, and practical resources for builders. Your goal is to find a diverse set of concrete updates for developers. Do NOT report on general EIP discussions or their status changes in this section.
  * **Focus:**
      * **Updates to Developer Frameworks & Tooling:** Look for new versions or significant feature releases for any popular smart contract development frameworks, testing suites, or general tooling. For each tool with an update, create a main bullet point with the tool's name (e.g., * Foundry:) and use nested bullet points for specific updates.
      * **New Libraries, Utilities & Smart Contracts:** Report on the release of new open-source libraries, helpful utilities, or interesting smart contract designs that developers can use (e.g., new Solidity/Vyper libraries, innovative contract architectures).
      * **Guides, Tutorials & Educational Content:** Find and summarize new, practical guides, in-depth explainers, or educational courses that would be valuable for Ethereum developers.
      * **Contests & Capture The Flags (CTFs):** Announce new developer-focused contests or CTFs, or report on the winners and interesting solutions from recently concluded ones.
  * **Keywords for Search (Starting Points):** "Ethereum developer tools," "EVM developer framework," "Solidity tooling," "smart contract library update," "Solidity guide," "Vyper tutorial," "Solidity CTF."

**8. Security**

  * **Content:** Report on security incidents, vulnerabilities, audits, and best practices relevant to the Ethereum ecosystem, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * Details of any significant DeFi exploits or hacks (protocol, amount lost, nature of vulnerability, post-mortems).
      * Newly disclosed vulnerabilities in smart contracts, clients, wallets, or L2s.
      * Important security audit releases for major protocols.
      * New tools, standards, or initiatives aimed at improving ecosystem security (e.g., ERC-7265).
      * Discussions on formal verification, bug bounties.
  * **Keywords for Search (Starting Points):** "DeFi hack," "Ethereum security vulnerability," "smart contract audit," "crypto exploit report," "Ethereum bug bounty."

**9. Ecosystem**

  * **Content:** Broader news from the Ethereum ecosystem, including DAOs, NFTs, public goods, and community initiatives, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * Major project milestones or product launches not covered in more specific sections.
      * Significant DAO governance proposals, votes, or treasury actions.
      * Updates on public goods funding initiatives (e.g., Gitcoin Grants rounds, Protocol Guild, ESP grants).
      * Noteworthy NFT collections, market trends, or infrastructure developments (unless covered in "Notable at app layer").
      * Community-led events, educational initiatives, or important discussions.
  * **Keywords for Search (Starting Points):** "Ethereum project launch," "DAO news," "Gitcoin grants," "NFT news Ethereum," "Ethereum community."

**10. Notable at app layer**

  * **Content:** Highlight interesting new decentralized applications (dapps), user-facing innovations, or significant updates to existing applications on Ethereum or L2s, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * Innovative or unique dapps gaining traction.
      * Significant feature releases or milestones for established applications.
      * Trends in application development (e.g., SocialFi, DePIN, new gaming models).
  * **Keywords for Search (Starting Points):** "New Ethereum dApp," "[dApp Name] update," "DeFi project launch," "NFT marketplace news."

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
  * **Scope:** Your output must ONLY contain the sections listed in this prompt (Layer 2, Developer Stuff, Security, Ecosystem, Notable at app layer). Do not generate content for any other sections.
  * **Headings:** All section headings MUST be formatted as Markdown H2 headings (e.g., `## Layer 2`)  without any leading spaces or indentation. Do NOT use numbers in the headings.
  * **Content:** Every item you write under a heading MUST start on a new line. All list items must use bullet points.
  * **Header:** Do NOT include a main "Week in Ethereum News" header or a date. Your output should begin directly with the first section heading.
