package com.hospitalarbackend.hospitalarbackend.service;

import com.hospitalarbackend.hospitalarbackend.Utils.ValidarCPF;
import com.hospitalarbackend.hospitalarbackend.model.PacienteModel;
import com.hospitalarbackend.hospitalarbackend.respository.PacienteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PacienteService {
    @Autowired
    private PacienteRepository pacienteRepository;

    public PacienteModel criarPaciente(PacienteModel pacienteModel) {
        boolean isPacienteValido = validarDados(pacienteModel);

        if (!isPacienteValido) return null;

        return pacienteRepository.save(pacienteModel);

    }

    public boolean validarDados(PacienteModel pacienteModel) {
        ValidarCPF validarCPF = new ValidarCPF();

        String cpfPaciente = pacienteModel.getCPF().replaceAll("[^\\d]", "");
        boolean cpfValido = validarCPF.validarCPF(cpfPaciente.trim());

        if (cpfValido) return true;

        return false;

    }
}
