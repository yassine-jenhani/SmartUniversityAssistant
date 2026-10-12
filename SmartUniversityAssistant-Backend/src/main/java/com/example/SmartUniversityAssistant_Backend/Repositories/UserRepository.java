package com.example.SmartUniversityAssistant_Backend.Repositories;

import com.example.SmartUniversityAssistant_Backend.Models.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
