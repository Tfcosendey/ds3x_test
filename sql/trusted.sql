CREATE OR REPLACE TABLE `ps-eng-dados-ds3x.thalescosendey.icc_trusted` AS
SELECT DISTINCT
    `Mês`,
    `ICC`,
    `ICC até 10 SM`,
    `ICC + de 10 SM`,
    `ICC Homens`,
    `ICC Mulheres`,
    `ICC até 35 anos`,
    `ICC + de 35 anos`,
    `ICEA`,
    `ICEA até 10 SM`,
    `ICEA + de 10 SM`,
    `ICEA Homens`,
    `ICEA Mulheres`,
    `ICEA até 35 anos`,
    `ICEA + de 35 anos`,
    `IEC`,
    `IEC até 10 SM`,
    `IEC + de 10 SM`,
    `IEC Homens`,
    `IEC Mulheres`,
    `IEC até 35 anos`,
    `IEC + de 35 anos`,
    CURRENT_TIMESTAMP() AS load_timestamp
FROM
    `ps-eng-dados-ds3x.thalescosendey.icc_raw`;

CREATE OR REPLACE TABLE `ps-eng-dados-ds3x.thalescosendey.icf_trusted` AS
SELECT DISTINCT
    `Mês`,
    `ICF`,
    `ICF até 10 SM`,
    `ICF + de 10 SM`,
    `Emprego Atual`,
    `Emprego Atual até 10 SM`,
    `Emprego Atual + de 10 SM`,
    `Perspectiva Profissional`,
    `Perspectiva Profissional até 10 SM`,
    `Perspectiva Profissional + de 10 SM`,
    `Renda Atual`,
    `Renda Atual até 10 SM`,
    `Renda Atual + de 10 SM`,
    `Acesso a Crédito`,
    `Acesso a Crédito até 10 SM`,
    `Acesso a Crédito + de 10 SM`,
    `Nível de Consumo Atual`,
    `Nível de Consumo Atual até 10 SM`,
    `Nível de Consumo Atual + de 10 SM`,
    `Perspectiva de Consumo`,
    `Perspectiva de Consumo até 10 SM`,
    `Perspectiva de Consumo + de 10 SM`,
    `Momento para Duráveis`,
    `Momento para Duráveis até 10 SM`,
    `Momento para Duráveis + de 10 SM`,
    CURRENT_TIMESTAMP() AS load_timestamp
FROM
    `ps-eng-dados-ds3x.thalescosendey.icf_raw`;
