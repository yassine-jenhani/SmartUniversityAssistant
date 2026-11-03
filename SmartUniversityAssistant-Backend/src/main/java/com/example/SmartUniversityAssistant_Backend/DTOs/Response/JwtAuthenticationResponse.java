package com.example.SmartUniversityAssistant_Backend.DTOs.Response;

import com.example.SmartUniversityAssistant_Backend.Models.UserRole;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Set;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class JwtAuthenticationResponse {

    private String accessToken;
    private String tokenType;
    private String refreshToken;
    private Long userId;
    private Set<UserRole> roles;
    private boolean isVerified;

}
