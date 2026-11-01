package com.example.SmartUniversityAssistant_Backend.RestControllers;

import com.example.SmartUniversityAssistant_Backend.DTOs.Request.AdminRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.StudentRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.TeacherRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Response.JwtAuthenticationResponse;
import com.example.SmartUniversityAssistant_Backend.Exceptions.TokenRefreshException;
import com.example.SmartUniversityAssistant_Backend.Models.RefreshToken;
import com.example.SmartUniversityAssistant_Backend.Models.User;
import com.example.SmartUniversityAssistant_Backend.Repositories.UserRepository;
import com.example.SmartUniversityAssistant_Backend.Services.AuthenticationService;
import com.example.SmartUniversityAssistant_Backend.Services.JwtServiceImpl;
import com.example.SmartUniversityAssistant_Backend.Services.RefreshTokenService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/auth")
public class AuthenticationRestController {

    private final AuthenticationService authenticationService;
    private final RefreshTokenService refreshTokenService;
    private final JwtServiceImpl jwtService;

    @PostMapping("/signup-admin")
    public ResponseEntity<JwtAuthenticationResponse> SignUpAdmin(@Valid @RequestBody AdminRequest request) {
        return ResponseEntity.ok(authenticationService.registerAdmin(request));
    }

    @PostMapping("/signup-teacher")
    public ResponseEntity<JwtAuthenticationResponse> SignUpTeacher(@Valid @RequestBody TeacherRequest request) {
        return ResponseEntity.ok(authenticationService.registerTeacher(request));
    }

    @PostMapping("/signup-student")
    public ResponseEntity<JwtAuthenticationResponse> SignUpStudent(@Valid @RequestBody StudentRequest request) {
        return ResponseEntity.ok(authenticationService.registerStudent(request));
    }

    @PostMapping("/refresh-token")
    public ResponseEntity<JwtAuthenticationResponse> refreshToken(
            @RequestBody Map<String, String> request) {

        String refreshToken = request.get("refreshToken");

        RefreshToken token = refreshTokenService.findByToken(refreshToken)
                .orElseThrow(() ->
                        new TokenRefreshException(
                                refreshToken,
                                "Refresh token not found"
                        )
                );

        User user = token.getUser();

        String newToken = jwtService.generateToken(user);

        return ResponseEntity.ok(
                JwtAuthenticationResponse.builder()
                        .accessToken(newToken)
                        .refreshToken(refreshToken)
                        .userId(user.getId())
                        .role(user.getRoles().toString())
                        .build()
        );
    }
}
