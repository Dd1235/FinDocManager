# Classification-and-Processing-of-Unstructure-Financial-Documents (Work in Progress)

## Problem

- A fictional Credit Union, "Appian Credit Union" received documents in PDF Form
- These could be
    - Applications for back accounts (credit card, savings account)
    - Identity documents (driver's license, state/country identification, passport) (Sticking to Indian documents initially)
    - Supporting financial documents (income statements, paystubs, tax returns)
    - receipts

- Need to make "best effort" categorization and summarization to speed up the process
- Categorization should be hierachical:
    - Person (associate documents to the correct person, using name, government ID, email)
    - Type: Group with similar types

## System

### Retrieval Augmented Generation (RAG)

- A RAG system can help when knowledge base contains propriety, highly sensitive information
- Helps avoid hallucation, and refuses answering when lacking context
- process documents, query relevant parts, craft the response

## Folder Structure

- `helper` consists of python scripts that aren't exactly related to the project, but are learning the tools used
- `data/` consists of the pdf documents and can be used to simulate api endpoints