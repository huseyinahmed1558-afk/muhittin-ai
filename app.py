import streamlit as st

st.set_page_config(
    page_title="Muhittin AI & Futbol Quiz", page_icon="⚽", layout="centered"
)

# Sol Yan Menü (Sayfa Seçimi)
st.sidebar.title("📌 Menü")
secim = st.sidebar.radio(
    "Gitmek istediğiniz sayfayı seçin:",
    ["🤖 Muhittin AI", "⚽ Futbol Bilgi Yarışması"],
)

# ---------------------------------------------------------
# SAYFA 1: MUHİTTİN AI SOHBET BOTU
# ---------------------------------------------------------
if secim == "🤖 Muhittin AI":
    st.title("🦅 Muhittin AI")
    st.caption("Kurucusu Hüseyin Tarafından Geliştirilen Yapay Zeka Asistanı")

    # Sohbet Geçmişi Hafızası
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Merhaba Hüseyin kurucum! Ben Muhittin. Sana nasıl yardımcı olabilirim?",
            }
        ]

    # Eski Mesajları Ekrana Yazdırma
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Kullanıcıdan Mesaj Alma
    if prompt := st.chat_input("Muhittin'e bir şeyler yaz..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Muhittin'in Basit Cevap Mantığı
        cevap = "Seni anlıyorum! Ben Hüseyin'in geliştirdiği Muhittin AI. Başka nasıl yardımcı olabilirim?"
        if "merhaba" in prompt.lower() or "selam" in prompt.lower():
            cevap = "Selam! Neler yapıyorsun?"
        elif "beşiktaş" in prompt.lower():
            cevap = "Şanlı Beşiktaş! 🦅 Siyah-Beyaz!"
        elif "kimsin" in prompt.lower():
            cevap = "Ben Muhittin AI! Hüseyin tarafından kodlandım."

        st.session_state.messages.append({"role": "assistant", "content": cevap})
        st.chat_message("assistant").write(cevap)

# ---------------------------------------------------------
# SAYFA 2: FUTBOL BİLGİ YARIŞMASI
# ---------------------------------------------------------
elif secim == "⚽ Futbol Bilgi Yarışması":
    st.title("⚽ Futbol Bilgi Yarışması")
    st.write("Futbol bilgisini test et, en yüksek skoru yap!")

    sorular = [
        {
            "soru": "Beşiktaş'ın namağlup şampiyon olduğu tarihi sezon hangisidir?",
            "secenekler": ["1990-1991", "1991-1992", "2015-2016", "2020-2021"],
            "cevap": "1991-1992",
        },
        {
            "soru": "UEFA Şampiyonlar Ligi tarihinin en çok gol atan oyuncusu kimdir?",
            "secenekler": [
                "Lionel Messi",
                "Cristiano Ronaldo",
                "Robert Lewandowski",
                "Karim Benzema",
            ],
            "cevap": "Cristiano Ronaldo",
        },
        {
            "soru": "Süper Lig tarihinde bir sezonda en çok gol atan yabancı futbolcu kimdir?",
            "secenekler": [
                "Alex de Souza",
                "Mario Gomez",
                "MBaye Diagne",
                "Bafétimbi Gomis",
            ],
            "cevap": "MBaye Diagne",
        },
        {
            "soru": "2022 Dünya Kupası'nı kazanan ülke hangisidir?",
            "secenekler": ["Fransa", "Brezilya", "Arjantin", "İngiltere"],
            "cevap": "Arjantin",
        },
        {
            "soru": "Süper Lig'de '100'ler Kulübü'ne giren ilk yabancı futbolcu kimdir?",
            "secenekler": [
                "Alex de Souza",
                "Gheorghe Hagi",
                "Shota Arveladze",
                "Mert Nobre",
            ],
            "cevap": "Alex de Souza",
        },
    ]

    if "skor" not in st.session_state:
        st.session_state.skor = 0
    if "soru_index" not in st.session_state:
        st.session_state.soru_index = 0
    if "bitti" not in st.session_state:
        st.session_state.bitti = False

    if not st.session_state.bitti:
        mevcut = sorular[st.session_state.soru_index]
        st.subheader(
            f"Soru {st.session_state.soru_index + 1} / {len(sorular)}"
        )
        st.write(f"**{mevcut['soru']}**")

        for secenek in mevcut["secenekler"]:
            if st.button(secenek, key=secenek):
                if secenek == mevcut["cevap"]:
                    st.success("Tebrikler, Doğru Cevap! 🎉")
                    st.session_state.skor += 20
                else:
                    st.error(f"Yanlış! Doğru cevap: {mevcut['cevap']}")

                if st.session_state.soru_index + 1 < len(sorular):
                    st.session_state.soru_index += 1
                    st.rerun()
                else:
                    st.session_state.bitti = True
                    st.rerun()
    else:
        st.balloons()
        st.header("🏆 Yarışma Bitti!")
        st.write(f"Toplam Skorun: **{st.session_state.skor} / 100**")

        if st.session_state.skor == 100:
            st.success("İnanılmaz! Tam bir futbol profesörüsün!")
        elif st.session_state.skor >= 60:
            st.info("Gayet iyi bir performans!")
        else:
            st.warning("Biraz daha futbol izlemen lazım!")

        if st.button("Tekrar Oyna 🔄"):
            st.session_state.skor = 0
            st.session_state.soru_index = 0
            st.session_state.bitti = False
            st.rerun()
