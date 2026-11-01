package com.example.SmartUniversityAssistant_Backend.Config;

import com.example.SmartUniversityAssistant_Backend.Models.AccountStatus;
import com.example.SmartUniversityAssistant_Backend.Models.Admin;
import com.example.SmartUniversityAssistant_Backend.Models.Gender;
import com.example.SmartUniversityAssistant_Backend.Models.UserRole;
import com.example.SmartUniversityAssistant_Backend.Repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.time.LocalDateTime;
import java.util.Calendar;
import java.util.Date;
import java.util.Set;

@Configuration
@RequiredArgsConstructor
public class SuperAdminSeeder {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Bean
    CommandLineRunner initAdmin() {
        return args -> {

            boolean superAdminExists =
                    userRepository.existsByRolesContaining(
                            UserRole.SUPER_ADMIN
                    );

            if (superAdminExists) {
                return;
            }

            Admin admin = new Admin();

            // Create birthDate using Calendar or simple Date instantiation
            Calendar calendar = Calendar.getInstance();
            calendar.set(2002, Calendar.MARCH, 30);
            Date birthDate = calendar.getTime();

            admin.setFirstName("System");
            admin.setLastName("Administrator");
            admin.setAdminNumber("A01");
            admin.setEmail("system.administrator@gmail.com");
            admin.setPassword(passwordEncoder.encode("system**123"));
            admin.setRoles(Set.of(UserRole.SUPER_ADMIN));
            admin.setEnabled(true);
            admin.setPhone("+216********");
            admin.setAddress("Tunis");
            admin.setStatus(AccountStatus.ENABLED);
            admin.setBirthDate(birthDate);
            admin.setGender(Gender.MALE);
            admin.setVerified(true);
            admin.setCreatedAt(LocalDateTime.now());

            userRepository.save(admin);

            System.out.println(
                    "Super Admin user created successfully."
            );
        };
    }
}