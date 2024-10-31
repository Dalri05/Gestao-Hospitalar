package com.hospitalarbackend.hospitalarbackend.model;

import jakarta.persistence.*;
import lombok.Data;

import java.util.Date;
import java.util.List;

@Entity
@Data
public class ConsultaModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @ManyToOne
    private PacienteModel paciente;

    private String exameFeito;

    private Date dateConsulta = new Date();

    private Double valorConsulta;

}
