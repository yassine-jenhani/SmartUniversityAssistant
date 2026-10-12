package com.example.SmartUniversityAssistant_Backend.Models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "quiz_attempts")
@Getter
@Setter
@NoArgsConstructor
public class QuizAttempt {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "student_id", nullable = false)
    private Student student;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "quiz_id", nullable = false)
    private Quiz quiz;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private QuizAttemptStatus status = QuizAttemptStatus.IN_PROGRESS;

    @Column(nullable = false)
    private Double score = 0.0;

    @Column(nullable = false)
    private Double maxScore = 0.0;

    private LocalDateTime startedAt = LocalDateTime.now();

    private LocalDateTime submittedAt;

    private LocalDateTime gradedAt;

    // Optional: percentage from 0 to 100.
    private Double percentage;

    // Whether the student passed the quiz.
    private Boolean passed;
}