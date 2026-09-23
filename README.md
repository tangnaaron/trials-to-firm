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

## Reproducibility


## Project Structure

```text
.
├── code/                  
│   ├── python/       
│      ├── 00_generate_answer_key.py           
```