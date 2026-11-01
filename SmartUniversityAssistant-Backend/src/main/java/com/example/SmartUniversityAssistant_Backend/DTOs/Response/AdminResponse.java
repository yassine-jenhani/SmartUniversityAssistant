package com.example.SmartUniversityAssistant_Backend.DTOs.Response;

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
public class AdminResponse {

    private Long adminId;
    private String firstname;
    private String lastname;
    private String email;
    private String address;
    private String phone;
    private String profilePicture;
    private Set<UserRole> roles;
    private Date birthDate;
    private Gender gender;

}
