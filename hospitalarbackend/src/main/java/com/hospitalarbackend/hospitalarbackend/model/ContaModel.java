package com.hospitalarbackend.hospitalarbackend.model;

import jakarta.persistence.*;
import lombok.Data;

import java.util.Date;

@Entity
@Data
public class ContaModel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(nullable = false, unique = true)
    private String usuario;

    @Column(nullable = false)
    private String senha;

    private Date dataCadastro = new Date();

    private boolean isContaAtiva = true;

    private boolean isAdministrador = false;

}
