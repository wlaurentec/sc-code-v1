package com.alterapirest.apirest.Repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.alterapirest.apirest.Entities.Producto;

public interface ProductoRepository extends JpaRepository<Producto, Long> {

}
