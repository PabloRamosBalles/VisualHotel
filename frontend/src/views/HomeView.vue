<template>
  <div class="home-page">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="nav-content">
        <div class="logo">VisualHotel</div>
        <button class="client-access" @click="openLogin">Acceso Clientes</button>
      </div>
    </nav>

    <!-- Hero Slider -->
    <section class="hero-slider">
      <div class="slide-container" :style="{ backgroundImage: 'url(' + slides[currentSlide].image + ')' }">
        <div class="overlay">
          <h1 class="hero-text">{{ slides[currentSlide].text }}</h1>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
      <h2 class="stats-title">Orgullosos de nuestro trabajo.</h2>
      <div class="stats-cards">
        <div class="stat-card">
          <i class="fas fa-home stat-icon" style="color:#ff4d79;"></i>
          <div>
            <div class="stat-value">+40.000</div>
            <div class="stat-label">Alojamientos</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-moon stat-icon" style="color:#ff4d79;"></i>
          <div>
            <div class="stat-value">+1 Millón</div>
            <div class="stat-label">Noches reservadas</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="fas fa-city stat-icon" style="color:#ff4d79;"></i>
          <div>
            <div class="stat-value">+40</div>
            <div class="stat-label">Ciudades</div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <!-- <section class="about-section">
      <h2>Sobre VisualHotel</h2>
      <p>
        VisualHotel es una plataforma moderna para gestionar reservas y habitaciones de manera eficiente y simple. Nuestro objetivo es digitalizar la experiencia hotelera para clientes y administradores por igual.
      </p>
    </section>
    <br> -->
    <section class="about-steps-section">
      <div class="about-steps-grid">
        <div class="about-step">
          <div class="about-step-number">1</div>
          <h3>Gestiona reservas</h3>
          <p>
            Visualiza y administra <strong>todas las reservas</strong> de tu hotel en un solo lugar, de forma clara y rápida.
          </p>
          <img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80" alt="Gestiona reservas" />
        </div>
        <div class="about-step">
          <div class="about-step-number">2</div>
          <h3>Controla habitaciones</h3>
          <p>
            <strong>Actualiza el estado</strong> de cada habitación y mantén el control de la ocupación en tiempo real.
          </p>
          <img src="https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=400&q=80" alt="Controla habitaciones" />
        </div>
        <div class="about-step">
          <div class="about-step-number">3</div>
          <h3>Registra huéspedes</h3>
          <p>
            <strong>Agrega y consulta información</strong> de huéspedes de manera rápida y segura, mejorando la atención.
          </p>
          <img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80" alt="Registra huéspedes" />
        </div>
        <div class="about-step">
          <div class="about-step-number">4</div>
          <h3>Personaliza tu panel</h3>
          <p>
            Disfruta de una <strong>herramienta adaptada</strong> a las necesidades de tu hotel y equipo de recepción.
          </p>
          <img src="https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?auto=format&fit=crop&w=400&q=80" alt="Personaliza tu panel" />
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <h2>Preguntas Frecuentes (FAQ)</h2>
      <div class="faq-items">
        <details>
          <summary>¿Cómo registro una nueva reserva?</summary>
          <p>Desde el panel principal, haz clic en “Crear reserva” y completa los datos del huésped y la habitación. La reserva se añadirá automáticamente al sistema.</p>
        </details>
        <details>
          <summary>¿Puedo cambiar el estado de una habitación?</summary>
          <p>Sí, puedes actualizar el estado de cualquier habitación (Disponible, Ocupada, Limpieza, etc.) desde la sección de habitaciones en tu panel.</p>
        </details>
        <details>
          <summary>¿Cómo consulto la información de un huésped?</summary>
          <p>En la sección de huéspedes puedes buscar y ver los datos de cada persona alojada, así como su historial de reservas.</p>
        </details>
        <details>
          <summary>¿Puedo personalizar el panel para mi hotel?</summary>
          <p>Sí, puedes adaptar la visualización y los accesos rápidos según las necesidades de tu equipo de recepción.</p>
        </details>
        <details>
          <summary>¿Qué hago si olvido mi contraseña?</summary>
          <p>Haz clic en “¿Olvidaste tu contraseña?” en la pantalla de inicio de sesión y sigue los pasos para recuperarla.</p>
        </details>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="social-links">
        <a href="#">Facebook</a>
        <a href="#">Instagram</a>
        <a href="#">Twitter</a>
      </div>
      <p>&copy; 2025 VisualHotel. Todos los derechos reservados.</p>
    </footer>

    <!-- LOGIN -->
    <div v-if="showLogin" class="modal-overlay">
      <div class="modal">
        <div class="modal-left">
          <div class="logo">VisualHotel</div>
          <div class="subtitle">Tu panel de gestión hotelera</div>
        </div>
        <div class="modal-right">
          <h2>Bienvenido</h2>
          <form @submit.prevent="login">
            <input v-model="loginEmail" type="email" placeholder="Email" required />
            <input v-model="loginPassword" type="password" placeholder="Contraseña" required />
            <div class="modal-buttons">
              <button type="submit">Entrar</button>
              <button type="button" @click="showLogin = false">Cancelar</button>
            </div>
          </form>
          <p v-if="loginError" class="error">{{ loginError }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',

  data() {
    return {
      currentSlide: 0,
      slides: [
        {
          image: 'https://media.istockphoto.com/id/1448506100/photo/male-hotel-receptionist-assisting-female-guest.jpg?s=612x612&w=0&k=20&c=xXJn95XgzSA4_LgGczr7ce-FnpcWXwYIr-fGH9yN_z0=',
          text: 'Bienvenido a VisualHotel — Tu experiencia de hospedaje ideal.',
        },
        {
          image: 'https://t4.ftcdn.net/jpg/01/04/13/57/360_F_104135791_1cLZHNM7Y74TFsLKtG08JcfbIe3SiRma.jpg',
          text: 'Reserva, gestiona y disfruta — Todo en un solo lugar.',
        },
        {
          image: 'https://t3.ftcdn.net/jpg/00/29/13/38/360_F_29133877_bfA2n7cWV53fto2BomyZ6pyRujJTBwjd.jpg',
          text: 'Tu comodidad es nuestra prioridad.',
        },
      ],
      interval: null,
      showLogin: false,
      loginEmail: '',
      loginPassword: '',
      loginError: '',
    };
  },
  
  methods: {
    // goToClientAccess() {
    //   this.$router.push({ name: 'ClientAccess' })
    // },
    startAutoSlide() {
      this.interval = setInterval(this.nextSlide, 5000)
    },
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.slides.length) % this.slides.length
    },
    openLogin() {
      this.showLogin = true;
      this.loginError = '';
      this.loginEmail = '';
      this.loginPassword = '';
    },
    async login() {
      try {
        const res = await fetch('http://127.0.0.1:8001/api/login/', {
          method: 'POST',
          headers:{
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.loginEmail,
            password: this.loginPassword,
          }),
        })
        if (!res.ok) throw new Error('Credenciales incorrectas');
        const data = await res.json();
        console.log(data);
        localStorage.setItem('access', data.access);
        localStorage.setItem('refresh', data.refresh);
        this.showLogin = false;
        console.log('Tokens guardados, redirigiendo...');
        this.$router.push({ name: 'panel' });
      }catch (error) {
        this.loginError = 'Error al iniciar sesión. Por favor, inténtalo de nuevo.';
      }
    }
  },
  beforeUnmount() {
    clearInterval(this.interval)
  },
  mounted() {
    setInterval(() => {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length
    }, 5000)
  },
}
</script>

<style lang="scss">
html, body {
  margin: 0;
  padding: 0;
}

.home-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.navbar {
  background: linear-gradient(90deg, #ffa200 60%, #ffb366 100%);
  padding: 0.6rem 0;
  box-shadow: 0 4px 16px rgba(255,140,0,0.10);
  position: sticky;
  top: 0;
  z-index: 100;
  transition: box-shadow 0.2s;

  .nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1300px;
    margin: 0 auto;
    padding: 0.7rem 2.5rem;
  }

  .logo {
    font-size: 2rem;
    font-weight: 900;
    color: #fff;
    letter-spacing: 1.5px;
    text-shadow: 0 2px 8px rgba(255,140,0,0.10);
    transition: color 0.2s;
    cursor: pointer;
    font-family: 'Montserrat', 'Roboto', Arial, sans-serif;
  }

  .client-access {
    background: #fff;
    color: #ffa200;
    padding: 0.6rem 1.6rem;
    border: none;
    border-radius: 24px;
    cursor: pointer;
    font-weight: 700;
    font-size: 1.08rem;
    box-shadow: 0 2px 12px rgba(255,140,0,0.10);
    transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.1s;
    letter-spacing: 0.5px;

    &:hover {
      background: #ffb366;
      color: #fff;
      box-shadow: 0 4px 24px rgba(255,140,0,0.18);
      transform: translateY(-2px) scale(1.04);
    }
  }
}

.hero-slider {
  height: 60vh;
  background-size: cover;
  background-position: center;
  position: relative;

  .slide-container {
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: background-image 1s ease-in-out, transform 1.5s cubic-bezier(.4,0,.2,1);
    will-change: transform;
    animation: heroZoom 8s infinite alternate;
    @keyframes heroZoom {
      from { transform: scale(1);}
      to { transform: scale(1.07);}
    }
    .overlay {
      background-color: rgba(0, 0, 0, 0.5);
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;

      .hero-text {
        color: #fff;
        font-size: 2.5rem;
        text-align: center;
        max-width: 800px;
        padding: 0 1rem;
      }
    }
  }
}

.stats-section {
  margin: 2.5rem auto 0 auto;
  max-width: 1100px;
  text-align: center;
  padding: 0 1rem;
}
.stats-title {
  font-size: 2.1rem;
  font-weight: 700;
  margin-bottom: 2.5rem;
  color: #222;
  letter-spacing: -1px;
}
.stats-cards {
  display: flex;
  justify-content: space-around;
  align-items: flex-start;
  gap: 2rem;
  flex-wrap: wrap;
}
.stat-card {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(255,140,0,0.07);
  padding: 2.2rem 2.5rem 1.7rem 2.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 220px;
  transition: transform 0.18s, box-shadow 0.18s;
}
.stat-card:hover {
  transform: translateY(-6px) scale(1.03);
  box-shadow: 0 8px 32px rgba(255,140,0,0.13);
}
.stat-icon {
  font-size: 3.2rem;
  margin-bottom: 1.2rem;
  background: linear-gradient(135deg, #ffa200 60%, #ffb366 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.stat-value {
  font-size: 2.1rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 0.2rem;
}
.stat-label {
  font-size: 1.08rem;
  color: #444;
  font-weight: 400;
  letter-spacing: 0.5px;
}
@media (max-width: 900px) {
  .stats-cards {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }
  .stat-card {
    min-width: 180px;
    width: 90%;
  }
}

.about-steps-section {
  background: #eaf4fb;
  padding: 4rem 1rem 3rem 1rem;
  border-radius: 24px;
  margin: 3rem auto 2rem auto;
  max-width: 1400px;
}

.about-steps-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2.5rem;
  align-items: start;
}

.about-step {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(31, 38, 135, 0.07);
  padding: 2rem 1.2rem 1.5rem 1.2rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  min-width: 220px;
  position: relative;
  transition: box-shadow 0.2s, transform 0.2s;
}

.about-step:hover {
  box-shadow: 0 8px 32px rgba(255, 77, 121, 0.13);
  transform: translateY(-6px) scale(1.03);
}

.about-step-number {
  font-size: 2.2rem;
  font-weight: 700;
  color: #ffb366;
  margin-bottom: 0.5rem;
  margin-left: 0.1rem;
}

.about-step h3 {
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 0.7rem;
  color: #222;
}

.about-step p {
  font-size: 1.05rem;
  color: #333;
  margin-bottom: 1.2rem;
  line-height: 1.5;
}

.about-step strong {
  font-weight: 700;
  color: #111;
}

.about-step img {
  width: 100%;
  max-width: 260px;
  border-radius: 12px;
  margin-top: auto;
  object-fit: cover;
  aspect-ratio: 4/3;
  box-shadow: 0 2px 12px rgba(255,77,121,0.07);
}

@media (max-width: 1100px) {
  .about-steps-grid {
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
}
@media (max-width: 700px) {
  .about-steps-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  .about-step {
    align-items: center;
    text-align: center;
  }
}

.faq-section {
  padding: 3rem 2rem;
  background: #f6faff;
  border-radius: 24px;
  margin: 3rem auto 2rem auto;
  max-width: 900px;
  box-shadow: 0 4px 24px rgba(31, 38, 135, 0.07);

  h2 {
    text-align: center;
    font-size: 2.2rem;
    margin-bottom: 2.5rem;
    color: #222;
    font-weight: 800;
    letter-spacing: 0.5px;
  }

  .faq-items {
    max-width: 700px;
    margin: 0 auto;

    details {
      margin-bottom: 1.2rem;
      border-radius: 12px;
      background: #fff;
      border: none;
      box-shadow: 0 2px 12px rgba(255,140,0,0.07);
      transition: box-shadow 0.2s, background 0.2s;
      overflow: hidden;
      position: relative;

      &[open] {
        box-shadow: 0 4px 24px rgba(255,140,0,0.13);
        background: #fff7ec;
      }

      summary {
        font-weight: 700;
        cursor: pointer;
        outline: none;
        font-size: 1.15rem;
        color: #ffa200;
        padding: 1.2rem 1.5rem;
        background: none;
        border: none;
        transition: color 0.2s;
        position: relative;
        display: flex;
        align-items: center;

        &::before {
          margin-right: 0.8rem;
          font-size: 1.2rem;
          color: #ffa200;
          transition: transform 0.3s;
        }
      }

      &[open] summary {
        color: #ffa200;
      }

      p {
        margin: 0;
        padding: 0 1.5rem 1.2rem 2.3rem;
        color: #444;
        font-size: 1.05rem;
        line-height: 1.6;
        animation: fadeInFaq 0.4s;
      }
    }
  }
}

@keyframes fadeInFaq {
  from { opacity: 0; transform: translateY(-10px);}
  to { opacity: 1; transform: translateY(0);}
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.35);
  display: flex; align-items: center; justify-content: center;
  z-index: 1000;
}

.modal {
  display: flex;
  flex-direction: row;
  background: #fff;
  border-radius: 28px;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
  min-width: 650px;
  min-height: 370px;
  overflow: hidden;
  animation: fadeIn 0.5s;
}

.modal-left {
  background: linear-gradient(135deg, #ff8c00 60%, #ffb366 100%);
  flex: 1.1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #fff;
  padding: 2.5rem 1.5rem;
  min-width: 220px;
  text-align: center;
}

.modal-left .logo {
  font-size: 2.7rem;
  font-weight: 900;
  letter-spacing: 2px;
  margin-bottom: 0.7rem;
  margin-left: 1rem;
  margin-right: 1rem;
  font-family: 'Montserrat', 'Roboto', Arial, sans-serif;
}

.modal-left .subtitle {
  font-size: 1.1rem;
  opacity: 0.93;
  margin-bottom: 1.5rem;
}

.modal-right {
  flex: 1.6;
  background: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2.5rem 2.2rem;
}

.modal-right h2 {
  color: #ffa200;
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 1.2rem;
  text-align: center;
  letter-spacing: 0.5px;
}

.modal-right form {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.modal-right input[type="email"],
.modal-right input[type="password"] {
  width: 100%;
  max-width: 320px;
  background: #eaf4fb;
  border: none;
  border-radius: 22px;
  padding: 1rem 1.3rem;
  font-size: 1.08rem;
  margin-bottom: 1.1rem;
  outline: none;
  transition: box-shadow 0.2s, border 0.2s;
  box-shadow: 0 2px 8px rgba(255,140,0,0.07);
}

.modal-right input[type="email"]:focus,
.modal-right input[type="password"]:focus {
  box-shadow: 0 0 0 2px #ffb36655;
  border: 1.5px solid #ffa200;
}

.modal-buttons {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 1.2rem;
  margin-top: 1.2rem;
  width: 100%;
}

.modal-buttons button {
  min-width: 140px;
  border-radius: 22px;
  font-size: 1.08rem;
  font-weight: 700;
  padding: 0.85rem 0;
  border: none;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.1s;
  box-shadow: 0 2px 8px rgba(255,140,0,0.10);
}

.modal-buttons button[type="submit"] {
  background: linear-gradient(90deg, #ffa200 60%, #ffb366 100%);
  color: #fff;
}

.modal-buttons button[type="submit"]:hover {
  background: linear-gradient(90deg, #ffb366 0%, #ffa200 100%);
  color: #fff;
  transform: translateY(-2px) scale(1.03);
}

.modal-buttons button[type="button"] {
  background: #fff;
  color: #ffa200;
  border: 2px solid #ffa200;
}

.modal-buttons button[type="button"]:hover {
  background: #ffa200;
  color: #fff;
  border: 2px solid #ffb366;
}

@media (max-width: 800px) {
  .modal {
    flex-direction: column;
    min-width: 320px;
    min-height: 0;
  }
  .modal-left, .modal-right {
    min-width: 0;
    width: 100%;
    padding: 2rem 1.2rem;
  }
}

.footer {
  background-color: #ffa200;
  color: #fff;
  text-align: center;
  padding: 2rem;

  .social-links {
    margin-bottom: 1rem;

    a {
      margin: 0 1rem;
      color: #fff;
      text-decoration: none;
      font-weight: 500;

      &:hover {
        text-decoration: underline;
      }
    }
  }

  p {
    font-size: 0.875rem;
  }
}
</style>