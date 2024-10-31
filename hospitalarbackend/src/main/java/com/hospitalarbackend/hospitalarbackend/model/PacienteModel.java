package com.hospitalarbackend.hospitalarbackend.model;

import jakarta.persistence.*;
import lombok.Data;

import java.util.Date;
import java.util.List;

@Entity
@Data
public class PacienteModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    private String nome;

    @OneToOne
    private ContaModel conta;

    private String CPF;

    private Date dataNascimento;

    private boolean isSus = false;

    @OneToMany
    private List<ConsultaModel> consultas;
}
