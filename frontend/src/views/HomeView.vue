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

<style lang="scss" src="../assets/styles/home.scss"></style>