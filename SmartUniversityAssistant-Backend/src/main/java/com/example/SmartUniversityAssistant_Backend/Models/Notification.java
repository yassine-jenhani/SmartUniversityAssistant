package com.example.SmartUniversityAssistant_Backend.Models;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Notification {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    private String message;

    @Column(name = "is_read")
    private boolean isRead;

    private LocalDateTime createdAt;

    private LocalDateTime readAt;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "sent_to", nullable = false, foreignKey = @ForeignKey(name = "FK_NOTIFICATION_USER"))
    private User sentTo;
}
