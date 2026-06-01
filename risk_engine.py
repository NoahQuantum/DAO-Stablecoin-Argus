"""
=============================================================================
Project : DAO-Stablecoin-Argus
Layer   : Layer 2 - Advanced Analytics Layer
Module  : risk_engine.py
Author  : NoahQuantum (Noah-Bridge DAO)

[Description]
This module serves as the central mathematical engine of the Advanced 
Analytics Layer. It aggregates risk metrics from Layer 1 (Data Ingestion) 
and other Layer 2 trackers to compute a definitive Coin Run Vulnerability 
Score (Scale: 0-100). It acts as the brain of the DAO, determining the 
overall health and vulnerability of the stablecoin ecosystem.
=============================================================================
"""

class RiskEngine:
    def __init__(self):
        print("🧮 [Layer 2] Risk Engine initialized.")
        self.base_score = 0.0

    def calculate_vulnerability_score(self, divergence_pct: float, whale_z_score: float, sovereign_risk: int) -> float:
        """
        Calculates the final vulnerability score using weighted parameters.
        - divergence_pct: Gap between off-chain reserves and on-chain supply.
        - whale_z_score: Anomaly score of large capital flights in DEX pools.
        - sovereign_risk: NLP-based regulatory threat score.
        """
        print("[Risk Engine] Aggregating risk vectors...")
        
        # Risk weights (Subject to DAO governance voting)
        weight_divergence = 2.0  # High impact
        weight_whale = 1.5       # Medium-High impact
        weight_sovereign = 1.0   # Baseline impact

        # Normalize and compute component scores
        score_div = min(divergence_pct * weight_divergence * 10, 40) # Max 40 points
        score_whale = min(max(whale_z_score, 0) * weight_whale * 10, 30) # Max 30 points
        score_sov = min(sovereign_risk * weight_sovereign, 30) # Max 30 points

        final_score = score_div + score_whale + score_sov
        final_score = min(final_score, 100.0) # Cap at 100

        print(f"📊 [Risk Engine] Final Coin Run Vulnerability Score: {final_score:.2f} / 100")
        
        if final_score >= 75.0:
            print("🚨 CRITICAL: Severe risk of a Coin Run. Immediate action required!")
        elif final_score >= 50.0:
            print("⚠️ WARNING: Elevated risk levels detected. Monitor closely.")
        else:
            print("✅ SAFE: Ecosystem is currently stable.")

        return final_score

if __name__ == '__main__':
    # Diagnostic test run with mock inputs
    engine = RiskEngine()
    engine.calculate_vulnerability_score(divergence_pct=0.8, whale_z_score=2.5, sovereign_risk=15)
