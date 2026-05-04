from IncidentsDashboard import app, db, Incidents

incidents_data = [
    # 2024 - Janeiro (5 incidentes - pico)
    {"date": "2024-01-05", "type": "Malware", "severity": "Alta", "affected_area": "TI", "description": "Ransomware detectado em servidor de arquivos"},
    {"date": "2024-01-12", "type": "Phishing", "severity": "Média", "affected_area": "RH", "description": "Email fraudulento com link malicioso"},
    {"date": "2024-01-18", "type": "DDoS", "severity": "Alta", "affected_area": "TI", "description": "Ataque volumétrico derrubou portal do cliente"},
    {"date": "2024-01-22", "type": "Engenharia Social", "severity": "Baixa", "affected_area": "Financeiro", "description": "Tentativa de obtenção de credenciais por telefone"},
    {"date": "2024-01-29", "type": "Acesso Não Autorizado", "severity": "Alta", "affected_area": "TI", "description": "Tentativa de acesso remoto não autorizado"},
    # 2024 - Fevereiro (2 incidentes)
    {"date": "2024-02-10", "type": "Malware", "severity": "Média", "affected_area": "Operações", "description": "Trojan identificado em estação de trabalho"},
    {"date": "2024-02-22", "type": "Phishing", "severity": "Baixa", "affected_area": "Marketing", "description": "Colaborador reportou email suspeito"},
    # 2024 - Março (1 incidente)
    {"date": "2024-03-15", "type": "Acesso Não Autorizado", "severity": "Média", "affected_area": "Jurídico", "description": "Acesso a documentos fora do horário"},
    # 2024 - Abril (4 incidentes)
    {"date": "2024-04-02", "type": "DDoS", "severity": "Alta", "affected_area": "TI", "description": "Ataque de negação de serviço no servidor web"},
    {"date": "2024-04-11", "type": "Malware", "severity": "Alta", "affected_area": "Financeiro", "description": "Banking trojan interceptou transações"},
    {"date": "2024-04-19", "type": "Engenharia Social", "severity": "Média", "affected_area": "RH", "description": "Funcionário manipulado a revelar dados internos"},
    {"date": "2024-04-27", "type": "Phishing", "severity": "Alta", "affected_area": "Diretoria", "description": "Spear phishing direcionado a executivos"},
    # 2024 - Maio (1 incidente)
    {"date": "2024-05-20", "type": "Acesso Não Autorizado", "severity": "Baixa", "affected_area": "RH", "description": "Ex-funcionário tentou acessar sistema"},
    # 2024 - Junho (6 incidentes - maior pico)
    {"date": "2024-06-03", "type": "Malware", "severity": "Alta", "affected_area": "TI", "description": "Worm se propagando pela rede interna"},
    {"date": "2024-06-07", "type": "DDoS", "severity": "Alta", "affected_area": "TI", "description": "Ataque coordenado derrubou sistemas por 4 horas"},
    {"date": "2024-06-12", "type": "Phishing", "severity": "Alta", "affected_area": "Diretoria", "description": "CEO fraud tentando redirecionar transferência"},
    {"date": "2024-06-17", "type": "Engenharia Social", "severity": "Alta", "affected_area": "TI", "description": "Atacante se passou por suporte técnico"},
    {"date": "2024-06-22", "type": "Malware", "severity": "Média", "affected_area": "Operações", "description": "Spyware encontrado em notebook corporativo"},
    {"date": "2024-06-28", "type": "Acesso Não Autorizado", "severity": "Alta", "affected_area": "TI", "description": "Brute force bem-sucedido em conta de administrador"},
    # 2024 - Julho (2 incidentes)
    {"date": "2024-07-14", "type": "DDoS", "severity": "Média", "affected_area": "TI", "description": "Sobrecarga no servidor de email"},
    {"date": "2024-07-29", "type": "Phishing", "severity": "Baixa", "affected_area": "Marketing", "description": "Campanha de phishing em massa detectada"},
    # 2024 - Agosto (3 incidentes)
    {"date": "2024-08-06", "type": "Malware", "severity": "Alta", "affected_area": "TI", "description": "Rootkit encontrado em servidor de banco de dados"},
    {"date": "2024-08-15", "type": "Engenharia Social", "severity": "Média", "affected_area": "Operações", "description": "Visitante tentou acessar área restrita"},
    {"date": "2024-08-27", "type": "Acesso Não Autorizado", "severity": "Alta", "affected_area": "TI", "description": "Credenciais comprometidas usadas no VPN"},
    # 2024 - Setembro (1 incidente)
    {"date": "2024-09-10", "type": "Phishing", "severity": "Média", "affected_area": "Financeiro", "description": "Tentativa de fraude simulando banco"},
    # 2024 - Outubro (4 incidentes)
    {"date": "2024-10-04", "type": "Malware", "severity": "Alta", "affected_area": "Operações", "description": "Ransomware criptografou arquivos de produção"},
    {"date": "2024-10-13", "type": "DDoS", "severity": "Alta", "affected_area": "TI", "description": "Ataque durante período de férias"},
    {"date": "2024-10-21", "type": "Engenharia Social", "severity": "Baixa", "affected_area": "RH", "description": "PUP detectado e removido pelo antivírus"},
    {"date": "2024-10-30", "type": "Phishing", "severity": "Alta", "affected_area": "Diretoria", "description": "Whaling attack contra CFO da empresa"},
    # 2024 - Novembro (2 incidentes)
    {"date": "2024-11-08", "type": "Acesso Não Autorizado", "severity": "Média", "affected_area": "Jurídico", "description": "Acesso a documentos confidenciais"},
    {"date": "2024-11-25", "type": "Malware", "severity": "Alta", "affected_area": "TI", "description": "Keylogger detectado em computador da equipe"},
    # 2024 - Dezembro (1 incidente)
    {"date": "2024-12-15", "type": "DDoS", "severity": "Média", "affected_area": "TI", "description": "Ataque no período de festas"},
    # 2025 - Janeiro (5 incidentes - pico)
    {"date": "2025-01-06", "type": "Malware", "severity": "Alta", "affected_area": "TI", "description": "Novo ransomware variante detectado"},
    {"date": "2025-01-13", "type": "Phishing", "severity": "Alta", "affected_area": "Diretoria", "description": "Campanha direcionada a gestores"},
    {"date": "2025-01-19", "type": "DDoS", "severity": "Alta", "affected_area": "TI", "description": "Ataque volumétrico de longa duração"},
    {"date": "2025-01-24", "type": "Engenharia Social", "severity": "Média", "affected_area": "Financeiro", "description": "Ligação suspeita solicitando dados corporativos"},
    {"date": "2025-01-30", "type": "Acesso Não Autorizado", "severity": "Alta", "affected_area": "TI", "description": "Tentativa de acesso via exploit conhecido"},
    # 2025 - Fevereiro (2 incidentes)
    {"date": "2025-02-11", "type": "Malware", "severity": "Média", "affected_area": "Marketing", "description": "Adware instalado via software não autorizado"},
    {"date": "2025-02-26", "type": "Phishing", "severity": "Baixa", "affected_area": "RH", "description": "Email suspeito reportado sem clique"},
    # 2025 - Março (3 incidentes)
    {"date": "2025-03-05", "type": "DDoS", "severity": "Alta", "affected_area": "TI", "description": "Ataque coordenado contra infraestrutura"},
    {"date": "2025-03-17", "type": "Malware", "severity": "Alta", "affected_area": "Financeiro", "description": "Banking trojan interceptou transações financeiras"},
    {"date": "2025-03-28", "type": "Engenharia Social", "severity": "Média", "affected_area": "Operações", "description": "Funcionário entregou crachá a não autorizado"},
    # 2025 - Abril (1 incidente)
    {"date": "2025-04-14", "type": "Acesso Não Autorizado", "severity": "Baixa", "affected_area": "RH", "description": "Tentativa de login com credenciais expiradas"},
    # 2025 - Maio (4 incidentes)
    {"date": "2025-05-03", "type": "Malware", "severity": "Alta", "affected_area": "TI", "description": "Rootkit encontrado em servidor crítico"},
    {"date": "2025-05-12", "type": "Phishing", "severity": "Alta", "affected_area": "Diretoria", "description": "Whaling attack contra novo diretor"},
    {"date": "2025-05-20", "type": "DDoS", "severity": "Média", "affected_area": "TI", "description": "Sobrecarga no sistema de autenticação"},
    {"date": "2025-05-29", "type": "Engenharia Social", "severity": "Alta", "affected_area": "TI", "description": "Atacante se passou por fornecedor externo"},
]

with app.app_context():
    db.drop_all()
    db.create_all()
    
    for item in incidents_data:
        incident = Incidents(
            Date=item["date"],
            Type=item["type"],
            Severity=item["severity"],
            Affected_area=item["affected_area"],
            Description=item["description"]
        )
        db.session.add(incident)
    
    db.session.commit()
    print(f"{len(incidents_data)} incidentes inseridos com sucesso!")
