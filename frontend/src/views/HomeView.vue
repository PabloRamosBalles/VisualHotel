<template>
  <div class="home-page">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="nav-content">
        <div class="logo">VisualHotel</div>
        <button class="client-access">Acceso Clientes</button>
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
      interval: null
    };
  },
  
  methods: {
    startAutoSlide() {
      this.interval = setInterval(this.nextSlide, 5000)
    },
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.slides.length) % this.slides.length
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
  padding: 1rem 2rem;
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
    font-size: 1.8rem;
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