package com.example.SmartUniversityAssistant_Backend.DTOs.Response;

import com.example.SmartUniversityAssistant_Backend.Models.Department;
import com.example.SmartUniversityAssistant_Backend.Models.Gender;
import com.example.SmartUniversityAssistant_Backend.Models.UserRole;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;
import java.util.Set;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class TeacherResponse {

    private String firstname;
    private String lastname;
    private String email;
    private String password;
    private String address;
    private String phone;
    private String profilePicture;
    private Set<UserRole> roles;
    private Date birthDate;
    private Gender gender;
    private String teacherNumber;
    private Department department;
    private String specialization;

}
