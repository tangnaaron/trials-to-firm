# Introduction

## About
ClinicalTrials.gov records almost every clinical trial run in the United States: who sponsors it, the phase, the condition, when it started, and whether and why it stopped. That makes it close to a complete census of drug development. But it cannot answer questions about firms, for four reasons.

Sponsors are typed as free text, not identifiers, so one firm appears under many spellings, subsidiary names and legal suffixes.
Ownership changes are invisible. When a firm is acquired or renamed, the registry never links the old name to the new one, so a firm's pipeline history breaks at every deal.
There is no therapeutic-area classification.
Why a trial stopped sits in a free-text field.

We are building a public database that fixes all four and links trials to the firms behind them, year by year, for listed pharmaceutical and medical-device firms from about 2005 to the present. Three things come out of it: the database, a data article that documents and validates it, and an empirical paper that uses it. Jennifer Kao is a co-author on the project.

The co-authors read the project outline this month and agreed that the ownership layer is the main contribution: knowing, trial by trial, which pipelines changed hands, when, and under what name the combined firm carried on. No existing database records that, and it is what makes questions about acquisitions answerable, such as which of a target's trials an acquirer keeps and which it stops.

The rule that shapes everything. Every number we release must be reproducible by anyone from free public sources. That is why the ownership layer is built from SEC filings, which are public, rather than from a commercial deals database. It is also why the work starts with a test: before building a method on SEC filings, we need to know how far they reach.


## SEC EDGAR M&A Reconstruction Pilot
This part evaluates whether SEC EDGAR filings alone can be used to
reconstruct key facts about known corporate acquisitions and renamings.

For each deal, the project attempts to recover four facts:

1. Date the deal was agreed
2. Date the deal closed
3. Date the target ceased to be a public company
4. Name of the combined company afterward

The project compares an answer key constructed from company-issued press
releases against results reconstructed using SEC EDGAR filings alone.

### Answer Key

`code/python/scripts/00_generate_answer_key.py` hand-codes the answer key for
16 test cases spanning 2009–2023 and writes it to `data/answer_key.csv`. Each
fact is sourced from company press releases (archived via the Wayback Machine
where the original page is gone), exchange notices (e.g. Nasdaq Trader), or
company reports, never from SEC filings, so that the key is independent of the
method being tested.

`data/answer_key.csv` has one row per case with the following columns:

| Column | Description |
|---|---|
| `deal_id` | Case identifier (1–16) |
| `acquirer`, `target` | Acquirer and target (blank where there is no clear acquirer–target relationship, i.e. the control case and Mylan/Upjohn) |
| `parties` | List of all public companies involved, filled for every case (e.g. `['Mylan N.V.', 'Pfizer Inc.']`); for a divested business unit, its public parent is listed |
| `name_change_occurred` | Whether the surviving public company changed its name |
| `name_change_date` | Date the name change took effect |
| `resulting_public_company_name` | Name of the public company that carried on after the deal (fact 4)|
| `public_company_that_ceased_trading` | Company that stopped being publicly traded  |
| `ceased_public_date` | Date that company ceased to be public (fact 3)|
| `agreement_date` | Date the deal was agreed (fact 1) |
| `closing_date` | Date the deal closed (fact 2) |
| `agreement_source`, `closing_source`, `public_status_source`, `name_source` | URL supporting each fact |
| `notes` | Deal structure details and caveats |

All dates are formatted `YYYY-MM-DD`; a blank cell means the fact does not
apply to that case. `parties` is stored in the CSV as a Python list literal;
parse it with `ast.literal_eval` after reading.

## Reproducibility

Requires Python 3 and `pandas`. Run scripts from the repository root, since
output paths are relative to it:

```bash
python code/python/scripts/00_generate_answer_key.py
```

This regenerates `data/answer_key.csv`.

## Project Structure

```text
.
├── code/
│   └── python/
│       └── scripts/
│           └── 00_generate_answer_key.py   # builds the answer key
├── data/
│   └── answer_key.csv                      # answer key output
└── README.md
```