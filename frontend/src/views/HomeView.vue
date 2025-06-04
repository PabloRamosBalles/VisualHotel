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
          <!-- Arrows -->
          <!-- <button class="arrow left" @click="prevSlide">&#10094;</button>
          <button class="arrow right" @click="nextSlide">&#10095;</button> -->
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section class="about-section">
      <h2>Sobre VisualHotel</h2>
      <p>
        VisualHotel es una plataforma moderna para gestionar reservas y habitaciones de manera eficiente y simple. Nuestro objetivo es digitalizar la experiencia hotelera para clientes y administradores por igual.
      </p>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <h2>Preguntas Frecuentes (FAQ)</h2>
      <div class="faq-items">
        <details>
          <summary>¿Cómo puedo reservar una habitación?</summary>
          <p>Puedes usar nuestro sistema de reservas accediendo desde el botón “Acceso Clientes”.</p>
        </details>
        <details>
          <summary>¿Puedo cancelar mi reserva?</summary>
          <p>Sí, puedes cancelar desde tu perfil hasta 24 horas antes de la llegada.</p>
        </details>
        <details>
          <summary>¿Ofrecen atención al cliente?</summary>
          <p>Claro, puedes contactarnos por redes sociales o nuestro formulario de contacto.</p>
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
    <div v-if="showLogin" class="modal-overlay">
      <div class="modal">
        <h2>Iniciar sesión</h2>
        <form @submit.prevent="login">
          <input v-model="loginEmail" type="email" placeholder="Email" required />
          <input v-model="loginPassword" type="password" placeholder="Contraseña" required />
          <button type="submit">Entrar</button>
          <button type="button" @click="showLogin = false">Cancelar</button>
        </form>
        <p v-if="loginError" class="error">{{ loginError }}</p>
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
  background-color: #ff8c00;
  padding: 0.3rem 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;

  .nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;  
    width: 100%;
    padding: 1rem 2rem;
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: #fff;
  }

  .client-access {
    background-color: #fff;
    color: #ff8c00;
    padding: 0.5rem 1.25rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: 500;
    transition: background-color 0.3s;

    &:hover {
      background-color: #d9d9d9;
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
    transition: background-image 1s ease-in-out;
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

.about-section {
  padding: 3rem 2rem;
  background-color: #f9f9f9;
  text-align: center;

  h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }

  p {
    max-width: 700px;
    margin: 0 auto;
    color: #555;
  }
}

.faq-section {
  padding: 3rem 2rem;

  h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 2rem;
  }

  .faq-items {
    max-width: 700px;
    margin: 0 auto;

    details {
      background: #f1f1f1;
      margin-bottom: 1rem;
      padding: 1rem;
      border-radius: 6px;
      cursor: pointer;

      summary {
        font-weight: 600;
      }

      p {
        margin-top: 0.5rem;
        color: #444;
      }
    }
  }
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  display: flex; align-items: center; justify-content: center;
  z-index: 1000;
}
.modal {
  background: #fff;
  padding: 2.5rem 2rem 2rem 2rem;
  border-radius: 14px;
  min-width: 320px;
  box-shadow: 0 4px 24px rgba(255, 140, 0, 0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 2px solid #ff8c00;
}
.modal h2 {
  color: #ff8c00;
  margin-bottom: 1.5rem;
  font-weight: 700;
  font-size: 1.6rem;
}
.modal form {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 1rem;
}
.modal input[type="email"],
.modal input[type="password"] {
  padding: 0.75rem 1rem;
  border: 1.5px solid #ffb366;
  border-radius: 6px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
}
.modal input[type="email"]:focus,
.modal input[type="password"]:focus {
  border: 1.5px solid #ff8c00;
}
.modal button[type="submit"] {
  background: linear-gradient(90deg, #ff8c00 60%, #ffb366 100%);
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 0.75rem 0;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 0.5rem;
  transition: background 0.2s;
}
.modal button[type="submit"]:hover {
  background: linear-gradient(90deg, #ffb366 0%, #ff8c00 100%);
}
.modal button[type="button"] {
  background: #fff;
  color: #ff8c00;
  border: 1.5px solid #ff8c00;
  border-radius: 6px;
  padding: 0.75rem 0;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 0.25rem;
  transition: background 0.2s, color 0.2s;
}
.modal button[type="button"]:hover {
  background: #ff8c00;
  color: #fff;
}
.modal .error {
  color: #ff4d00;
  margin-top: 0.5rem;
  font-size: 0.95rem;
  text-align: center;
}

.footer {
  background-color: #ff8c00;
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