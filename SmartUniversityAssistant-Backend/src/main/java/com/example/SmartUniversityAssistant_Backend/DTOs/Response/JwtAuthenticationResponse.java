package com.example.SmartUniversityAssistant_Backend.DTOs.Response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class JwtAuthenticationResponse {

    private String accessToken;
    private String tokenType;
    private String refreshToken;
    private Long userId;
    private String role;
    private boolean isVerified;

}
