package com.hospitalarbackend.hospitalarbackend.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
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

    @JsonProperty("CPF")
    private String CPF;

    private Date dataNascimento;

    private boolean isSus;

    @OneToMany
    @JsonIgnore
    private List<ConsultaModel> consultas;
}
