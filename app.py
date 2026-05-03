import colorama
from colorama import Fore, Style

# Inicializa o colorama para o terminal (Requisito da Atividade)
colorama.init()

def definir_cor_e_alerta(nivel, fase_voo):
    """
    Função que define a cor e a gravidade da mensagem baseada no nível (0-5V)
    e na fase do voo (Simulação de Ambiente Real).
    """
    if nivel == 1:
        return Fore.RED + Style.BRIGHT, "CRITICAL LOW - Risco de pane OVERHIT/superaquecimento"
    elif nivel == 2:
        if fase_voo == "DECOLAGEM":
            return Fore.RED + Style.BRIGHT, "ABORTAR OPERAÇÃO - Falha de arrefecimento detectada"
        return Fore.YELLOW, "LOW LEVEL - Verificar sistema de arrefecimento"
    elif nivel == 3:
        return Fore.GREEN, "NOMINAL - Nível de fluido operacional"
    elif nivel == 4:
        return Fore.CYAN, "OPTIMAL - Performance ideal para cruzeiro"
    elif nivel == 5:
        # Alterado para Amarelo conforme solicitado
        return Fore.YELLOW, "OVERFLOW/PRESSURE - Alerta de alta pressão no reservatório"
    else:
        return Fore.WHITE, "SENSOR ERROR - Verifique a fiação (0-5V)"
    
def simular_monitoramento():
    # Lista de situações baseada no projeto EvoluAIr / Cessna 172
    # Simulando leituras do sensor analógico (Requisito: Usar listas e valores definidos)
    leituras_sensor = [5, 4, 3, 2, 1]
    fases = ["TAXI", "DECOLAGEM", "CRUZEIRO"]
    
    # Simulação: Nível 2 detectado durante a DECOLAGEM
    fase_atual = fases[1] 

    print(f"--- EVOLUAIR SYSTEMS | MONITORAMENTO DE FLUIDOS ---")
    print(f"STATUS DA AERONAVE: {fase_atual}\n")

    for leitura in leituras_sensor:
        cor, mensagem = definir_cor_e_alerta(leitura, fase_atual)
        
        # Exibe a situação com a cor correspondente e restaura o estilo (Requisito)
        print(f"Sensor (In): {leitura}.0V | {cor}{mensagem}{Style.RESET_ALL}")

    print("\n" + "-" * 50)
    print("Simulação concluída. Dados enviados ao log do sistema.")

if __name__ == "__main__":
    simular_monitoramento()
