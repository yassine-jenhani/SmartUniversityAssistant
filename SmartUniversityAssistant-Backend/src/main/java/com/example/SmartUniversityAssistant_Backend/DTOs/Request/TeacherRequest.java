package com.example.SmartUniversityAssistant_Backend.DTOs.Request;

import com.example.SmartUniversityAssistant_Backend.Models.Department;
import com.example.SmartUniversityAssistant_Backend.Models.Gender;
import com.example.SmartUniversityAssistant_Backend.Models.Specialization;
import com.example.SmartUniversityAssistant_Backend.Models.UserRole;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;
import java.util.List;
import java.util.Set;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class TeacherRequest {

    @NotBlank(message = "Firstname cannot be blank")
    @Size(min = 3, message = "firstname must have at least 3 characters long")
    private String firstname;

    @NotBlank(message = "Lastname cannot be blank")
    @Size(min = 3, message = "lastname must have at least 3 characters long")
    private String lastname;

    @NotBlank(message = "Email cannot be blank")
    @Email(message = "Please provide a valid email address")
    private String email;

    @NotBlank(message = "Password cannot be blank")
    @Size(min = 8, message = "Password must be at least 8 characters long")
    private String password;

    @NotBlank(message = "Address cannot be blank")
    private String address;

    @NotBlank(message = "Phone number cannot be blank")
    @Size(min = 8, message = "The phone number must be at least 8 characters")
    private String phone;

    private Set<UserRole> roles;

    private Date birthDate;

    private Gender gender;

    @NotBlank(message = "department field cannot be blank")
    private Department department;

    private List<Long> specializationIds;

}
