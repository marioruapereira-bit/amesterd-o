import streamlit as st
import requests
from io import BytesIO

st.set_page_config(page_title="Roteiro Países Baixos", page_icon="🇳🇱", layout="centered")

# --- FUNÇÃO METEOROLOGIA ---
@st.cache_data(ttl=3600)
def get_weather(date_str):
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.3676&longitude=4.9041&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Europe%2FAmsterdam"
        resp = requests.get(url).json()
        dates = resp['daily']['time']
        
        if date_str in dates:
            idx = dates.index(date_str)
            max_t = resp['daily']['temperature_2m_max'][idx]
            min_t = resp['daily']['temperature_2m_min'][idx]
            rain = resp['daily']['precipitation_probability_max'][idx]
            code = resp['daily']['weathercode'][idx]
            
            weather_map = {
                0: "☀️ Limpo", 1: "🌤️ Parcialmente nublado", 2: "⛅ Nublado", 3: "☁️ Muito nublado",
                45: "🌫️ Nevoeiro", 48: "🌫️ Nevoeiro gelado",
                51: "🌧️ Chuvisco", 53: "🌧️ Chuvisco moderado", 55: "🌧️ Chuvisco forte",
                61: "🌧 Chuva leve", 63: "🌧️ Chuva", 65: "🌧️ Chuva forte",
                80: "🌦️ Aguaceiros", 81: "🌦️ Aguaceiros fortes", 95: "⛈️ Trovoada"
            }
            desc = weather_map.get(code, "🌈 Variável")
            return f"**Meteorologia:** {desc} | 🌡️ {min_t}°C a {max_t}°C | ☔ Chuva: {rain}%"
        else:
            return "🌦️ Previsão meteorológica ainda não disponível."
    except Exception:
        return "🌦️ Erro ao carregar meteorologia."


# --- FUNÇÃO IMAGENS (À prova de bloqueios) ---
@st.cache_data(show_spinner=False)
def render_image(url, caption):
    try:
        # Disfarça o pedido como se fosse um navegador real para contornar a segurança da Wikipedia
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        resposta = requests.get(url, headers=headers, timeout=5)
        if resposta.status_code == 200:
            st.image(BytesIO(resposta.content), caption=caption, use_column_width=True)
    except Exception:
        pass


# --- CABEÇALHO ---
st.title("🇳🇱 Roteiro Expresso: Países Baixos")
st.markdown("**6 a 8 de Outubro | Mário e Maria João**")
st.caption("Base: Amsterdam Centraal | Check-in/out obrigatório nos transportes (OVpay).")

st.markdown("### 📱 Bilhetes e Horários")
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("🚆 Comboios NS", "https://www.ns.nl/en", use_container_width=True)
with col2:
    st.link_button("🚌 Autocarros", "https://9292.nl/en", use_container_width=True)
with col3:
    st.link_button("⛴️ Barco", "https://www.markenexpress.nl/en/", use_container_width=True)

st.divider()


# --- DIAS ---
tab1, tab2, tab3 = st.tabs(["6 Out: Norte", "7 Out: Centro/Sul", "8 Out: Oeste"])

with tab1:
    st.header("Moinhos e Tradição Piscatória")
    st.info(get_weather("2026-10-06"))
    st.markdown("**Logística:** Comboio + Autocarro + Barco")
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Zaanse_Schans_Zuid.jpg/800px-Zaanse_Schans_Zuid.jpg", "Moinhos no rio Zaan")
    st.markdown("""
    ### Zaanse Schans
    * **11h00:** Partida de *Amsterdam Centraal*.
    * **11h15 – 11h35:** 🚆 **Sprinter** (dir. *Uitgeest*). Sair em **Zaandijk Zaanse Schans**.
    * **11h45 – 13h30 | O que fazer:** 
        * Caminhar ao longo do rio Zaan para ver os 8 moinhos de vento históricos.
        * Entrar na **Catharina Hoeve**, uma réplica de uma quinta do séc. XVII, para ver como é feito o queijo Gouda e fazer provas gratuitas.
        * Passar na oficina de tamancos (**Kooijman**) para ver uma demonstração ao vivo.
    * **13h30 – 14h20:** 🚆 Regresso a *Amsterdam Centraal*. Subir ao terminal de autocarros e apanhar o **Autocarro 316** (EBS). Sair em **Volendam Centrum**.
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Volendam_-_haven_-_2009.jpg/800px-Volendam_-_haven_-_2009.jpg", "Porto de Volendam")
    st.markdown("""
    ### Volendam
    * **14h20 – 16h15 | O que fazer (Almoço):** 
        * Caminhar pela **De Dijk**, a animada rua principal no topo do dique.
        * Procurem uma banca de rua (*Vishandel*). Peçam **Kibbeling** (lascas de peixe fritas com molho de alho) e um **Haring** (arenque cru com cebola e pickles).
    * **16h15 – 16h45:** ⛴️ Embarcar no **Marken Express** (travessia de 30 min).
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Marken_-_Haven_1.jpg/800px-Marken_-_Haven_1.jpg", "Casas de madeira verdes em Marken")
    st.markdown("""
    ### Marken
    * **16h45 – 18h00 | O que fazer:** 
        * Percorram as ruelas estreitas (os *werven*) para ver as autênticas casas de madeira pintadas de verde escuro, construídas sobre estacas para resistirem às inundações.
    * **18h00 – 18h45:** 🚌 Apanhar **Autocarro 315** (paragem *Minneweg*), trocar para o **Metro 52** na estação *Amsterdam Noord*, até *Amsterdam Centraal*.
    """)

with tab2:
    st.header("O Centro e o Extremo Sul")
    st.info(get_weather("2026-10-07"))
    st.markdown("**Logística:** Apenas Comboios Intercity (viagens longas)")
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Oudegracht_Utrecht.jpg/800px-Oudegracht_Utrecht.jpg", "Oudegracht (Canal Velho)")
    st.markdown("""
    ### Utrecht
    * **08h30:** Partida de *Amsterdam Centraal*.
    * **08h40 – 09h07:** 🚆 **Intercity** (dir. *Maastricht* ou *Heerlen*). Sair em **Utrecht Centraal**.
    * **09h15 – 13h30 | O que fazer:** 
        * Caminhem ao longo do **Oudegracht**. Utrecht é famosa pelos **werfkelders**: antigas caves ao nível da água do canal.
        * Vão até à base da monumental **Torre Dom**.
        * **12h30:** Almocem numa das esplanadas em baixo, ao nível dos canais.
    * **13h38 – 15h32:** 🚆 Voltar a *Utrecht Centraal*. Comboio **Intercity** direto para **Maastricht** (1h54 min).
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Vrijthof_Maastricht.jpg/800px-Vrijthof_Maastricht.jpg", "Praça Vrijthof em Maastricht")
    st.markdown("""
    ### Maastricht
    * **15h40 – 19h00 | O que fazer:** 
        * Caminhem até à imensa **Praça Vrijthof**, rodeada de igrejas e esplanadas.
        * Entrem na **Boekhandel Dominicanen**, uma livraria impressionante instalada dentro de uma igreja gótica do século XIII.
        * **17h30 (Vinho local):** Sentem-se numa esplanada clássica e peçam um copo de **Apostelhoeve**, a vinha holandesa mais prestigiada da região.
    * **19h00 – 21h30:** 🚆 Comboio **Intercity** direto de regresso a *Amsterdam Centraal* (2h25 min).
    """)

with tab3:
    st.header("As Cidades de Ouro e Regresso")
    st.info(get_weather("2026-10-08"))
    st.markdown("**Logística:** Apenas Comboios Intercity + Gestão de Bagagem")
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Haarlem_Grote_Markt_Bavo.jpg/800px-Haarlem_Grote_Markt_Bavo.jpg", "Praça Grote Markt em Haarlem")
    st.markdown("""
    ### Haarlem
    * **08h30:** 🧳 **Check-out.** Deixar as malas nos cacifos automáticos da estação *Amsterdam Centraal*.
    * **09h05 – 09h20:** 🚆 **Intercity** (dir. *Haarlem* ou *Zandvoort*). 15 min de viagem.
    * **09h25 – 12h30 | O que fazer:** 
        * Vão à **Grote Markt** para admirar a imponente Igreja de São Bavão.
        * Caminhem pelas **Gouden Straatjes** (as "ruas douradas"), ideais para compras independentes.
    * **12h30 – 13h10:** 🚆 Em Haarlem, comboio **Intercity** (dir. *Den Haag* ou *Rotterdam*). Sair em **Delft**.
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Delft_canal_view.jpg/800px-Delft_canal_view.jpg", "Canais em Delft")
    st.markdown("""
    ### Delft
    * **13h15 – 17h00 | O que fazer:** 
        * Almocem na histórica **Praça do Mercado**.
        * Visitem a **Nieuwe Kerk**, onde estão os túmulos da família real holandesa.
        * Percorram o sereno canal **Oude Delft** e entrem numa loja histórica para ver a autêntica cerâmica **Delft Blue** pintada à mão.
    * **17h00 – 18h15:** 🚆 Comboio **Intercity** de Delft para *Amsterdam Centraal* (55 min). 
    * **18h15 – 18h30 | Aeroporto:** Recolha das malas nos cacifos da estação, seguida de comboio para o Aeroporto de **Schiphol** (15 min de viagem).
    * **18h45:** 🛫 Chegada a Schiphol. Check-in tranquilo para o voo KL 1587 às 20h50.
    """)
