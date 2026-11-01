package com.example.SmartUniversityAssistant_Backend.Services;

import com.example.SmartUniversityAssistant_Backend.DTOs.Request.AdminRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.StudentRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Request.TeacherRequest;
import com.example.SmartUniversityAssistant_Backend.DTOs.Response.JwtAuthenticationResponse;
import com.example.SmartUniversityAssistant_Backend.Exceptions.EmailAlreadyExistsException;
import com.example.SmartUniversityAssistant_Backend.Exceptions.ResourceNotFoundException;
import com.example.SmartUniversityAssistant_Backend.Models.*;
import com.example.SmartUniversityAssistant_Backend.Repositories.*;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
@RequiredArgsConstructor
public class AuthenticationServiceImpl implements AuthenticationService {

    private final UserRepository userRepository;
    private final AdminRepository adminRepository;
    private final TeacherRepository teacherRepository;
    private final StudentRepository studentRepository;
    private final PasswordEncoder passwordEncoder;
    private final SpecializationRepository specializationRepository;
    private final RefreshTokenService refreshTokenService;
    private final JwtService jwtService;

    @Override
    public JwtAuthenticationResponse registerAdmin(AdminRequest request) {

        // Check if the email exists
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new EmailAlreadyExistsException("Email already in use");
        }

        long adminCount = adminRepository.count();
        String generatedAdminNumber = String.format("A%02d", adminCount + 1);

        // Assign role if no roles are provided
        Set<UserRole> assignedRoles = request.getRoles() != null ? request.getRoles() : Set.of(UserRole.ADMIN);

        var admin = Admin.builder()
                .email(request.getEmail())
                .password(passwordEncoder.encode(request.getPassword()))
                .adminNumber(generatedAdminNumber)
                .isVerified(false)
                .isEnabled(true)
                .address(request.getAddress())
                .gender(request.getGender())
                .phone(request.getPhone())
                .birthDate(request.getBirthDate())
                .status(AccountStatus.ENABLED)
                .lastName(request.getLastname())
                .firstName(request.getFirstname())
                .roles(assignedRoles)
                .build();

        userRepository.save(admin);

        // Generate token & Refresh token
        var jwt = jwtService.generateToken(admin);
        var refreshToken = refreshTokenService.createRefreshToken(admin);

        return JwtAuthenticationResponse.builder()
                .accessToken(jwt)
                .refreshToken(refreshToken.getToken())
                .role(assignedRoles.toString())
                .tokenType("Bearer")
                .isVerified(false)
                .userId(admin.getId())
                .build();
    }

    @Override
    public JwtAuthenticationResponse registerStudent(StudentRequest request) {

        // Check if the email exists
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new EmailAlreadyExistsException("Email already in use");
        }

        long studentCount = studentRepository.count();
        String generatedStudentNumber = String.format("S%04d", studentCount + 1);

        // Assign role if no roles are provided
        Set<UserRole> assignedRoles = request.getRoles() != null ? request.getRoles() : Set.of(UserRole.STUDENT);

        var student = Student.builder()
                .email(request.getEmail())
                .password(passwordEncoder.encode(request.getPassword()))
                .isVerified(false)
                .isEnabled(true)
                .address(request.getAddress())
                .gender(request.getGender())
                .studyYear(request.getStudyYear())
                .studentNumber(generatedStudentNumber)
                .phone(request.getPhone())
                .birthDate(request.getBirthDate())
                .status(AccountStatus.ENABLED)
                .lastName(request.getLastname())
                .firstName(request.getFirstname())
                .roles(assignedRoles)
                .build();

        userRepository.save(student);

        // Generate token & Refresh token
        var jwt = jwtService.generateToken(student);
        var refreshToken = refreshTokenService.createRefreshToken(student);

        return JwtAuthenticationResponse.builder()
                .accessToken(jwt)
                .refreshToken(refreshToken.getToken())
                .role(assignedRoles.toString())
                .tokenType("Bearer")
                .isVerified(false)
                .userId(student.getId())
                .build();
    }

    @Override
    public JwtAuthenticationResponse registerTeacher(TeacherRequest request) {

        // Check if the email exists
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new EmailAlreadyExistsException("Email already in use");
        }

        long teacherCount = teacherRepository.count();
        String generatedTeacherNumber = String.format("T%03d", teacherCount + 1);

        List<Specialization> foundSpecializations = specializationRepository.findAllById(request.getSpecializationIds());

        if (foundSpecializations.isEmpty()) {
            throw new ResourceNotFoundException("At least one valid specialization must be provided.");
        }

        // Assign role if no roles are provided
        Set<UserRole> assignedRoles = request.getRoles() != null ? request.getRoles() : Set.of(UserRole.TEACHER);

        var teacher = Teacher.builder()
                .email(request.getEmail())
                .password(passwordEncoder.encode(request.getPassword()))
                .isVerified(false)
                .isEnabled(true)
                .teacherNumber(generatedTeacherNumber)
                .department(request.getDepartment())
                .specializations(new HashSet<>(foundSpecializations))
                .address(request.getAddress())
                .gender(request.getGender())
                .phone(request.getPhone())
                .birthDate(request.getBirthDate())
                .status(AccountStatus.ENABLED)
                .lastName(request.getLastname())
                .firstName(request.getFirstname())
                .roles(assignedRoles)
                .build();

        userRepository.save(teacher);

        // Generate token & Refresh token
        var jwt = jwtService.generateToken(teacher);
        var refreshToken = refreshTokenService.createRefreshToken(teacher);

        return JwtAuthenticationResponse.builder()
                .accessToken(jwt)
                .refreshToken(refreshToken.getToken())
                .role(assignedRoles.toString())
                .tokenType("Bearer")
                .isVerified(false)
                .userId(teacher.getId())
                .build();
    }

}
