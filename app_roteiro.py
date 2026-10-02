import streamlit as st
import requests

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
                45: "🌫️️ Nevoeiro", 48: "🌫️ Nevoeiro gelado",
                51: "🌧️ Chuvisco", 53: "🌧️️ Chuvisco moderado", 55: "🌧️ Chuvisco forte",
                61: "🌧 Chuva leve", 63: "🌧️️ Chuva", 65: "🌧️ Chuva forte",
                80: "🌦 Aguaceiros", 81: "🌦️ Aguaceiros fortes", 95: "⛈️ Trovoada"
            }
            desc = weather_map.get(code, "🌈 Variável")
            return f"**Meteorologia:** {desc} | 🌡️ {min_t}°C a {max_t}°C | ☔ Chuva: {rain}%"
        else:
            return "🌦️ Previsão meteorológica indisponível."
    except Exception:
        return "🌦️ Erro ao carregar meteorologia."


# --- FUNÇÃO IMAGENS ---
def render_image(url, caption):
    st.markdown(f'''
        <div style="text-align: center;">
            <img src="{url}" style="width:100%; border-radius: 8px;" referrerpolicy="no-referrer">
            <p style="font-size: 0.8em; color: gray; margin-top: 5px;">{caption}</p>
        </div>
        <br>
    ''', unsafe_allow_html=True)


# --- CABEÇALHO ---
st.title("🇳🇱 Roteiro Expresso: Países Baixos")
st.markdown("**5 a 8 de Outubro | Mário Pereira e Elvira Carlota**")
st.caption("Check-in/out obrigatório nos transportes públicos com cartão bancário (OVpay).")

st.markdown("### 📱 Bilhetes e Horários")
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("🚆 Comboios NS", "https://www.ns.nl/en", use_container_width=True)
with col2:
    st.link_button("🚌 Autocarros", "https://9292.nl/en", use_container_width=True)
with col3:
    st.link_button("⛴️ Barco", "https://www.markenexpress.nl/en/", use_container_width=True)

st.divider()


# --- DIAS E LOGÍSTICA ---
tab0, tab1, tab2, tab3 = st.tabs(["✈️ Voos & Hotel", "6 Out: Norte", "7 Out: Centro/Sul", "8 Out: Oeste"])

with tab0:
    st.header("Informações Logísticas")
    st.markdown("""
    ### 🏨 Alojamento (5 a 8 Out)
    **[Clayton Hotel Amsterdam American](https://maps.google.com/?q=Clayton+Hotel+Amsterdam+American)**
    * **Morada:** Leidsekade 97, Amsterdam
    * **Regime:** Pequeno-almoço incluído
    
    ### 🛫 Voos e Transferes
    **Dia 5 de Outubro (Ida)**
    * ✈️ **Voo TP 674:** LIS 18h15 ➔ AMS 22h20
    * 🚘 **Transfer (22h20):** Do Aeroporto para o Hotel. *Ponto de Encontro: Subir ao Piso 3 (Partidas), sair pela Porta C e aguardar na passadeira no exterior pelo motorista com a placa.*
    """)
    st.link_button("Ver Estado do Voo TP 674", "https://www.google.com/search?q=TP+674+flight+status")
    
    st.markdown("""
    **Dia 8 de Outubro (Regresso)**
    * 🚘 **Transfer (17h28):** Do Hotel para o Aeroporto. *Aguardar no lobby do hotel com a bagagem às 17h15.*
    * ✈️ **Voo KL 1587:** AMS 20h50 ➔ LIS 22h50
    """)
    st.link_button("Ver Estado do Voo KL 1587", "https://www.google.com/search?q=KL+1587+flight+status")

with tab1:
    st.header("Evento, Moinhos e Tradição")
    st.info(get_weather("2026-10-06"))
    st.markdown("**Logística:** Elétrico + Comboio + Autocarro + Barco")
    
    st.markdown("""
    ### Manhã: Conferência
    * **08h30:** Pequeno-almoço no **[Clayton Hotel](https://maps.google.com/?q=Clayton+Hotel+Amsterdam+American)**.
    * **09h00:** Deslocação do hotel para o local do evento (*Sustainability Week Europe*).
    * **10h30:** Deslocação do local do evento para a estação **[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)** para iniciar o roteiro turístico.
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Zaanse_Schans_Zuid.jpg/800px-Zaanse_Schans_Zuid.jpg", "Moinhos no rio Zaan")
    st.markdown("""
    ### [Zaanse Schans](https://maps.google.com/?q=Zaanse+Schans)
    * **11h00:** Partida de *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)*.
    * **11h15 – 11h35:** 🚆 **Sprinter** (dir. *Uitgeest*). Sair na estação **[Zaandijk Zaanse Schans](https://maps.google.com/?q=Zaandijk+Zaanse+Schans+station)**.
    * **11h45 – 13h30 | O que fazer:** 
        * Caminhar ao longo do rio para ver os 8 moinhos de vento históricos.
        * Entrar na **[Catharina Hoeve](https://maps.google.com/?q=Catharina+Hoeve+Cheese+Farm)** para ver como é feito o queijo Gouda (provas gratuitas).
        * Oficina de tamancos (**[Kooijman](https://maps.google.com/?q=Kooijman+Souvenirs+%26+Clogs+Wooden+Shoe+Workshop)**).
    * **13h30 – 14h20:** 🚆 Regresso a *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)*. Subir ao terminal de autocarros e apanhar o **Autocarro 316** (EBS). Sair em **[Volendam Centrum](https://maps.google.com/?q=Volendam+Centrum)**.
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Volendam_-_haven_-_2009.jpg/800px-Volendam_-_haven_-_2009.jpg", "Porto de Volendam")
    st.markdown("""
    ### [Volendam](https://maps.google.com/?q=Volendam)
    * **14h20 – 16h15 | O que fazer (Almoço):** 
        * Caminhar pela rua principal **[De Dijk](https://maps.google.com/?q=De+Dijk,+Volendam)**.
        * Procurem uma banca de rua (*Vishandel*). Peçam **Kibbeling** (lascas de peixe fritas com molho de alho) e um **Haring** (arenque cru com cebola e pickles).
    * **16h15 – 16h45:** ⛴️ Embarcar no **[Marken Express](https://maps.google.com/?q=Marken+Express+Volendam)** (travessia de 30 min).
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Marken_-_Haven_1.jpg/800px-Marken_-_Haven_1.jpg", "Casas de madeira verdes em Marken")
    st.markdown("""
    ### [Marken](https://maps.google.com/?q=Marken,+Netherlands)
    * **16h45 – 18h00 | O que fazer:** 
        * Percorram as ruelas estreitas (os *werven*) para ver as autênticas casas de madeira pintadas de verde escuro sobre estacas.
    * **18h00 – 18h45:** 🚌 Apanhar **Autocarro 315** (paragem **[Minneweg](https://maps.google.com/?q=Minneweg,+Marken)**), trocar para o **Metro 52** na estação **[Amsterdam Noord](https://maps.google.com/?q=Station+Noord,+Amsterdam)**, até *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)*.
    """)

with tab2:
    st.header("O Centro e o Extremo Sul")
    st.info(get_weather("2026-10-07"))
    st.markdown("**Logística:** Apenas Comboios Intercity (viagens longas)")
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Oudegracht_Utrecht.jpg/800px-Oudegracht_Utrecht.jpg", "Oudegracht (Canal Velho)")
    st.markdown("""
    ### [Utrecht](https://maps.google.com/?q=Utrecht)
    * **08h30:** Apanhar o elétrico do Hotel até *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)*.
    * **08h40 – 09h07:** 🚆 **Intercity** (dir. *Maastricht* ou *Heerlen*). Sair na estação **[Utrecht Centraal](https://maps.google.com/?q=Utrecht+Centraal)**.
    * **09h15 – 13h30 | O que fazer:** 
        * Caminhem ao longo do **[Oudegracht](https://maps.google.com/?q=Oudegracht,+Utrecht)** para verem os passadiços e esplanadas ao nível da água.
        * Vão até à base da monumental **[Torre Dom](https://maps.google.com/?q=Dom+Tower,+Utrecht)**.
        * **12h30:** Almocem numa das esplanadas em baixo, nos canais.
    * **13h38 – 15h32:** 🚆 Voltar a *[Utrecht Centraal](https://maps.google.com/?q=Utrecht+Centraal)*. Comboio **Intercity** direto para a estação de **[Maastricht](https://maps.google.com/?q=Maastricht+Station)** (1h54 min).
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Vrijthof_Maastricht.jpg/800px-Vrijthof_Maastricht.jpg", "Praça Vrijthof em Maastricht")
    st.markdown("""
    ### [Maastricht](https://maps.google.com/?q=Maastricht)
    * **15h40 – 19h00 | O que fazer:** 
        * Caminhem até à imensa **[Praça Vrijthof](https://maps.google.com/?q=Vrijthof,+Maastricht)**.
        * Entrem na **[Boekhandel Dominicanen](https://maps.google.com/?q=Boekhandel+Dominicanen,+Maastricht)**, uma livraria impressionante instalada dentro de uma igreja gótica.
    * **17h30 (Vinho local):** Sentem-se numa esplanada clássica e peçam um copo de **[Apostelhoeve](https://maps.google.com/?q=Wijndomein+Apostelhoeve,+Maastricht)**.
    * **19h00 – 21h30:** 🚆 Comboio **Intercity** direto de *[Maastricht Station](https://maps.google.com/?q=Maastricht+Station)* de regresso a *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)*.
    """)

with tab3:
    st.header("As Cidades de Ouro e Regresso")
    st.info(get_weather("2026-10-08"))
    st.markdown("**Logística:** AVISO - O transfer para o aeroporto sai do Hotel.")
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Haarlem_Grote_Markt_Bavo.jpg/800px-Haarlem_Grote_Markt_Bavo.jpg", "Praça Grote Markt em Haarlem")
    st.markdown("""
    ### [Haarlem](https://maps.google.com/?q=Haarlem)
    * **08h30:** 🧳 **Check-out.** Deixar as malas guardadas na receção do **[Clayton Hotel](https://maps.google.com/?q=Clayton+Hotel+Amsterdam+American)** (Não as levem para a estação).
    * **09h00:** Elétrico do Hotel para *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)*.
    * **09h20 – 09h35:** 🚆 **Intercity** (dir. *Haarlem* ou *Zandvoort*) até **[Haarlem Station](https://maps.google.com/?q=Haarlem+Station)**.
    * **09h40 – 12h30 | O que fazer:** 
        * Vão à **[Grote Markt](https://maps.google.com/?q=Grote+Markt,+Haarlem)** para admirar a imponente **[Igreja de São Bavão](https://maps.google.com/?q=Grote+of+St.-Bavokerk,+Haarlem)**.
        * Caminhem pelas **[Gouden Straatjes](https://maps.google.com/?q=Gouden+Straatjes,+Haarlem)** (as "ruas douradas").
    * **12h30 – 13h10:** 🚆 Em *[Haarlem Station](https://maps.google.com/?q=Haarlem+Station)*, comboio **Intercity** (dir. *Den Haag* ou *Rotterdam*). Sair na estação de **[Delft](https://maps.google.com/?q=Delft+Station)**.
    """)
    
    render_image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Delft_canal_view.jpg/800px-Delft_canal_view.jpg", "Canais em Delft")
    st.markdown("""
    ### [Delft](https://maps.google.com/?q=Delft)
    * **13h15 – 15h45 | O que fazer:** 
        * Almocem na histórica **[Praça do Mercado (Markt)](https://maps.google.com/?q=Markt,+Delft)**.
        * Visitem a **[Nieuwe Kerk](https://maps.google.com/?q=Nieuwe+Kerk,+Delft)**.
        * Percorram o canal **[Oude Delft](https://maps.google.com/?q=Oude+Delft,+Delft)** e vejam a cerâmica **Delft Blue**.
    * **15h45 – 16h40:** 🚆 Comboio **Intercity** de *[Delft Station](https://maps.google.com/?q=Delft+Station)* de regresso a *[Amsterdam Centraal](https://maps.google.com/?q=Amsterdam+Centraal)* (55 min). 
    * **16h45 – 17h10:** Apanhar o elétrico (Linha 2 ou 12) de regresso ao **[Clayton Hotel](https://maps.google.com/?q=Clayton+Hotel+Amsterdam+American)**.
    * **17h15 | 🧳 Recolha de Bagagem:** Pedir as malas na receção e aguardar no lobby.
    * **17h28 | 🚘 Transfer:** Partida do transfer privado do Hotel para o Aeroporto de **[Schiphol](https://maps.google.com/?q=Amsterdam+Airport+Schiphol)**.
    * **18h15:** 🛫 Chegada a *Schiphol* e check-in para o voo KL 1587.
    """)
