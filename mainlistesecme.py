from flask import Flask
import random
import string
app = Flask(__name__)
facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]
# Şifre Oluşturucunun komudu
length = 12  # Şifrenin uzunluğu
karakter = string.ascii_letters + string.digits + string.punctuation
sifre = ''.join(random.choice(karakter) for i in range(length))

# İlk açıldığındaki ana sayfa
@app.route("/")
def index():
    return f'<h1>MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1>'
# Rastgele Gerçek rotası
@app.route("/rastgele_gercek")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

# Şifre oluşturucunun rotası
@app.route("/sifre-olustur")
def generate_password():
    return f'<p>Oluşturulan Şifre: <b>{sifre}</b></p>'

if __name__ == "__main__":
    app.run(debug=True)
