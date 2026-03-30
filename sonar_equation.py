import numpy as np 
import francois_garisson as fg 
class SonarEquation:
    def __init__(self, source_level_db: float, target_strength_db: float, noise_level_db: float, directivity_index_db: float, detection_threshold_db: float) -> float:
        self.source_level = source_level_db
        self.target_strength = target_strength_db
        self.transmission_loss = 0.0 # This will be calculated based on the considered model
        self.noise_level = noise_level_db # Can be constant or calculated using a noise model
        self.directivity_index = directivity_index_db
        self.detection_threshold = detection_threshold_db # This can be set based on the desired probability of detection and false alarm

    def spherical_TL(self, distance: float) -> float:
        return 20 * np.log10(distance)
    
    def cylindrical_TL(self, distance: float) -> float:
        return 10 * np.log10(distance)
    def set_absorption_loss_const(self, c, S, T, z, f, pH = 7.5): 
        self.c = c 
        self.S = S 
        self.T = T 
        self.z = z 
        self.f = f 
        self.pH = pH
    def compute_SNR(self, distance: np.ndarray, geometrical_model: str = "spherical", absorption_loss: bool = False) -> np.ndarray:
        if geometrical_model == "spherical":
            self.transmission_loss = self.spherical_TL(distance)
        elif geometrical_model == "cylindrical":
            self.transmission_loss = self.cylindrical_TL(distance)
        if absorption_loss: 
            self.transmission_loss += fg.compute_alpha(self.c, self.S, self.T, self.z, self.f, self.pH) * (distance * 10**(-3))
        return self.source_level - self.transmission_loss + self.target_strength - self.noise_level + self.directivity_index
         