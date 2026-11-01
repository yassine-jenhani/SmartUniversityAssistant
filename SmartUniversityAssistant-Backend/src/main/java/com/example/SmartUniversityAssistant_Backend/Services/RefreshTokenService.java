package com.example.SmartUniversityAssistant_Backend.Services;

import com.example.SmartUniversityAssistant_Backend.Models.RefreshToken;
import com.example.SmartUniversityAssistant_Backend.Models.User;

import java.util.Optional;

public interface RefreshTokenService {

    public RefreshToken createRefreshToken(User user);
    public Optional<RefreshToken> findByToken(String token);
    Optional<RefreshToken> findByUser(User user);
    public RefreshToken verifyExpiration(RefreshToken token);

}
