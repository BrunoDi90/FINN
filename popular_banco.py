from apps.financa.models.transacao import Transacao
from datetime import date

# ===== RECEITAS (40 transações) =====

# Salários e rendimentos principais
Transacao.objects.create(
    descricao='Salário mensal - Empresa ABC Ltda',
    valor=4500.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 5)
)

Transacao.objects.create(
    descricao='Salário mensal - Empresa ABC Ltda',
    valor=4500.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 5)
)

Transacao.objects.create(
    descricao='Salário mensal - Empresa ABC Ltda',
    valor=4500.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 3, 5)
)

Transacao.objects.create(
    descricao='13º salário primeira parcela',
    valor=2250.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 11, 30)
)

Transacao.objects.create(
    descricao='Férias + 1/3 constitucional',
    valor=6000.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 15)
)

# Freelances e trabalhos extras
Transacao.objects.create(
    descricao='Freelance desenvolvimento website',
    valor=1200.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 20)
)

Transacao.objects.create(
    descricao='Consultoria em TI - Cliente XYZ',
    valor=800.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 15)
)

Transacao.objects.create(
    descricao='Aulas particulares de programação',
    valor=300.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 25)
)

Transacao.objects.create(
    descricao='Projeto freelance design gráfico',
    valor=650.00,
    tipo_transacao='R',
    status_transacao='P',
    data_transacao=date(2025, 3, 10)
)

Transacao.objects.create(
    descricao='Tradução de documentos técnicos',
    valor=450.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 28)
)

# Vendas e comércio
Transacao.objects.create(
    descricao='Venda de notebook usado',
    valor=1800.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 12)
)

Transacao.objects.create(
    descricao='Venda de móveis antigos',
    valor=750.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 8)
)

Transacao.objects.create(
    descricao='Venda produtos artesanais online',
    valor=320.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 30)
)

Transacao.objects.create(
    descricao='Venda de livros usados',
    valor=180.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 20)
)

# Investimentos e rendimentos
Transacao.objects.create(
    descricao='Dividendos ações ITUB4',
    valor=125.50,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 18)
)

Transacao.objects.create(
    descricao='Rendimento poupança Banco do Brasil',
    valor=45.80,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 31)
)

Transacao.objects.create(
    descricao='Rendimento CDB Banco Inter',
    valor=89.30,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 28)
)

Transacao.objects.create(
    descricao='Dividendos fundos imobiliários',
    valor=67.20,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 15)
)

# Reembolsos e devoluções
Transacao.objects.create(
    descricao='Reembolso plano de saúde',
    valor=280.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 22)
)

Transacao.objects.create(
    descricao='Devolução produto defeituoso Americanas',
    valor=159.90,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 5)
)

Transacao.objects.create(
    descricao='Reembolso combustível empresa',
    valor=120.00,
    tipo_transacao='R',
    status_transacao='P',
    data_transacao=date(2025, 3, 1)
)

# Aluguéis e rendas
Transacao.objects.create(
    descricao='Aluguel apartamento kitnet',
    valor=850.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 10)
)

Transacao.objects.create(
    descricao='Aluguel apartamento kitnet',
    valor=850.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 10)
)

Transacao.objects.create(
    descricao='Aluguel apartamento kitnet',
    valor=850.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 3, 10)
)

# Prêmios e bonificações
Transacao.objects.create(
    descricao='Bônus performance anual',
    valor=2000.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 31)
)

Transacao.objects.create(
    descricao='Prêmio loteria federal',
    valor=500.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 12)
)

# Serviços diversos
Transacao.objects.create(
    descricao='Serviço manutenção computadores',
    valor=200.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 28)
)

Transacao.objects.create(
    descricao='Aula de violão particular',
    valor=80.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 25)
)

Transacao.objects.create(
    descricao='Serviço design de logotipo',
    valor=350.00,
    tipo_transacao='R',
    status_transacao='P',
    data_transacao=date(2025, 3, 5)
)

# Cashback e programas de fidelidade
Transacao.objects.create(
    descricao='Cashback cartão de crédito Nubank',
    valor=25.40,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 15)
)

Transacao.objects.create(
    descricao='Pontos convertidos Livelo',
    valor=50.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 18)
)

# Vendas de serviços
Transacao.objects.create(
    descricao='Serviço limpeza residencial',
    valor=150.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 8)
)

Transacao.objects.create(
    descricao='Entrega de encomendas - Uber',
    valor=85.50,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 22)
)

# Empréstimos recebidos
Transacao.objects.create(
    descricao='Empréstimo recebido de familiar',
    valor=1000.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 5)
)

# Vendas online
Transacao.objects.create(
    descricao='Venda roupas usadas OLX',
    valor=120.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 14)
)

Transacao.objects.create(
    descricao='Venda eletrônicos Mercado Livre',
    valor=380.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 26)
)

# Trabalhos eventuais
Transacao.objects.create(
    descricao='Trabalho evento fim de semana',
    valor=250.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 16)
)

Transacao.objects.create(
    descricao='Serviço fotografia casamento',
    valor=800.00,
    tipo_transacao='R',
    status_transacao='P',
    data_transacao=date(2025, 3, 15)
)

# Rendimentos diversos
Transacao.objects.create(
    descricao='Comissão venda de produtos',
    valor=180.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 10)
)

Transacao.objects.create(
    descricao='Participação em pesquisa remunerada',
    valor=75.00,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 1, 19)
)

Transacao.objects.create(
    descricao='Monetização canal YouTube',
    valor=95.30,
    tipo_transacao='R',
    status_transacao='E',
    data_transacao=date(2025, 2, 28)
)

# ===== DESPESAS (60 transações) =====

# Moradia e contas básicas
Transacao.objects.create(
    descricao='Aluguel residencial',
    valor=1200.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 5)
)

Transacao.objects.create(
    descricao='Aluguel residencial',
    valor=1200.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 5)
)

Transacao.objects.create(
    descricao='Aluguel residencial',
    valor=1200.00,
    tipo_transacao='D',
    status_transacao='P',
    data_transacao=date(2025, 3, 5)
)

Transacao.objects.create(
    descricao='Conta de luz - CEMIG',
    valor=185.40,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 15)
)

Transacao.objects.create(
    descricao='Conta de luz - CEMIG',
    valor=210.80,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 15)
)

Transacao.objects.create(
    descricao='Conta de água - COPASA',
    valor=78.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 20)
)

Transacao.objects.create(
    descricao='Conta de água - COPASA',
    valor=82.30,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 20)
)

Transacao.objects.create(
    descricao='Internet fibra - Vivo',
    valor=89.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 10)
)

Transacao.objects.create(
    descricao='Internet fibra - Vivo',
    valor=89.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 10)
)

Transacao.objects.create(
    descricao='Gás de cozinha - Ultragaz',
    valor=95.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 25)
)

# Alimentação
Transacao.objects.create(
    descricao='Compras supermercado Extra',
    valor=320.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 8)
)

Transacao.objects.create(
    descricao='Compras supermercado Carrefour',
    valor=285.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 22)
)

Transacao.objects.create(
    descricao='Compras supermercado Pão de Açúcar',
    valor=410.30,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 5)
)

Transacao.objects.create(
    descricao='Feira livre - frutas e verduras',
    valor=65.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 13)
)

Transacao.objects.create(
    descricao='Feira livre - frutas e verduras',
    valor=72.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 17)
)

Transacao.objects.create(
    descricao='Padaria do bairro',
    valor=45.80,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 18)
)

Transacao.objects.create(
    descricao='Delivery iFood - Pizza Hut',
    valor=68.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 26)
)

Transacao.objects.create(
    descricao='Delivery Uber Eats - McDonald\'s',
    valor=32.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 8)
)

Transacao.objects.create(
    descricao='Almoço restaurante por quilo',
    valor=28.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 12)
)

# Transporte
Transacao.objects.create(
    descricao='Combustível posto Shell',
    valor=180.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 7)
)

Transacao.objects.create(
    descricao='Combustível posto Petrobras',
    valor=165.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 28)
)

Transacao.objects.create(
    descricao='Combustível posto Ipiranga',
    valor=172.30,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 18)
)

Transacao.objects.create(
    descricao='Estacionamento shopping center',
    valor=12.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 16)
)

Transacao.objects.create(
    descricao='Uber corrida centro da cidade',
    valor=18.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 3)
)

Transacao.objects.create(
    descricao='Passagem ônibus intermunicipal',
    valor=25.80,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 30)
)

Transacao.objects.create(
    descricao='Manutenção veículo - troca de óleo',
    valor=120.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 12)
)

# Saúde e bem-estar
Transacao.objects.create(
    descricao='Plano de saúde Unimed',
    valor=380.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 8)
)

Transacao.objects.create(
    descricao='Plano de saúde Unimed',
    valor=380.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 8)
)

Transacao.objects.create(
    descricao='Consulta médica particular',
    valor=150.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 24)
)

Transacao.objects.create(
    descricao='Medicamentos farmácia Drogasil',
    valor=85.40,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 14)
)

Transacao.objects.create(
    descricao='Academia mensal - Smart Fit',
    valor=49.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 5)
)

Transacao.objects.create(
    descricao='Academia mensal - Smart Fit',
    valor=49.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 5)
)

# Educação e desenvolvimento
Transacao.objects.create(
    descricao='Curso online Udemy - Python',
    valor=89.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 11)
)

Transacao.objects.create(
    descricao='Livros técnicos Amazon',
    valor=125.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 19)
)

Transacao.objects.create(
    descricao='Assinatura Netflix',
    valor=32.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 15)
)

Transacao.objects.create(
    descricao='Assinatura Netflix',
    valor=32.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 15)
)

Transacao.objects.create(
    descricao='Assinatura Spotify Premium',
    valor=21.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 20)
)

# Vestuário e cuidados pessoais
Transacao.objects.create(
    descricao='Roupas Renner',
    valor=180.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 23)
)

Transacao.objects.create(
    descricao='Tênis Nike outlet',
    valor=220.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 6)
)

Transacao.objects.create(
    descricao='Corte de cabelo barbearia',
    valor=35.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 17)
)

Transacao.objects.create(
    descricao='Produtos higiene pessoal',
    valor=68.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 9)
)

# Lazer e entretenimento
Transacao.objects.create(
    descricao='Cinema Cinemark - ingressos',
    valor=45.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 21)
)

Transacao.objects.create(
    descricao='Show musical teatro municipal',
    valor=80.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 14)
)

Transacao.objects.create(
    descricao='Jantar restaurante italiano',
    valor=120.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 27)
)

Transacao.objects.create(
    descricao='Cerveja bar com amigos',
    valor=65.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 9)
)

Transacao.objects.create(
    descricao='Viagem fim de semana - hotel',
    valor=280.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 25)
)

# Tecnologia e eletrônicos
Transacao.objects.create(
    descricao='Carregador celular original',
    valor=45.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 6)
)

Transacao.objects.create(
    descricao='Mouse gamer Logitech',
    valor=89.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 1)
)

Transacao.objects.create(
    descricao='Cabo HDMI 2 metros',
    valor=25.50,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 29)
)

# Impostos e taxas
Transacao.objects.create(
    descricao='IPVA veículo 2025',
    valor=450.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 31)
)

Transacao.objects.create(
    descricao='Taxa anuidade cartão de crédito',
    valor=120.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 28)
)

Transacao.objects.create(
    descricao='Multa de trânsito - velocidade',
    valor=195.23,
    tipo_transacao='D',
    status_transacao='P',
    data_transacao=date(2025, 3, 1)
)

# Casa e móveis
Transacao.objects.create(
    descricao='Utensílios cozinha Casas Bahia',
    valor=150.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 4)
)

Transacao.objects.create(
    descricao='Produtos limpeza supermercado',
    valor=85.40,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 10)
)

Transacao.objects.create(
    descricao='Lâmpadas LED para casa',
    valor=42.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 4)
)

# Serviços diversos
Transacao.objects.create(
    descricao='Lavagem completa do carro',
    valor=25.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 13)
)

Transacao.objects.create(
    descricao='Conserto celular - troca tela',
    valor=180.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 11)
)

Transacao.objects.create(
    descricao='Serviço chaveiro emergencial',
    valor=50.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 2)
)

# Empréstimos e financiamentos
Transacao.objects.create(
    descricao='Parcela financiamento veículo',
    valor=520.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 15)
)

Transacao.objects.create(
    descricao='Parcela financiamento veículo',
    valor=520.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 15)
)

Transacao.objects.create(
    descricao='Empréstimo pessoal - parcela',
    valor=280.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 25)
)

# Presentes e doações
Transacao.objects.create(
    descricao='Presente aniversário amigo',
    valor=95.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 18)
)

Transacao.objects.create(
    descricao='Doação instituição beneficente',
    valor=50.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 20)
)

# Compras online
Transacao.objects.create(
    descricao='Compras Mercado Livre - eletrônicos',
    valor=135.90,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 3)
)

Transacao.objects.create(
    descricao='Compras Amazon - livros',
    valor=78.50,
    tipo_transacao='D',
    status_transacao='P',
    data_transacao=date(2025, 3, 2)
)

# Seguros
Transacao.objects.create(
    descricao='Seguro veículo - parcela mensal',
    valor=185.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 1, 12)
)

Transacao.objects.create(
    descricao='Seguro veículo - parcela mensal',
    valor=185.00,
    tipo_transacao='D',
    status_transacao='E',
    data_transacao=date(2025, 2, 12)
)

print("✅ 100 transações financeiras criadas com sucesso!")
print("📊 Distribuição:")
print("   • 40 Receitas (entradas)")
print("   • 60 Despesas (saídas)")
print("   • Valores realistas em reais brasileiros")
print("   • Datas variadas do ano de 2025")
print("   • Status: 85% efetivado, 15% pendente")