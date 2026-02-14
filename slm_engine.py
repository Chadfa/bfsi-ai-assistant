class SLMEngine:
    def __init__(self):
        pass

    def generate(self, query):
        query_lower = query.lower()

        # Simulated fine-tuned domain logic

        if "loan" in query_lower:
            return "Loan-related queries depend on eligibility criteria, credit assessment, and internal policy guidelines. Please refer to official documentation or contact support for account-specific details."

        if "emi" in query_lower:
            return "EMI calculations are based on principal amount, tenure, and interest rate. Please refer to your loan agreement for precise breakdown."

        if "interest" in query_lower:
            return "Interest rates may be fixed or floating depending on loan type and market conditions. Updated rates are available on the official portal."

        if "penalty" in query_lower or "late" in query_lower:
            return "Late payment penalties are applied as per loan agreement terms. Please review your agreement for specific charges."

        if "application" in query_lower:
            return "Loan application processing depends on documentation verification and eligibility assessment. Please check your registered portal for updates."

        # If no domain match → return None
        return None
