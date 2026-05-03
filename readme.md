
---

# EvoluAIr Systems - Módulo de Monitoramento de Fluidos (Protótipo)

## ✈️ Descrição do Projeto
Este projeto integra as competências da **Agenda 11** do curso de Desenvolvimento de Sistemas da ETEC com o projeto autoral **EvoluAIr Systems**. Trata-se de uma simulação de ambiente real para monitoramento do fluido de arrefecimento em aeronaves leves, como o **Cessna 172 (Motor Diesel/Jet-A1)**.

O sistema processa sinais analógicos e fornece alertas visuais coloridos, auxiliando o piloto em decisões críticas, como a interrupção de uma decolagem em caso de falha de arrefecimento.

## 🛠️ Detalhes Técnicos e Lógica de Hardware
Para garantir o realismo da simulação, o software foi desenhado sob os seguintes parâmetros:
*   **Entrada de Dados**: Simulação de um sinal analógico de **0V a 5V DC**, padrão em sensores de aquisição de dados industriais e aeronáuticos.
*   **Mapeamento de Tensão**:
    *   **1.0V**: Nível Crítico (Risco de superaquecimento).
    *   **3.0V - 4.0V**: Operação Nominal e Ideal.
    *   **5.0V**: Alerta de sobrepressão ou transbordo (Exibido em **Amarelo** para atenção).
*   **Decisão Contextual**: O sistema utiliza lógica condicional para elevar a gravidade do alerta caso o nível baixo seja detectado especificamente durante a fase de **DECOLAGEM (Take-off)**.

## 🚀 Funcionalidades
*   **Monitoramento em Tempo Real**: Classificação de 5 níveis de segurança.
*   **Alertas Visuais**: Utilização da biblioteca `colorama` para destaque de mensagens no terminal.
*   **Segurança de Voo**: Diferenciação de alertas baseado no status da aeronave.

## 📋 Requisitos e Instalação
1.  **Python 3.14+** (ou versão instalada no ambiente).
2.  **Biblioteca Colorama**:
    ```powershell
    pip install colorama
    ```

## 📂 Como Executar
1.  Navegue até a pasta do projeto: `.../DEV/Projetos/Ag_11_Colorama`.
2.  Execute o script:
    ```powershell
    python app.py
    ```

---
**Desenvolvido por:** Adriano – Técnico de Manutenção e Aluno de Desenvolvimento de Sistemas (ETEC).
**Prazo de Entrega:** 04/05/2026.
```
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Cessna_logo.svg/1280px-Cessna_logo.svg.png" width="300" alt="Cessna Logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AIRCRAFT-CESSNA%20172%20JT--A-blue?style=for-the-badge&logo=air-force" alt="Aircraft">
  <img src="https://img.shields.io/badge/SYSTEM-EVOLUAIR%20SENTINEL-orange?style=for-the-badge" alt="System">
</p>
### 🛠️ Especificações do Transdutor de Fluido
| Tensão (V) | Nível Simulado | Status do Sistema | Ação EvoluAIr |
| :--- | :--- | :--- | :--- |
| **1.0V** | Crítico | Perigo de Pane | **ALERTA VERMELHO** |
| **2.0V** | Baixo | Atenção / Leak | **ABORT (Se Take-off)** |
| **3.0V** | Nominal | Operação Padrão | Monitoramento Ativo |
| **5.0V** | Alta Pressão | Sobrecarga | **AVISO AMARELO** |
### 🛫 Flight Plan (Checklist de Desenvolvimento)
- [x] Importação da Biblioteca Colorama (Agenda 11)
- [x] Mapeamento de Sinais Analógicos (Lógica de Hardware)
- [x] Implementação de Lógica de Decisão Crítica (Take-off/Cruise)
- [x] Saída de Dados com Codificação de Cores ANSI
