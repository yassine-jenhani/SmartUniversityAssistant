package com.example.SmartUniversityAssistant_Backend.Repositories;

import com.example.SmartUniversityAssistant_Backend.Models.User;
import com.example.SmartUniversityAssistant_Backend.Models.UserRole;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String username);

    boolean existsByRolesContaining(UserRole role);
}
