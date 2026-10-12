package com.example.SmartUniversityAssistant_Backend.Models;

import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "students")
@Getter
@Setter
@NoArgsConstructor
public class Student extends User {

    private String studentNumber;

    private String university;

    private String major;

    private Integer studyYear;

}
