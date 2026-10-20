# AAI-520 Group 6: Multi-Agent Financial Analysis System

## Project Overview

This project implements a multi-agent financial research system that analyzes company news, financial results, and recent market activity. The system combines prompt chaining, intelligent article routing, specialist agents with dynamic financial tools, and an evaluator-optimizer workflow.

The project was developed for AAI-520: Natural Language Processing and Generative AI. Apple Inc. (`AAPL`) was used for the integrated workflow test.

## Project Objective

The objective is to build a modular Investment Research Agent that can:

- Develop a financial research plan for a selected stock.
- Retrieve and process current financial news.
- Classify and route articles to appropriate specialist agents.
- Use dynamic Yahoo Finance tools to gather supporting evidence.
- Generate structured earnings, company-news, and market analyses.
- Combine the specialist findings into a unified draft.
- Evaluate and improve the draft before producing the final analysis.

## GitHub Repository

[AAI-520 Group 6 Multi-Agent Financial Analysis](https://github.com/ZinahO/AAI-520-Group-6-Multi-Agent-Financial-Analysis)

## Team Members and Contributions

| Team Member | Primary Contribution |
|---|---|
| Zinah Othman | Prompt chaining, financial-news research, data preprocessing, classification, information extraction, and summarization |
| Noslinn Tosta | Article routing, specialist agents, Yahoo Finance tools, validation, combined draft generation, and JSON handoff |
| Sristi Ghimire | Evaluator-optimizer, reflection, memory, final analysis, and output validation |
| All team members | System integration, end-to-end testing, documentation, GitHub collaboration, and final review |

## System Architecture

| Stage | Input | Main Process | Output | Owner |
|---|---|---|---|---|
| Prompt Chaining and Research | Stock symbol (`AAPL`) | Research planning, news retrieval, preprocessing, classification, extraction, and summarization | `zinah_prompt_chain_output.json` | Zinah |
| Routing and Specialist Agents | Prompt-chaining JSON | Article routing, Yahoo Finance tool execution, specialist analysis, and draft generation | `routing_specialist_output.json` | Noslinn |
| Evaluator-Optimizer | Routing and specialist JSON | Evaluation, revision, reflection, and quality optimization | Final optimized financial analysis | Sristi |

The system processes information in the following order:

**Stock Symbol → Prompt Chaining → Article Routing → Specialist Agents → Combined Draft → Evaluator-Optimizer → Final Financial Analysis**

In the final integrated notebook, `prompt_chain_output` and `routing_specialist_output` are passed directly between stages in memory. The JSON files remain available as reproducibility checkpoints and records of the team integration process.

The system is divided into three primary components:

1. **Prompt Chaining and Research:** Collects and processes the financial-news evidence.
2. **Routing and Specialist Agents:** Routes the evidence, retrieves supporting financial data, and produces specialist analyses.
3. **Evaluator-Optimizer:** Evaluates and improves the combined draft to produce the final analysis.

The complete system demonstrates four agent functions: research planning, dynamic financial-tool use, self-reflection, and persistent memory.

## Complete Workflow

### 1. Prompt Chaining and Research

The prompt-chaining workflow receives a stock symbol and develops a research plan. It retrieves financial news from Yahoo Finance and processes the articles through the following stages:

1. Ingest
2. Preprocess
3. Classify
4. Extract
5. Summarize

The completed prompt-chaining data is exported as:

- `zinah_prompt_chain_output.json`

This file provides the structured input required by the routing and specialist-agent workflow.

The prompt-chaining workflow uses Yahoo Finance to retrieve recent stock news, with a search fallback if no articles are found. Preprocessing keeps the title, summary, publication date, publisher, and URL while removing unnecessary metadata. Gemini generates a numbered research plan, dynamically classifies articles without predefined categories, extracts key financial findings, and summarizes the results. Error handling includes API retries, 15-second delays to manage rate limits, and handling invalid publication dates. The final structured output is passed to the routing and specialist agents for further analysis.

### 2. Routing and Specialist Agents

The routing and specialist-agent component was developed by Noslinn Tosta. It loads the prompt-chaining JSON file, validates the required fields, routes the processed articles, runs the appropriate Yahoo Finance tools, and generates structured specialist analyses.

#### Input Validation

The routing notebook confirms that the prompt-chaining output includes:

- `symbol`
- `research_plan`
- `processed_news`
- `summary`

It also verifies that the processed-news collection is not empty before continuing.

#### Article Routing

Each processed article is assigned to one of three categories:

- `earnings`
- `news`
- `market`

The router first examines the article’s existing classification and content. When the correct category remains ambiguous, the shared Gemini `call_llm()` function is used as a fallback routing mechanism.

The routing log records information about each decision so that the team can review how the articles were assigned.

#### Specialist Agents and Dynamic Tools

| Specialist | Purpose | Dynamic Tool |
|---|---|---|
| Earnings Specialist | Examines revenue, net income, EPS, and earnings-related evidence | Yahoo Finance quarterly income statement |
| News Specialist | Reviews company developments and operational information | Yahoo Finance company profile |
| Market Specialist | Evaluates recent price performance, volatility, and trading volume | Yahoo Finance one-month price history |

Each specialist analysis contains the following required sections:

- Key Findings
- Supporting Evidence
- Positive Signals
- Negative Signals
- Risks and Limitations

The specialist agents distinguish reported facts from interpretation and identify situations in which the available evidence is insufficient to support a conclusion.

#### Combined Draft Analysis

The three specialist analyses are combined into one structured draft containing:

- Earnings Specialist Analysis
- News Specialist Analysis
- Market Specialist Analysis

This draft is passed to the evaluator-optimizer for quality review and revision.

#### Routing Output

The completed routing workflow is exported as:

- `routing_specialist_output.json`

The JSON file contains these top-level fields:

- `symbol`
- `research_plan`
- `source_summary`
- `routing_log`
- `routed_articles`
- `specialist_results`
- `draft_analysis`
- `workflow_status`

The `draft_analysis` field is the primary input for the evaluator-optimizer stage.

### 3. Evaluator-Optimizer, Reflection, and Memory

The evaluator-optimizer receives the combined specialist draft and reviews it for accuracy, completeness, structure, evidence use, and clarity. It then determines whether the draft meets the required quality threshold or needs further revision.

The Evaluator Agent uses a 100-point rubric consisting of factual accuracy (30 points), completeness (20 points), risk assessment (20 points), clarity (15 points), and relevance (15 points). The passing threshold is 80 points. If the analysis does not pass, the Optimizer Agent revises it using the evaluator feedback and lessons retrieved from memory. The loop stops when the analysis passes, reaches the maximum number of revisions, or encounters a handled API, JSON, or validation error.

After evaluation, the self-reflection component records the initial and latest scores, improvement, strengths, weaknesses, and lessons learned. The memory component saves this reflection to `agent_memory.json` and retrieves relevant lessons for future optimization prompts.

The primary evaluator-optimizer files are:

- `evaluator_optimizer.ipynb`
- `evaluator_optimizer_output.json`
- `optimization_test_results.json`
- `agent_memory.json`

The final integrated notebook also creates `/content/AAI_520_Group_6_Final_Project_Output.json`, which contains the prompt-chaining output, routing and specialist results, evaluator-optimizer result, optional optimization test, and overall workflow status.

## Repository Files

| File | Description |
|---|---|
| `README.md` | Project overview, architecture, setup instructions, workflow, results, and documentation |
| `AAI520_Group6_Multi_Agent_Financial_Analysis.ipynb` | Final integrated notebook containing the complete end-to-end workflow |
| `AAI520_Group6_Multi_Agent_Financial_Analysis.pdf` | Readable PDF export of the completed integrated notebook |
| `prompt_chaining_financial_news.ipynb` | Prompt-chaining, news-research, classification, extraction, and summarization workflow |
| `zinah_prompt_chain_output.json` | Structured prompt-chaining output used by the routing workflow |
| `routing_specialist_agents.ipynb` | Routing, Yahoo Finance tools, specialist agents, validation, and export workflow |
| `routing_specialist_output.json` | Combined routing and specialist-agent output passed to the evaluator-optimizer |
| `evaluator_optimizer.ipynb` | Evaluator-optimizer, reflection, memory, and final-analysis workflow |
| `evaluator_optimizer_output.json` | Evaluator-optimizer result checkpoint |
| `optimization_test_results.json` | Deliberately weak-analysis optimization test results |
| `agent_memory.json` | Saved reflection records and lessons learned |
| `rubric.py` | Defines the evaluation criteria, scoring weights, and passing threshold used by the evaluator-optimizer workflow |

## Installation Instructions

The project is designed to run in Google Colab.

### 1. Open the Notebooks

For the final end-to-end workflow, open `AAI520_Group6_Multi_Agent_Financial_Analysis.ipynb` in Google Colab. The three original component notebooks remain in the repository to document each team member's contribution and may also be opened separately.

### 2. Install the Required Libraries

Run the following command in Colab:

```python
!pip install -q yfinance google-genai
```

### 3. Configure the Gemini API Key

1. Create or obtain a valid Gemini API key.
2. Open the **Secrets** panel in Google Colab.
3. Add a secret named:

```text
GEMINI_API_KEY
```

4. Enable notebook access to the secret.

The API key must not be written directly into a notebook or committed to GitHub.

### Requirements

- Python 3
- Google Colab
- Google Gemini API access
- `google-genai`
- `yfinance`
- `pandas`
- Internet access for retrieving dynamic financial and news data

## Execution Instructions

### Recommended: Run the Final Integrated Notebook

1. Open `AAI520_Group6_Multi_Agent_Financial_Analysis.ipynb` in Google Colab.
2. Confirm that `GEMINI_API_KEY` is available through Colab Secrets.
3. Select **Runtime > Run all**.
4. Confirm that the research plan and 10 processed-news records are generated.
5. Confirm that every article receives a routing decision and written reason.
6. Confirm that all three Yahoo Finance tools report a successful status.
7. Confirm that the three specialist analyses contain all required sections.
8. Confirm that the evaluator returns a final score and status.
9. Confirm that reflection and memory are saved.
10. Confirm that the final output reports `workflow_status: completed`.

The final integrated notebook passes its structured outputs directly between stages in memory, so manual JSON uploads are not required. The component-by-component instructions below document the original team workflow and can be used to test each notebook separately.

### Component-by-Component Execution

The original notebooks should be executed in workflow order.

### Step 1: Run the Prompt-Chaining Notebook

1. Open `prompt_chaining_financial_news.ipynb` in Google Colab.
2. Confirm that `GEMINI_API_KEY` is available through Colab Secrets.
3. Run the notebook cells in order.
4. Confirm that the research plan and processed-news records are generated.
5. Export or download `zinah_prompt_chain_output.json`.

### Step 2: Run the Routing and Specialist Notebook

1. Open `routing_specialist_agents.ipynb` in Google Colab.
2. Upload `zinah_prompt_chain_output.json` to the Colab session.
3. Confirm that the JSON path in the loading cell is:

```python
json_path = "/content/zinah_prompt_chain_output.json"
```

4. Confirm that `GEMINI_API_KEY` is available through Colab Secrets.
5. Run the notebook cells in order.
6. Confirm that the articles are routed successfully.
7. Confirm that all Yahoo Finance tools complete successfully.
8. Confirm that the three specialist analyses contain the required sections.
9. Generate the combined draft analysis.
10. Export or download `routing_specialist_output.json`.

### Step 3: Run the Evaluator-Optimizer Notebook

1. Open `evaluator_optimizer.ipynb` in Google Colab.
2. Upload `routing_specialist_output.json` to the Colab session.
3. Load the routing output and pass its `symbol`, `draft_analysis`, and `specialist_results` to the evaluator-optimizer workflow.
4. Run the evaluator, optimizer, self-reflection, and persistent-memory cells in order.
5. Confirm that the evaluation result includes a score, status, revision history, reflection, and memory status.
6. Review and export `evaluator_optimizer_output.json`, `optimization_test_results.json`, and `agent_memory.json`.

## Testing and Validation Results

### Prompt-Chaining Handoff Test

The routing notebook successfully loaded the prompt-chaining output with:

- Symbol: `AAPL`
- Processed articles: 10
- Required input fields present
- Nonempty processed-news collection

The prompt-chaining workflow was successfully tested using AAPL, retrieving and processing 10 news articles through all five stages. The final output was verified to include the stock symbol, research plan, classified articles, extracted findings, and summary. Error handling includes Gemini API retries, request delays, a Yahoo Finance search fallback, and invalid date handling. No separate automated unit tests were implemented; validation was performed through successful notebook execution and output review.

### Routing Test

The integrated routing test processed 10 articles:

- Earnings: 2 articles
- News: 5 articles
- Market: 3 articles

Five ambiguous articles required Gemini fallback routing decisions. The routing workflow preserved a decision log and written reason for every article.

### Financial Tool Test

All three Yahoo Finance tool paths executed successfully:

- Earnings Specialist: quarterly income statement
- News Specialist: company profile
- Market Specialist: one-month price history

### Specialist Analysis Test

The workflow successfully generated earnings, news, and market analyses. Each analysis passed validation for the following required sections:

- Key Findings
- Supporting Evidence
- Positive Signals
- Negative Signals
- Risks and Limitations

The notebook produced the confirmation:

```text
All specialist analyses contain the required sections.
```

### Handoff Test

The completed output included the expected fields and produced the following confirmations:

```text
Full end-to-end workflow completed successfully.
Evaluator-optimizer handoff is ready.
Symbol: AAPL
Specialists: ['earnings', 'news', 'market']
Draft analysis included: True
```

The routing output was successfully exported as `routing_specialist_output.json`.

### Evaluator-Optimizer Test

The live integrated AAPL analysis received a score of 93/100 and passed the 80-point quality threshold on its initial evaluation. No revision was required. Self-reflection completed successfully, and the resulting lessons were saved to persistent memory.

Because the live analysis passed on its first evaluation, a deliberately weak analysis was tested separately to demonstrate the Optimizer Agent. The weak analysis improved from 32/100 to 72/100 after one optimization cycle. This demonstration was intentionally limited to one revision, so it stopped at the maximum-revision condition before reaching the passing threshold. The result confirms that the Optimizer responded to evaluator feedback and that the stopping condition worked correctly.

### Final Integrated Test

The final integrated workflow was tested on October 19, 2026, using `AAPL` and Gemini model `gemini-3.7-flash`. The complete system ran from the initial stock symbol through research planning, five-stage prompt chaining, article routing, three specialist agents, dynamic Yahoo Finance tools, combined draft generation, evaluation, self-reflection, persistent memory, and final structured output creation.

The final run reported:

```text
Integrated project output created successfully.
Symbol: AAPL
Workflow status: completed
Final evaluation status: passed
Final score: 93
```

## Validation and Error Handling

The routing and specialist workflow includes checks for:

- Required prompt-chaining fields
- Nonempty processed-news input
- Supported routing categories
- Valid fallback routing decisions
- Successful Yahoo Finance tool results
- Required specialist-analysis headings
- Required handoff fields
- Presence of the combined draft analysis
- Required evaluator rubric criteria
- Valid integer scores within each criterion's range
- Nonempty optimized and final analyses
- Evaluation stopping conditions
- Self-reflection and persistent-memory status
- Final integrated output fields and completion status

These checks identify missing data or integration problems before the output is passed to the next workflow stage.

## Limitations

- Yahoo Finance data is dynamic, so results may change between executions.
- News availability and article summaries depend on the data returned by Yahoo Finance.
- Gemini API quotas or rate limits may interrupt model calls.
- A one-month market window does not provide long-term performance context.
- A single quarterly financial statement does not establish historical growth.
- News articles may discuss companies other than the selected ticker.
- External news summaries may lack detailed financial or operational evidence.
- AI-generated analysis may contain incomplete, inaccurate, or unsupported statements.
- The workflow requires human review before its findings are used.
- The system is an academic prototype and is not intended for production investment decisions.

## Ethical Considerations and Financial Disclaimer

The system uses AI-generated analysis and third-party financial data. These sources may contain inaccuracies, incomplete information, bias, or outdated data. The workflow therefore includes validation steps and requires human review of routing decisions, evidence, interpretations, and final conclusions.

The project does not use its outputs to make autonomous financial decisions. Users should verify important claims through authoritative financial filings, official company announcements, and qualified financial professionals.

This project was created for educational purposes. Its outputs do not constitute investment recommendations, financial advice, legal advice, or guarantees of future market performance. Neither the project team nor the system is responsible for financial decisions made using its generated analysis.

## AI-Assisted Tools Disclosure

Generative AI tools were used to support the development and implementation of this project. Google Gemini is integrated directly into the financial-analysis workflow through the Gemini API. The current prompt-chaining implementation uses `gemini-3.7-flash` to generate a research plan, classify financial news, extract key information, and summarize the findings.

Gemini is also used within the routing and specialist workflow for fallback routing decisions and structured specialist-analysis generation.

ChatGPT was used as a development-support tool for reviewing code structure, troubleshooting implementation and integration issues, improving code comments and documentation, developing the README, and identifying potential workflow improvements.

All AI-generated suggestions and outputs were reviewed, tested, and modified as needed before being incorporated into the project. AI responses were not treated as automatically correct. The team used code execution, structured validation, evidence checks, and workflow testing to evaluate the generated results.

Yahoo Finance (`yfinance`) was used as the financial-data and news source.

The evaluator-optimizer also uses `gemini-3.7-flash`. Gemini evaluates the combined analysis, produces structured feedback, revises analyses that do not meet the passing threshold, and supports the deliberately weak-analysis optimization demonstration. Self-reflection and memory are implemented in Python using the evaluator history and local JSON storage.

## Conclusion

This project demonstrates how multiple agentic AI patterns can be combined into a modular financial-research workflow. Prompt chaining organizes the research and news-processing stages, routing directs the evidence to the appropriate domain specialists, dynamic Yahoo Finance tools provide supporting data, and the evaluator-optimizer improves the combined analysis.

The prompt-chaining and routing components successfully exchanged structured JSON data, processed 10 AAPL-related articles, generated three specialist analyses, and prepared a complete draft for the evaluator-optimizer. The modular design also makes it possible to inspect intermediate outputs, identify evidence limitations, and test each component separately.

The final integrated AAPL analysis passed the evaluator with a score of 93/100, saved its self-reflection to memory, and completed the full workflow successfully.

## References

Google. (2026). *Gemini API documentation*. Google AI for Developers. https://ai.google.dev/gemini-api/docs

OpenAI. (2026). *ChatGPT* [Large language model]. https://chatgpt.com/

yfinance. (2026). *yfinance documentation*. https://ranaroussi.github.io/yfinance/

Yahoo Finance. (2026). *Yahoo Finance*. https://finance.yahoo.com/
