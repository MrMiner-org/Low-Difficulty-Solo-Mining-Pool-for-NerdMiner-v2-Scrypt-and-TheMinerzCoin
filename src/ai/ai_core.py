from ai.ai_models.pool_optimization_model import PoolOptimizationModel
from ai.ai_models.rewards_prediction_model import RewardsPredictionModel
from utils.logger import log

class AICore:
    def __init__(self):
        self.opt_model = PoolOptimizationModel()
        self.pred_model = RewardsPredictionModel()

    def optimize_pool(self):
        log("AI: Optimizing pool parameters...")
        self.opt_model.train()
        recommendations = self.opt_model.get_recommendations()
        log(f"AI Recommendations: {recommendations}")

    def predict_rewards(self):
        log("AI: Predicting rewards...")
        self.pred_model.train()
        predictions = self.pred_model.predict()
        log(f"AI Reward Predictions: {predictions}")
