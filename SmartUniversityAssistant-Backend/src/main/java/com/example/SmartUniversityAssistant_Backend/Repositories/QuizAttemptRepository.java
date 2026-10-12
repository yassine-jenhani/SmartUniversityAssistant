package com.example.SmartUniversityAssistant_Backend.Repositories;

import com.example.SmartUniversityAssistant_Backend.Models.QuizAttempt;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface QuizAttemptRepository extends JpaRepository<QuizAttempt, UUID> {
}
