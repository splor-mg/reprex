# Reprex: Modelagem Simplificada de Servidores SPLOR

Este reprex demonstra a modelagem simplificada de banco de dados para servidores da equipe SPLOR, focando nas informações essenciais conforme especificado no issue.

## 📋 Objetivos

1. **Regras de unicidade e constraints:**
   - Cada servidor deve ser registrado apenas uma vez na tabela principal
   - Garantir CPF único e MASP único como constraints

2. **Histórico de servidores:**
   - Necessidade de manter histórico dos servidores com datas de ingresso e saída pregressas
   - Dados relevantes: data de ingresso, data de saída, observações

3. **Relacionamento entre tabelas:**
   - Estrutura simples com duas tabelas principais
   - Garantir relacionamentos claros entre servidores ativos e histórico
   - **Evitar duplicação de informações**

## 🗂️ Estrutura do Reprex

### Arquivos Principais
- `datapackage.yaml` - Configuração do datapackage com as duas tabelas essenciais
- `scripts.py` - Script para gerar diagrama ER baseado na inferência dos dados
- `scripts_from_yaml.py` - Script para gerar diagrama ER baseado no YAML
- `requirements.txt` - Dependências necessárias

### Dados de Exemplo
- `data/servidores_ativos.csv` - Dados essenciais dos servidores ativos
- `data/servidores_historico.csv` - Histórico de movimentações dos servidores

## 🔧 Como Usar

### 1. Instalar dependências Python:
```bash
pip install -r requirements.txt
```

### 2. Instalar Graphviz (para gerar diagramas):

**Windows:**
```bash
# Opção 1: Via winget
winget install graphviz

# Opção 2: Via Chocolatey
choco install graphviz

# Opção 3: Via Scoop
scoop install graphviz

# Opção 4: Download direto
# Baixe de: https://graphviz.org/download/
```

**Linux:**
```bash
sudo apt-get install graphviz  # Ubuntu/Debian
sudo yum install graphviz      # CentOS/RHEL
```

**macOS:**
```bash
brew install graphviz
```

### 3. Gerar diagramas ER:
```bash
# Gerar diagrama ER baseado na inferência
python scripts.py

# Gerar diagrama ER baseado no YAML
python scripts_from_yaml.py
```

### 4. Visualizar diagramas:
- Os arquivos `.png` serão gerados automaticamente
- Use qualquer visualizador de imagens para abrir os arquivos
- Alternativa online: https://dreampuf.github.io/GraphvizOnline/

## 📊 Modelagem Proposta

### Tabelas Principais

#### `servidores_ativos`
**Informações essenciais dos servidores ativos (sem duplicação):**
- **id** (PK) - Identificador único
- **masp** (UK) - Matrícula do servidor (único)
- **nome_completo** - Nome completo do servidor
- **cpf** (UK) - CPF do servidor (único)
- **data_nascimento** - Data de nascimento
- **email_institucional** - Email institucional

#### `servidores_historico`
**Histórico de movimentações dos servidores:**
- **id** (PK) - Identificador único
- **servidor_id** (FK) - Referência ao servidor
- **data_ingresso** - Data de ingresso no período
- **data_saida** - Data de saída do período
- **observacoes** - Observações sobre o período

## 🎯 Regras de Negócio

1. **Unicidade:** CPF e MASP devem ser únicos na tabela de servidores ativos
2. **Histórico:** Todas as movimentações são registradas com datas de início e fim
3. **Integridade:** Relacionamento garantem consistência dos dados
4. **Simplicidade:** Estrutura focada apenas nas informações essenciais
5. **Sem Duplicação:** Informações temporais ficam apenas na tabela de histórico

## 📈 Vantagens da Modelagem Simplificada

1. **Facilidade de manutenção:** Menos tabelas e relacionamentos
2. **Performance:** Consultas mais simples e rápidas
3. **Clareza:** Estrutura fácil de entender e implementar
4. **Flexibilidade:** Fácil extensão futura se necessário
5. **Sem Redundância:** Eliminação de duplicação de informações

## 🔍 **Principais Melhorias:**

### **Antes (com duplicação):**
- `data_ingresso` aparecia em **ambas** as tabelas
- Informação redundante e propensa a inconsistências

### **Depois (sem duplicação):**
- `data_ingresso` aparece **apenas** na tabela de histórico
- Tabela de servidores ativos contém apenas informações **permanentes**
- Histórico contém todas as informações **temporais**

## 📊 **Lógica da Nova Estrutura:**

1. **`servidores_ativos`** = Informações **permanentes** do servidor
2. **`servidores_historico`** = Informações **temporais** (períodos de estadia)

### **Exemplo de Uso:**
- Para saber quando um servidor ingressou na SEPLAG: consultar `servidores_historico`
- Para saber se um servidor está ativo: verificar se existe registro em `servidores_ativos`
- Para histórico completo: juntar as duas tabelas via `servidor_id`

