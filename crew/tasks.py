from crewai import Task

def create_tasks(product, websites, researcher, analyst):

    research_task = Task(
        description=f"""
You are a strict e-commerce research agent.

CRITICAL RULES:
- You MUST use the search tools to find real products
- DO NOT say "I'll search" or "I'll start"
- DO NOT generate fake thinking steps

Search for: {product}
On: {websites}

FINAL OUTPUT FORMAT (STRICT):

For each product:

Product Name
Price
Rating
Website
Direct Link

Rules:
- Must include REAL links
- Must NOT include explanations
- Must NOT include introductions
- Must NOT include markdown headings
""",
        expected_output="Clean product list with real links",
        agent=researcher,
    )
    analysis_task = Task(
        description=f"""
You are a strict e-commerce analysis agent.
Compare all collected products for {product}

CRITICAL RULES:
- You MUST analyze the research data thoroughly
- DO NOT say "I'll analyze" or "I'll start"
- DO NOT generate fake thinking steps

You MUST rank products based on:
- price (lower is better)
- rating (higher is better)
- value for money
- Storage vs price 

For EACH product, Explain:
- why its better than others
- what are the tradeoffs
- what type of user it is best for




FINAL OUTPUT FORMAT (STRICT):
For each product:

Product Name
Price
Rating
Website
Direct Link
Reason for ranking (MUST include real analysis, with other products, no generic statements)

Rules:
- Must include REAL links
- Must NOT include explanations
- Must NOT include introductions
- Must NOT include markdown headings
""",
        expected_output="Human readable ranked list with real analysis and real links",
        agent=analyst,
    )

    return research_task, analysis_task