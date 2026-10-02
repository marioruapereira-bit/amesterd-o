import streamlit as st

st.set_page_config(page_title="Roteiro Países Baixos", page_icon="🇳🇱", layout="centered")

st.title("🇳🇱 Roteiro Expresso: Países Baixos")
st.markdown("**6 a 8 de Outubro | Base: Amsterdam Centraal**")
st.caption("Check-in/Check-out obrigatório com cartão bancário/telemóvel (OVpay) nos transportes.")

# Botões de acesso rápido aos transportes
st.markdown("### 📱 Bilhetes e Horários")
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("🚆 Comboios NS", "https://www.ns.nl/en", use_container_width=True)
with col2:
    st.link_button("🚌 Autocarros", "https://9292.nl/en", use_container_width=True)
with col3:
    st.link_button("⛴️ Barco", "https://www.markenexpress.nl/en/", use_container_width=True)

st.divider()

# Navegação por dias
tab1, tab2, tab3 = st.tabs(["6 Out: Norte", "7 Out: Centro/Sul", "8 Out: Oeste"])

with tab1:
    st.header("Moinhos e Tradição Piscatória")
    st.markdown("**Logística:** Comboio + Autocarro + Barco")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Zaanse_Schans_Zuid.jpg/800px-Zaanse_Schans_Zuid.jpg", caption="Zaanse Schans")
    st.markdown("""
    * **11h00:** Partida da estação *Amsterdam Centraal*.
    * **11h15 – 11h35:** 🚆 Comboio **Sprinter** (dir. *Uitgeest*). Sair em **Zaandijk Zaanse Schans**.
    * **11h45 – 13h30:** 📍 Caminhada de 15 min e visita aos moinhos, fábrica de queijo e tamancos.
    * **13h30 – 14h20:** 🚆 Comboio **Sprinter** de regresso a *Amsterdam Centraal*. Subir ao terminal de autocarros (piso superior) e apanhar o **Autocarro 316** (EBS). Sair em **Volendam Centrum**.
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Volendam_-_haven_-_2009.jpg/800px-Volendam_-_haven_-_2009.jpg", caption="Porto de Volendam")
    st.markdown("""
    * **14h20 – 16h15:** 📍 Almoço rápido nas bancas do porto (Kibbeling ou arenque cru).
    * **16h15 – 16h45:** ⛴️ Embarcar no **Marken Express** (bilhetes no quiosque do porto). Travessia de 30 minutos.
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Marken_-_Haven_1.jpg/800px-Marken_-_Haven_1.jpg", caption="Casas tradicionais de Marken")
    st.markdown("""
    * **16h45 – 18h00:** 📍 Visita a pé à ilha de Marken (casas de madeira verdes).
    * **18h00 – 18h45:** 🚌 Apanhar **Autocarro 315** (paragem *Minneweg*), trocar para o **Metro 52** na estação *Amsterdam Noord*, até *Amsterdam Centraal*.
    """)

with tab2:
    st.header("O Centro e o Extremo Sul")
    st.markdown("**Logística:** Apenas Comboios Intercity (viagens longas)")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Oudegracht_Utrecht.jpg/800px-Oudegracht_Utrecht.jpg", caption="Oudegracht em Utrecht")
    st.markdown("""
    * **08h30:** Partida de *Amsterdam Centraal*.
    * **08h40 – 09h07:** 🚆 Comboio **Intercity** (dir. *Maastricht* ou *Heerlen*). Sair em **Utrecht Centraal**.
    * **09h15 – 12h30:** 📍 Caminhada pelo centro e base da Torre Dom.
    * **12h30 – 13h30:** 📍 Almoço nas esplanadas das caves (*werfkelders*) ao nível da água no **Oudegracht**.
    * **13h38 – 15h32:** 🚆 Voltar a *Utrecht Centraal*. Comboio **Intercity** direto para **Maastricht** (1h54 min).
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Vrijthof_Maastricht.jpg/800px-Vrijthof_Maastricht.jpg", caption="Praça Vrijthof em Maastricht")
    st.markdown("""
    * **15h40 – 19h00:** 📍 Visita à praça **Vrijthof**, livraria dominicana e prova de vinho local.
    * **19h00 – 21h30:** 🚆 Comboio **Intercity** direto de regresso a *Amsterdam Centraal* (2h25 min).
    """)

with tab3:
    st.header("As Cidades de Ouro e Regresso")
    st.markdown("**Logística:** Apenas Comboios Intercity + Gestão de Bagagem")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Haarlem_Grote_Markt_Bavo.jpg/800px-Haarlem_Grote_Markt_Bavo.jpg", caption="Grote Markt em Haarlem")
    st.markdown("""
    * **08h30:** 🧳 Check-out. Deixar as malas nos cacifos da estação *Amsterdam Centraal*.
    * **09h05 – 09h20:** 🚆 Comboio **Intercity** (dir. *Haarlem* ou *Zandvoort*). 15 min de viagem.
    * **09h25 – 12h30:** 📍 Caminhada até à **Grote Markt**, Igreja de São Bavão e *Gouden Straatjes*.
    * **12h30 – 13h10:** 🚆 Em Haarlem, comboio **Intercity** (dir. *Den Haag* ou *Rotterdam*). Sair em **Delft**.
    """)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Delft_canal_view.jpg/800px-Delft_canal_view.jpg", caption="Canais de Delft")
    st.markdown("""
    * **13h15 – 14h30:** 📍 Almoço na Praça do Mercado.
    * **14h30 – 17h00:** 📍 Visita ao canal *Oude Delft*, olarias históricas e Nieuwe Kerk.
    * **17h00 – 18h15:** 🚆 Comboio **Intercity** de Delft para *Amsterdam Centraal* (55 min). Recolha das malas nos cacifos, seguida de comboio para o Aeroporto de Schiphol (15 min).
    * **18h30:** 🛫 Chegada a Schiphol. Check-in e embarque no voo KL 1587.
    """)
