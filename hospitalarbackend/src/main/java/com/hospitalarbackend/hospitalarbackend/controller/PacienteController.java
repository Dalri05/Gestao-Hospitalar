package com.hospitalarbackend.hospitalarbackend.controller;

import com.hospitalarbackend.hospitalarbackend.model.PacienteModel;
import com.hospitalarbackend.hospitalarbackend.respository.PacienteRepository;
import com.hospitalarbackend.hospitalarbackend.service.PacienteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/paciente")
public class PacienteController {
    @Autowired
    private PacienteService pacienteService;

    @Autowired
    private PacienteRepository pacienteRepository;

    @GetMapping("/listarPacientes")
    private List<PacienteModel> listarPacientes(){
        try {
            return pacienteRepository.findAll();
        } catch (Exception e){
            e.printStackTrace();
            return new ArrayList<>();
        }
    }

    @PostMapping("/criarPaciente")
    private String criarPaciente(@RequestBody PacienteModel pacienteModel){
        try {
            PacienteModel paciente = pacienteService.criarPaciente(pacienteModel);

            if (paciente != null) {
                return "Paciente cadastrado com sucesso!";
            }

            return "Não foi possível cadastrar paciente!";

        } catch (Exception e) {
            e.printStackTrace();
            return "Erro de servidor!";
        }
    }
}
