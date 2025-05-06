class FactCheckerAgent(Agent):
    """Agent that verifies information and flags suspicious content"""
    
    suspicious_keywords = ["error", "uncertain", "debated"]
    
    def run(self, text: str) -> Dict:
        print(f"✓ {self.name} fact checking...")
        time.sleep(0.5)
        # Identify suspicious keywords in the text
        flags = [kw for kw in self.suspicious_keywords if kw in text.lower()]
        return {
            "text": text,
            "accuracy": "high",
            "verified_claims": 3,
            "flags": flags
        }
