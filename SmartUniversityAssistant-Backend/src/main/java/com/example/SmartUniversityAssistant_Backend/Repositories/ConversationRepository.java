package com.example.SmartUniversityAssistant_Backend.Repositories;

import com.example.SmartUniversityAssistant_Backend.Models.Conversation;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface ConversationRepository extends JpaRepository<Conversation, UUID> {
}
