class FactCheckerAgent(Agent):
    """Agent that verifies information and flags suspicious content"""
    
    suspicious_keywords = ["error", "uncertain", "debated"]
    
    def run(self, text: str) -> Dict:
        print(f"✓ {self.name} fact checking...")
        time.sleep(0.5)
        # TODO: Check if any suspicious keywords are in the text
        flags = []  # Replace this with real logic
        return {
            "text": text,
            "accuracy": "high",
            "verified_claims": 3,
            "flags": flags
        }
