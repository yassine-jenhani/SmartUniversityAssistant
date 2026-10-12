package com.example.SmartUniversityAssistant_Backend.Repositories;

import com.example.SmartUniversityAssistant_Backend.Models.DocumentChunk;
import org.springframework.data.repository.CrudRepository;

import java.util.UUID;

public interface DocumentChunkRepository extends CrudRepository<DocumentChunk, UUID> {
}
