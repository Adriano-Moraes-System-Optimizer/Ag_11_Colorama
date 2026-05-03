
# EvoluAIr Systems - Monitoramento de Fluidos (Cessna 172)

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Cessna_logo.svg/1280px-Cessna_logo.svg.png" width="250" alt="Cessna Logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AIRCRAFT-CESSNA%20172%20JT--A-blue?style=for-the-badge&logo=air-force" alt="Aircraft">
  <img src="https://img.shields.io/badge/SYSTEM-EVOLUAIR%20SENTINEL-orange?style=for-the-badge" alt="System">
</p>

## ✈️ Sobre o Projeto
Este projeto é um protótipo do sistema **EvoluAIr**, focado no monitoramento crítico de fluido de arrefecimento para aeronaves leves. Ele integra os requisitos da **Agenda 11 (ETEC)** com lógica de hardware e segurança de voo.

## 🛠️ Especificações do Transdutor (Sinal 0-5V)
O sistema interpreta a voltagem enviada pelos sensores e define a ação necessária:

| Tensão (V) | Status do Sistema | Ação EvoluAIr | Cor no Terminal |
| :--- | :--- | :--- | :--- |
| **1.0V** | Perigo de Pane | **ALERTA CRÍTICO** | Vermelho |
| **2.0V** | Baixo / Vazamento | **ABORT (Se Take-off)** | Vermelho/Amarelo |
| **3.0V** | Operação Padrão | Monitoramento Ativo | Verde |
| **4.0V** | Performance Ideal | **NÍVEL OTIMIZADO** | Ciano |
| **5.0V** | Sobrecarga | **AVISO DE PRESSÃO** | Amarelo |

## 🚀 Lógica de Decisão Crítica
O diferencial deste software é a **inteligência contextual**:
*   **Em Voo (Cruzeiro):** Alertas de nível baixo sugerem monitoramento contínuo.
*   **Na Decolagem (Take-off):** O sistema detecta o risco e ordena **ABORTAR**, garantindo a segurança antes da aeronave deixar o solo.

## 🛫 Flight Plan (Checklist de Desenvolvimento)
- [x] Importação da Biblioteca Colorama (Requisito Agenda 11)
- [x] Mapeamento de Sinais Analógicos (0-5V DC)
- [x] Implementação de Lógica de Decisão (Take-off/Cruise)
- [x] Saída de Dados com Codificação de Cores ANSI

---
**Desenvolvido por:** Adriano 
*Técnico de Manutenção / Aluno de Desenvolvimento de Sistemas - ETEC*
