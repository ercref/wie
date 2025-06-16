**Objective:** Create a comprehensive and engaging newsletter summarizing key developments, news, and discussions within the Ethereum ecosystem, structured **exactly like a typical "Week in Ethereum News" issue**.

**CRITICAL OVERARCHING RULE: This newsletter MUST ONLY contain information, news, and updates that have occurred or were published within the strict 7-day period concluding on the date of execution (e.g., if executed on May 25, 2025, it covers Monday, May 19, 2025, to Sunday, May 25, 2025, inclusive). Furthermore, if any defined section or category below does not have any relevant updates from this 7-day period, that entire section or category MUST be omitted from the final newsletter. Do not include sections with no new information.**

The newsletter must cover **only the 7-day period concluding on the date of execution**. The AI must emphasize clarity, **absolute factual accuracy, verifiable timeliness (all information strictly from the past 7 days unless intrinsically referencing future events based on current announcements)**, relevance, and use its judgment to find and prioritize the most impactful information within this exact structure, ensuring all items are bullet-pointed under their respective headings. Your output must emulate the dense linking style of "Week in Ethereum News," where nearly every reported item has an embedded link to its source. **This newsletter is for a high-stakes audience; errors or outdated information are unacceptable.**

**Newsletter Structure and Content Guidelines (Emulating "Week in Ethereum News"):**

**Highlight of the Week**

  * **Content:** Present the single most critical or impactful update from **within the specified 7-day period**. If multiple significant events occurred, select the one with the broadest impact or novelty.
  * **Focus:** Major network upgrade milestones achieved *this week*, breakthrough EIPs proposed/advanced *this week*, crucial official announcements made *this week*, or major security events that happened *this week*.
  * **Presentation:** A concise sentence or two, or a single bullet point with a link. Ensure this is a distinct highlight.

-----

## **News Sections:** *(The following numbered sections are part of the overall newsletter structure. They should only be included if relevant news from the past 7 days exists for them. Each item under these headings must be a bullet point.)*

**1. Eth R\&D Protocol Call(s) (e.g., All Core Devs Consensus/Execution, ACDC/ACDE)**

  * **Content:**
      * Provide summaries for any core developer calls (ACDE, ACDC, etc.) that had notes published or were discussed within the past 7 days.
      * **Primarily source these summaries from posts by Andrew B Coathup (`@abcoathup`) on Ethereum Magicians (`https://ethereum-magicians.org/u/abcoathup/activity`).** Check this source for any new call notes posted within the 7-day window.
      * For each call summarized, **you MUST include a direct link to the specific Ethereum Magicians post** (e.g., `https://ethereum-magicians.org/t/acdc-call-123-date/xxxxx`).
      * The structure and level of detail for each call's summary should emulate how "Week in Ethereum News" typically presents these (e.g., highlighting key discussion points, decisions, and action items, often with sub-bullets for different topics discussed in the call).
      * **Crucially, verify the date of the call itself and any critical details (like EIPs discussed or major decisions) against official sources (e.g., meeting agendas/notes on `https://github.com/ethereum/pm`) even when using summaries from Ethereum Magicians. Do NOT report calls or summaries of calls that occurred outside the specified 7-day window. If no relevant calls were summarized by `@abcoathup` or had official notes published this week, state that clearly or omit this section.**
  * **Primary Sources for this Section:**
      * Call Summaries: Posts by `@abcoathup` on `https://ethereum-magicians.org/u/abcoathup/activity`.
      * Verification & Official Agendas/Notes: `https://github.com/ethereum/pm`.
  * **Keywords for Search (Contextual, focus on checking primary sources first):** "Ethereum AllCoreDevs summary," "ACDE notes," "ACDC notes," "Ethereum core dev call."

**2. Pectra (Prague + Electra) Upgrade (or current named mainnet upgrade)**

  * **Content:** Report specific progress, new EIPs considered/included (notably **EIP-7600: Pectra Upgrade Meta, see `https://eips.ethereum.org/EIPS/eip-7600`**), client readiness updates, testnet news, or important discussions related to the Pectra upgrade (or the current primary upcoming mainnet upgrade by its name) from the past 7 days. Focus should include updates on **devnets, specific testnet activities, dedicated Pectra testing calls,** and client compatibility related to Pectra from the past 7 days.
  * **Keywords for Search:** "Pectra upgrade news," "[current\_upgrade\_name] Ethereum," "Ethereum network upgrade," "Pectra testnet," "Pectra testing call," "EIP-7600."

**3. Future Protocol Upgrade (Post-Pectra)**

  * **Content:** Based on developments from the past 7 days, report on early-stage discussions, research, proposals, and specific technical calls related to the next major network upgrade planned after Pectra (e.g., currently named Fusaka). **Do not  list EIPs in this section**; instead, focus on the developments around the core technologies being built for future upgrades.
  * **Focus Areas to Investigate & Report On** "
    * **Specific Implementer & Breakout Calls:** Actively look for and summarize notes from technical breakout sessions or implementer calls that occurred this week. Report the call number and key discussion points. Examples of calls to look for include:
       * PeerDAS breakout calls
       * EOF (EVM Object Format) implementers calls
       * Verkle Tries implementers calls
   * **Major Research & Technology Updates:** Report on significant progress, new research, or benchmark results for the core technologies being developed for future upgrades. This includes:
       * Updates on testnets for these future features (e.g., "peerdas-devnet-X status").
       * Benchmark results or performance analysis (e.g., "EOF benefits for ZK proofs").
       * New research or major discussions on ethresear.ch related to statelessness, state management, etc.
  * **Primary Sources for this Section:** ethresear.ch, github.com/ethereum/pm (for meeting notes/agendas), official client team blogs, and trusted summaries on platforms like Ethereum Magicians.
  * **Keywords for Search:** "PeerDAS breakout call," "EOF implementers call," "Verkle Tries Ethereum," "Ethereum statelessness research," "peerdas-devnet," "Ethereum protocol roadmap."

**4. Layer 1**
  * **Source of Information:** You must actively browse the web for this information, focusing on ethresear.ch, github.com/ethereum/pm, ethereum-magicians.org, and relevant researcher/developer posts on platforms like X (formerly Twitter) or personal blogs.
  * **Content:** Based on developments from the past 7 days, report on significant Layer 1 protocol discussions, research, and technical developments that are not part of a major named upgrade (like Pectra or Fusaka). Crucially, your goal here is to report on specific technical discussions and research updates. Do NOT list EIPs or their status changes in this section; that information belongs in the dedicated 'EIPs/Standards' section.
  * **Focus Areas to Investigate & Report On:**
     * **Gas Limit, Fees, and Data Availability:**
        * Look for discussions or proposals regarding the gas limit, including any notable entities signaling for an increase (e.g., using a signaling dashboard).
        * Report on research related to bandwidth availability and its implications for blob count or block size.
    * **Data & Censorship Resistance:**
        * Find updates on topics like "Data Always" or discussions about the role of MEV-Boost relays in network stability and reorgs.
        * Summarize any discussions on inclusion list design, such as comparisons between same-slot vs. next-slot proposals.
    * **Networking Layer:**
        * Report on the status of QUIC support adoption across the network, including any available statistics on node distribution.
    * **Block Building & MEV Infrastructure**:
        * Look for news about new or updated block building networks (e.g., BuilderNet) or infrastructure related to MEV that aims to benefit users or stakers.
    * **Specific EIP Breakout Calls:**
        * Summarize notes from any specific breakout calls for EIPs that are related to L1 but not yet scheduled for a specific upgrade (e.g., ePBS breakout calls). Report the call number and key discussion points. Note: This is for summarizing the call's content, not for reporting the EIP's status.
  * **Keywords for Search:** "Ethereum gas limit," "Data Always Ethereum," "inclusion list design," "QUIC Ethereum," "BuilderNet," "ePBS breakout," "EVMMAX implementers call."

**5. Research**

  * **Source of Information:** You must actively browse ethresear.ch and other relevant sources (e.g., researcher blogs, academic papers) for this information.
  * **Content:** Based on developments from the past 7 days, identify and report on the most significant research topics, new posts, and active discussions. Your goal is to capture the most important research developments, whatever they may be.
  * **Output Structure:**
    * For each distinct major topic or thread you find, create a main bullet point to act as a thematic heading (e.g., * [Theme of Research]:).
    * Under each topic, create one or more nested bullet points summarizing the specific research paper, proposal, or discussion.
  * **Keywords for Search:**  "ethresear.ch," "Ethereum research."

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
  * **Scope:** Your output must ONLY contain the sections listed in this prompt (Highlight of the Week, Eth R&D Protocol Call(s), Pectra Upgrade, Future Protocol Upgrade, Layer 1, Research). Do not generate content for any other sections.
  * **Headings:** All section headings MUST be formatted as Markdown H2 headings (e.g., `## Highlight of the Week`) without any leading spaces or indentation. Do NOT use numbers in the headings.
  * **Content:** Every item you write under a heading MUST start on a new line. All list items must use bullet points.
  * **Header:** Do NOT include a main "Week in Ethereum News" header or a date. Your output should begin directly with the first section heading.
