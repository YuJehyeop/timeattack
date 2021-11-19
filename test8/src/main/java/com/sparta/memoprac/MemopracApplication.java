package com.sparta.memoprac;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@EnableJpaAuditing
@SpringBootApplication
public class MemopracApplication {

    public static void main(String[] args) {
        SpringApplication.run(MemopracApplication.class, args);
    }

}
