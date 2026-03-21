import numpy as np 
class SonarEquation:
    def __init__(self, source_level_db: float, target_strength_db: float, noise_level_db: float, directivity_index_db: float, detection_threshold_db: float) -> float:
        self.source_level = source_level_db
        self.target_strength = target_strength_db
        self.transmission_loss = 0.0 # This will be calculated based on the considered model
        self.noise_level = noise_level_db # Can be constant or calculated using a noise model
        self.directivity_index = directivity_index_db
        self.detection_threshold = detection_threshold_db # This can be set based on the desired probability of detection and false alarm

    def spherical_TL(self, range: float) -> float:
        return 20 * np.log10(range)
    
    def cylindrical_TL(self, range: float) -> float:
        return 10 * np.log10(range)
    
    def compute_SNR(self, range: np.ndarray, model: str = "spherical") -> np.ndarray:
        if model == "spherical":
            self.transmission_loss = self.spherical_TL(range)
        elif model == "cylindrical":
            self.transmission_loss = self.cylindrical_TL(range)
        return self.source_level - self.transmission_loss + self.target_strength - self.noise_level + self.directivity_index
         