import streamlit as st

st.set_page_config(
    page_title="Vestibulares 2026 | Informações e Dicas",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Lato:wght@400;700&display=swap');

    html, body, .stApp { background-color: #f5fbff; font-family: 'Lato', sans-serif; }

    .main-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.1rem;
        font-weight: 800;
        color: #002561;
        text-align: center;
        padding: 1rem 0 0.2rem 0;
    }
    .main-subtitle {
        font-family: 'Lato', sans-serif;
        text-align: center;
        color: #008ED4;
        font-size: 1rem;
        margin-bottom: 1.2rem;
    }

    h2, h3 { font-family: 'Montserrat', sans-serif !important; color: #002561 !important; }
    h4 { font-family: 'Montserrat', sans-serif !important; color: #008ED4 !important; }

    hr { border: 1.5px solid #9DDCF9; margin: 1rem 0; }

    .badge {
        display: inline-block;
        background: #D4EFFC;
        color: #002561;
        border-radius: 20px;
        padding: 3px 14px;
        font-size: 0.82rem;
        font-weight: 700;
        font-family: 'Montserrat', sans-serif;
        margin: 2px 3px 2px 0;
    }
    .badge-gray { background: #f0f0f0; color: #888; }

    .dica-box {
        background: #fffde7;
        border-left: 4px solid #EBEA70;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin: 0.7rem 0;
        font-family: 'Lato', sans-serif;
        color: #002561;
    }

    .alert-box {
        background: #fff0f3;
        border-left: 4px solid #EE2D67;
        border-radius: 8px;
        padding: 0.9rem 1.2rem;
        margin: 0.5rem 0;
        font-size: 0.93rem;
        font-family: 'Lato', sans-serif;
        color: #002561;
    }

    [data-testid="stSidebar"] { background: #002561 !important; }
    [data-testid="stSidebar"] * { color: #D4EFFC !important; font-family: 'Lato', sans-serif !important; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
        color: #00BDF2 !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    .stSelectbox label { font-family: 'Montserrat', sans-serif; color: #002561 !important; font-weight: 600; }

    .stTabs [data-baseweb="tab"] { font-family: 'Montserrat', sans-serif; font-weight: 700; color: #008ED4; }
    .stTabs [aria-selected="true"] { color: #002561 !important; border-bottom: 3px solid #00BDF2 !important; }

    div[data-testid="stInfo"] {
        background-color: #D4EFFC;
        color: #002561;
        border-left-color: #00BDF2;
        font-family: 'Lato', sans-serif;
    }
    div[data-testid="stSuccess"] {
        background-color: #8EC6B2;
        color: #002561;
        border-left-color: #002561;
        font-family: 'Lato', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    try:
        st.image("logo_ismart.png", width=130)
    except Exception:
        pass
    st.markdown("<h2 style='font-family:Montserrat,sans-serif;color:#00BDF2;font-size:1.1rem;'>📚 Vestibulares 2026</h2>", unsafe_allow_html=True)
    st.markdown("---")
    pagina = st.radio(
        "Navegue pelas seções:",
        ["🎓 Vestibulares 2026", "📅 Vestibulares Meio de Ano 2026", "💡 Você sabia?"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("Dashboard com informações e dicas para os vestibulares de 2026.")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA 1 — VESTIBULARES 2026
# ════════════════════════════════════════════════════════════════════════════
if pagina == "🎓 Vestibulares 2026":

    st.markdown('<div class="main-title">🎓 Vestibulares 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione um vestibular para ver as informações completas</div>', unsafe_allow_html=True)
    st.markdown("---")

    vestibular = st.selectbox("Escolha o vestibular:", ["Selecione...", "ENEM", "FUVEST", "UNICAMP"], label_visibility="collapsed")

    def render_datas(dados):
        for item, data, gray in dados:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{item}**")
            with col2:
                cls = "badge badge-gray" if gray else "badge"
                st.markdown(f'<span class="{cls}">{data}</span>', unsafe_allow_html=True)
            st.markdown("")

    if vestibular == "ENEM":
        st.markdown("## 📝 ENEM")
        st.markdown("---")
        tab1, tab2, tab3 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "🌟 Dicas de Ouro"])

        with tab1:
            st.markdown("### 📅 Cronograma")
            render_datas([
                ("Período para solicitar isenção", "13 a 24/04", False),
                ("Resultado da isenção", "08/05", False),
                ("Inscrições", "A ser divulgado", True),
                ("1º dia de prova", "A ser divulgado", True),
                ("2º dia de prova", "A ser divulgado", True),
                ("Datas SISU", "A ser divulgado", True),
            ])

        with tab2:
            st.markdown("### ℹ️ Informações")
            st.markdown("#### 📌 Modelo TESTLETS")
            st.info("O ENEM adotou o modelo de **TESTLETS** — formato que utiliza um único texto, gráfico ou mapa base para um bloco de 2 a 5 perguntas em sequência.")
            st.markdown("#### Como isso me afeta?")
            st.markdown("""
- **Tenha calma!** Não se apresse e leia as questões isoladamente. Busque entender profundamente o texto base para responder às questões. Muitas vezes, a resposta da questão 2 pode depender da lógica aplicada na questão 1.
- **Mais interpretação, menos Decoreba!** O foco deixa de ser decoreba e virá capacidade de interpretar contextos, inferir sentidos e analisar informações de forma integrada. Este ano, até questões de Exatas contarão com enunciados elaborados pensando em situações-problema complexas.
""")
            st.markdown("#### 📝 Redação")
            st.markdown("""
Na redação, os corretores esperam **menos redações prontas**, que seguem a "fôrma" que cabe qualquer tema; e **mais redações autorais**, que utilizam repertório sociocultural autêntico.

**Como tudo isso me afeta:**
- Evite ser genérico! O elemento **Ação** virou o mais influente da competência 5.
- Haverá **maior rigor na competência 5** (proposta de intervenção), **menor exigência na competência 4** (conectivos interparágrafos) e **penalização para repertórios considerados "de bolso"**.
""")

        with tab3:
            st.markdown("### 🌟 Dicas de Ouro")
            st.markdown('<div class="dica-box">✅ Treine questões/simulados de instituições que já utilizam o TESTLET em seus processos (como UNESP e FUVEST).</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Estude relacionando as disciplinas: Quando estudar Biologia, relacione com Química e Física; Quando estudar História, relacione com Geografia e Física. É essa visão interdisciplinar que será cobrada.</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Procure se atentar ao contexto, conecte pontos e eixos temáticos de cada questão!</div>', unsafe_allow_html=True)

    elif vestibular == "FUVEST":
        st.markdown("## 🏛️ FUVEST")
        st.markdown("---")
        tab1, tab2, tab3, tab4 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "📚 Leituras Obrigatórias", "🌟 Dicas de Ouro"])

        with tab1:
            st.markdown("### 📅 Cronograma")
            st.markdown("🔗 **Site:** [fuvest.br](https://www.fuvest.br)")
            st.markdown("")
            render_datas([
                ("Período para solicitar isenção", "A ser divulgado", True),
                ("Inscrições", "17/08 a 09/10", False),
                ("1ª Fase", "15/11", False),
                ("2ª Fase — Dia 1", "13/12", False),
                ("2ª Fase — Dia 2", "14/12", False),
            ])

        with tab2:
            st.markdown("### ℹ️ Informações")
            st.info("Desde o ano passado a FUVEST vem adequando sua prova para um estilo **interdisciplinar**, onde as questões são menos diretas e passam a cobrar a conexão de conhecimentos.")
            st.info("Os candidatos ao Vestibular 2027 terão pela frente uma **1ª Fase com menos questões de múltipla escolha** — em vez das tradicionais 90, serão **80 questões**, mantido o tempo de prova (5h).")
            st.markdown("#### 📋 Formato")
            st.markdown("""
**1ª Fase (5h):** 80 questões de Artes, Biologia, Educação Física, Filosofia, Física, Geografia, História, Inglês, Matemática, Português, Química e Sociologia.

**2ª Fase:**
- **Dia 1 (4h):** 10 questões discursivas de Português e uma redação.
- **Dia 2 (4h):** 12 questões discursivas de disciplinas específicas de acordo com a carreira escolhida.
""")
            st.markdown("#### Como tudo isso me afeta?")
            st.markdown("""
- **Mais interpretação e raciocínio, menos Decoreba!** O foco deixa de ser decoreba e virá capacidade de conectar e analisar conhecimentos de diferentes áreas em uma mesma questão, interpretar e relacionar contextos.
- **Sociologia, Filosofia, Educação Física e Artes** ganham mais espaço e seus conhecimentos passam a ser cobrados com maior especificidade.
- A **redação** poderá cobrar diferentes gêneros textuais para além da dissertação. Poderão ser cobradas redações no estilo artigo de opinião, posts, carta, crônica, discurso, etc.
""")

        with tab3:
            st.markdown("### 📚 Lista de Leituras Obrigatórias")
            st.success("🎉 **Novidade histórica:** Lista de leituras obrigatórias **só com autoras mulheres** pela primeira vez na história da FUVEST!")
            for titulo, autora in [
                ("Opúsculo Humanitário (1853)", "Nísia Floresta"),
                ("Nebulosas (1872)", "Narcisa Amália"),
                ("Memórias de Martha (1899)", "Julia Lopes de Almeida"),
                ("Caminho de pedras (1937)", "Rachel de Queiroz"),
                ("A paixão segundo G.H. (1964)", "Clarice Lispector"),
                ("Geografia (1967)", "Sophia de Mello Breyner Andresen"),
                ("Balada de amor ao vento (1990)", "Paulina Chiziane"),
                ("Canção para ninar menino grande (2018)", "Conceição Evaristo"),
                ("A visão das plantas (2019)", "Djaimilia Pereira de Almeida"),
            ]:
                st.markdown(f"- **{titulo}** — *{autora}*")
            st.markdown("---")
            st.markdown("#### 🏛️ Aulas Gratuitas — Biblioteca Brasiliana Guita e José Mindlin")
            st.markdown("A Biblioteca Brasiliana Guita e José Mindlin promoverá aulas dedicadas às obras literárias exigidas no Vestibular FUVEST 2027. Os encontros exploram enredo, personagens e contexto histórico, sendo conduzidos por professores e pesquisadores universitários.")
            st.markdown('<div class="alert-box">⚠️ As aulas são gratuitas; no entanto, para participação presencial, é necessário realizar inscrição prévia.</div>', unsafe_allow_html=True)
            st.markdown('<div class="alert-box">⚠️ As transmissões ocorrem ao vivo pelo canal do <strong>@bbmusp</strong> no YouTube, onde as gravações permanecem disponíveis posteriormente. Para mais informações, acesse a bio do <strong>@bbmusp</strong>.</div>', unsafe_allow_html=True)

        with tab4:
            st.markdown("### 🌟 Dicas de Ouro")
            st.markdown('<div class="dica-box">✅ Treine questões/simulados de instituições que já utilizam o TESTLET em seus processos (como UNESP e UNICAMP).</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Estude relacionando as disciplinas: Quando estudar Biologia, relacione com Química e Física; Quando estudar História, relacione com Geografia e Física. É essa visão interdisciplinar que será cobrada.</div>', unsafe_allow_html=True)
            st.markdown('<div class="dica-box">✅ Procure se atentar ao contexto, conecte pontos e eixos temáticos de cada questão!</div>', unsafe_allow_html=True)

    elif vestibular == "UNICAMP":
        st.markdown("## 🔬 UNICAMP")
        st.markdown("---")
        tab1, tab2, tab3 = st.tabs(["📅 Cronograma", "ℹ️ Informações", "📚 Leituras Obrigatórias"])

        with tab1:
            st.markdown("### 📅 Cronograma")
            st.markdown("🔗 **Site:** [comvest.unicamp.br](http://comvest.unicamp.br)")
            st.markdown("")
            render_datas([
                ("Período para solicitar isenção", "11/05 a 05/06", False),
                ("Inscrições", "03 a 31/08", False),
                ("1ª Fase", "18/10", False),
                ("2ª Fase — Dia 1", "29/11", False),
                ("2ª Fase — Dia 2", "30/11", False),
            ])

        with tab2:
            st.markdown("### ℹ️ Informações")
            st.info("O vestibular da UNICAMP é famoso por ser bastante **crítico** e focar na **interdisciplinaridade** das áreas do conhecimento em detrimento da memorização e decoreba.")
            st.markdown("#### 📋 Formato")
            st.markdown("""
**1ª Fase (5h):** 72 questões de Português, Literatura, Matemática, Inglês, História, Geografia, Física, Química, Biologia, Filosofia e Sociologia.

**2ª Fase:** Redação e questões dissertativas divididas entre núcleo comum e específicas por área do curso escolhido (Exatas, Humanas ou Biológicas).
""")

        with tab3:
            st.markdown("### 📚 Lista de Leituras Obrigatórias")
            for titulo, autora in [
                ("Prosas seguidas de odes mínimas", "José Paulo Paes"),
                ("Olhos d'água", "Conceição Evaristo"),
                ("A vida não é útil", "Ailton Krenak"),
                ("Vida e morte de M.J. Gonzaga de Sá", "Lima Barreto"),
                ("No seu pescoço", "Chimamanda Ngozi Adichie"),
                ("Morangos mofados (Contos escolhidos*)", "Caio Fernando Abreu"),
                ("Memórias Póstumas de Brás Cubas", "Machado de Assis"),
                ("Canções escolhidas**", "Paulo César Pinheiro"),
                ("Os funerais da Mamãe Grande", "Gabriel García Márquez"),
            ]:
                st.markdown(f"- **{titulo}** — *{autora}*")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA 2 — VESTIBULARES MEIO DE ANO 2026
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "📅 Vestibulares Meio de Ano 2026":

    st.markdown('<div class="main-title">📅 Vestibulares Meio de Ano 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Selecione um vestibular para ver as informações completas</div>', unsafe_allow_html=True)
    st.markdown("---")

    vestibular_meio = st.selectbox(
        "Escolha o vestibular:",
        ["Selecione...", "UNESP 2026/2", "INSPER 2026/2", "MAUÁ 2026/2", "FGV 2026/2"],
        label_visibility="collapsed"
    )

    def render_cronograma(dados, site=None):
        if site:
            st.markdown(f"🔗 **Site:** [{site}](https://{site})")
            st.markdown("")
        for item, data, gray in dados:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{item}**")
            with col2:
                cls = "badge badge-gray" if gray else "badge"
                st.markdown(f'<span class="{cls}">{data}</span>', unsafe_allow_html=True)
            st.markdown("")

    if vestibular_meio == "UNESP 2026/2":
        st.markdown("## 🏫 UNESP 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Período para solicitar isenção e redução de 50% da taxa", "06 a 12/04", False),
            ("Inscrições (vestibular)", "13/04 a 05/05", False),
            ("1ª Fase", "24/05", False),
            ("2ª Fase — Dia 1", "20/06", False),
            ("2ª Fase — Dia 2", "21/06", False),
        ], site="vunesp.com.br")

    elif vestibular_meio == "INSPER 2026/2":
        st.markdown("## 🏦 INSPER 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Período para solicitar isenção (via Ismart)", "Em análise", True),
            ("Inscrições", "Até 13/05", False),
            ("Prova", "07/06", False),
        ], site="insper.edu.br")

    elif vestibular_meio == "MAUÁ 2026/2":
        st.markdown("## ⚙️ MAUÁ 2026/2")
        st.markdown("---")
        st.markdown("🔗 **Site:** [maua.br](https://www.maua.br)")
        st.markdown("")
        st.markdown("**Isenção:** Solicitada no processo de inscrição")
        st.markdown("")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🏢 Modalidade Presencial")
            st.markdown(f'<span class="badge">Até 17/06</span> Inscrições para prova presencial', unsafe_allow_html=True)
            st.markdown("")
            st.markdown(f'<span class="badge">21/06</span> Prova presencial', unsafe_allow_html=True)
        with col2:
            st.markdown("#### 💻 Modalidade Online")
            st.markdown(f'<span class="badge">Até 22/06</span> Inscrições para prova online', unsafe_allow_html=True)
            st.markdown("")
            st.markdown(f'<span class="badge">24/06</span> Prova online', unsafe_allow_html=True)

    elif vestibular_meio == "FGV 2026/2":
        st.markdown("## 📊 FGV 2026/2")
        st.markdown("---")
        render_cronograma([
            ("Período para solicitar isenção", "Até 20/04", False),
            ("Inscrições", "Até 27/04", False),
            ("Prova", "24/05", False),
        ], site="fgv.br")

# ════════════════════════════════════════════════════════════════════════════
# PÁGINA 3 — VOCÊ SABIA?
# ════════════════════════════════════════════════════════════════════════════
elif pagina == "💡 Você sabia?":

    st.markdown('<div class="main-title">💡 Você sabia?</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Dicas e recursos gratuitos para turbinar seus estudos</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### Provas Antigas e/ou simulados")
    st.markdown("Grande parte das universidades oferecem provas antigas e/ou simulados gratuitos e online em seus sites. Acesse os sites das instituições e aproveite!")
    st.markdown("Ao longo do ano, diversos cursinhos abrem inscrições para simulados abertos gratuitos nas modalidades presencial/online. Confira as oportunidades:")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("**Estratégia Vestibulares**")
            st.link_button("Acessar simulados", "https://vestibulares.estrategia.com/instituicao/cursos/simulados-gratuitos", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Etapa**")
            st.link_button("Acessar simulados", "https://etapa.com.br/home/apoio-ao-vestibulando/simulados", use_container_width=True)

    with col1:
        with st.container(border=True):
            st.markdown("**Objetivo**")
            st.link_button("Acessar simulados", "https://www.curso-objetivo.br/vestibular/simulados.aspx", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Poliedro**")
            st.markdown("O cursinho oferece simulados abertos ao longo do ano. Fique atento ao site.")
            st.markdown("Acesse também o **Poliedro Resolve**, ferramenta de correção e resolução de questões de vestibular através de vídeos explicativos e comentários de questões de provas feito por professores do Poliedro.")
            st.link_button("Acessar simulados", "https://cursopoliedro.com.br/", use_container_width=True)
            st.link_button("Acessar Poliedro Resolve", "https://poliedroresolve.sistemapoliedro.com.br/", use_container_width=True)

    with col1:
        with st.container(border=True):
            st.markdown("**Anglo**")
            st.markdown("O cursinho oferece simulados abertos ao longo do ano. Fique atento ao site.")
            st.link_button("Acessar simulados", "https://cursoanglo.com.br/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**CPV**")
            st.link_button("Acessar simulados", "https://cursinho.cpv.com.br/simulados-abertos-cpv", use_container_width=True)

    st.markdown("---")
    st.markdown("### 🏫 Outros cursinhos com simulados abertos")
    st.markdown("""
Outros cursinhos que oferecem simulados abertos presenciais/online:
- **Cursinho da Poli**
- **CUJA (UNIFESP)**
""")
