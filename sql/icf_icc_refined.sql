CREATE OR REPLACE TABLE `ps-eng-dados-ds3x.thalescosendey.icf_icc_refined` AS
SELECT
    -- Criação da chave temporal
    FORMAT_TIMESTAMP('%Y-%m', icc.`Mês`) AS ano_mes,

    -- Métricas do ICC
    icc.`ICC` AS icc_indice,
    (icc.`ICC` - LAG(icc.`ICC`, -1) OVER (ORDER BY FORMAT_TIMESTAMP('%Y-%m', icc.`Mês`) DESC)) / LAG(icc.`ICC`, -1) OVER (ORDER BY FORMAT_TIMESTAMP('%Y-%m', icc.`Mês`) DESC) * 100 AS icc_percent_variacao,

    -- Métricas do ICF
    icf.`ICF` AS icf_indice,
    (icf.`ICF` - LAG(icf.`ICF`, -1) OVER (ORDER BY FORMAT_TIMESTAMP('%Y-%m', icf.`Mês`) DESC)) / LAG(icf.`ICF`, -1) OVER (ORDER BY FORMAT_TIMESTAMP('%Y-%m', icf.`Mês`) DESC) * 100 AS icf_percent_variacao,

    -- Timestamp de criação da tabela refinada
    CURRENT_TIMESTAMP() AS load_timestamp
FROM
    `ps-eng-dados-ds3x.thalescosendey.icc_trusted` icc
JOIN
    `ps-eng-dados-ds3x.thalescosendey.icf_trusted` icf
ON
    FORMAT_TIMESTAMP('%Y-%m', icc.`Mês`) = FORMAT_TIMESTAMP('%Y-%m', icf.`Mês`)
ORDER BY
    FORMAT_TIMESTAMP('%Y-%m', icc.`Mês`) DESC;
