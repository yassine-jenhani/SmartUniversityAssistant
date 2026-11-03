package com.example.SmartUniversityAssistant_Backend.Services;

import com.example.SmartUniversityAssistant_Backend.DTOs.Request.AdminRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.LoginRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.StudentRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.TeacherRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Response.JwtAuthenticationResponse;

public interface AuthenticationService {

    // Register methods
    JwtAuthenticationResponse registerAdmin(AdminRequest request);
    JwtAuthenticationResponse registerStudent(StudentRequest request);
    JwtAuthenticationResponse registerTeacher(TeacherRequest request);

    // Sign in method
    public JwtAuthenticationResponse SignIn(LoginRequest request);
}
