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

The system is divided into three primary components:

1. **Prompt Chaining and Research:** Collects and processes the financial-news evidence.
2. **Routing and Specialist Agents:** Routes the evidence, retrieves supporting financial data, and produces specialist analyses.
3. **Evaluator-Optimizer:** Evaluates and improves the combined draft to produce the final analysis.

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

> The prompt-chaining workflow uses Yahoo Finance to retrieve recent stock news, with a search fallback if no articles are found. Preprocessing keeps the title, summary, publication date, publisher, and URL while removing unnecessary metadata. Gemini generates a numbered research plan, dynamically classifies articles without predefined categories, extracts key financial findings, and summarizes the results. Error handling includes API retries, 15-second delays to manage rate limits, and handling invalid publication dates. The final structured output is passed to the routing and specialist agents for further analysis.
> 
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

> **Contributor completion note — Sristi:** Please document the final evaluation criteria, scoring method, acceptance threshold, optimization loop, stopping conditions, reflection or memory process, and final output fields.

> **Contributor completion note — Sristi:** Please add the name of the evaluator-optimizer notebook and the final optimized JSON or report after those files are committed to the repository.

## Repository Files

| File | Description |
|---|---|
| `README.md` | Project overview, architecture, setup instructions, workflow, results, and documentation |
| `prompt_chaining_financial_news.ipynb` | Prompt-chaining, news-research, classification, extraction, and summarization workflow |
| `zinah_prompt_chain_output.json` | Structured prompt-chaining output used by the routing workflow |
| `routing_specialist_agents.ipynb` | Routing, Yahoo Finance tools, specialist agents, validation, and export workflow |
| `routing_specialist_output.json` | Combined routing and specialist-agent output passed to the evaluator-optimizer |
| `[Evaluator notebook filename]` | **Sristi:** Replace this placeholder with the committed evaluator-optimizer notebook filename |
| `[Final output filename]` | **Sristi:** Replace this placeholder with the final optimized output filename |

## Installation Instructions

The project is designed to run in Google Colab.

### 1. Open the Notebooks

Open each notebook in Google Colab directly from the GitHub repository or upload the downloaded notebook to Colab.

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

The notebooks should be executed in workflow order.

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

1. Upload `routing_specialist_output.json` to the Colab session.
2. Load the JSON file into the evaluator-optimizer notebook.
3. Pass the `draft_analysis` and supporting workflow data to the evaluator.
4. Run the evaluation and optimization process.
5. Review and export the final optimized analysis.

> **Contributor completion note — Sristi:** Please verify these instructions and add the exact file path, function names, execution order, and export steps used in the final evaluator-optimizer notebook.

## Testing and Validation Results

### Prompt-Chaining Handoff Test

The routing notebook successfully loaded the prompt-chaining output with:

- Symbol: `AAPL`
- Processed articles: 10
- Required input fields present
- Nonempty processed-news collection

> **Contributor completion note — Zinah:** Please add any additional prompt-chaining unit tests, error-handling tests, or output-validation results demonstrated in your final notebook.

### Routing Test

The integrated routing test processed 10 articles:

- Earnings: 1 article
- News: 2 articles
- Market: 7 articles

Three ambiguous articles required Gemini fallback routing decisions. The routing workflow preserved a decision log for review.

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

> **Contributor completion note — Sristi:** Please add the evaluator score, number of optimization iterations, acceptance result, memory or reflection test, and final-output validation results.

### Final Integrated Test

> **Team completion note:** After the evaluator-optimizer is integrated, add the final test date, model configuration, total workflow result, and confirmation that the complete system runs from the initial stock symbol through the final optimized analysis.

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

> **Contributor completion note — Sristi:** Please add the model and AI-assisted functions used in the evaluator-optimizer workflow if they differ from the tools documented above.

## Conclusion

This project demonstrates how multiple agentic AI patterns can be combined into a modular financial-research workflow. Prompt chaining organizes the research and news-processing stages, routing directs the evidence to the appropriate domain specialists, dynamic Yahoo Finance tools provide supporting data, and the evaluator-optimizer improves the combined analysis.

The prompt-chaining and routing components successfully exchanged structured JSON data, processed 10 AAPL-related articles, generated three specialist analyses, and prepared a complete draft for the evaluator-optimizer. The modular design also makes it possible to inspect intermediate outputs, identify evidence limitations, and test each component separately.

> **Team completion note:** After the final integrated test, add one sentence confirming the evaluator-optimizer result and the successful completion of the full workflow.

## References

Google. (2026). *Gemini API documentation*. Google AI for Developers. https://ai.google.dev/gemini-api/docs

OpenAI. (2026). *ChatGPT* [Large language model]. https://chatgpt.com/

yfinance. (2026). *yfinance documentation*. https://ranaroussi.github.io/yfinance/

Yahoo Finance. (2026). *Yahoo Finance*. https://finance.yahoo.com/
