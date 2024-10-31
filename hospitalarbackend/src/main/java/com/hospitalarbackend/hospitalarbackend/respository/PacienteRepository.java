package com.hospitalarbackend.hospitalarbackend.respository;

import com.hospitalarbackend.hospitalarbackend.model.PacienteModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PacienteRepository  extends JpaRepository<PacienteModel, Integer> {
}
