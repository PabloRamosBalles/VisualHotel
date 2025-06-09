<template>
  <div id="reservation-page">
    <button id="logout-btn" @click="logout" title="Cerrar sesión">
      <i class="fas fa-sign-out-alt"></i> Logout
    </button>
    <div id="reservation-header">
      <h1 id="reservation-title">Reservas</h1>
      <h1 v-if="reservations.length > 0">{{ reservations[0].hotel.name }}</h1>
      <button id="btn-create-reservation" @click="createReservation">
        + Nueva Reserva
      </button>
    </div>
    <div v-if="successMessage"
     :class="['success-message', { 'fade-out': !successVisible }]">
      {{ successMessage }}
    </div>
    <div v-if="showCreatePopup" class="modal-overlay">
    <div class="modal">
      <h2>Nueva Reserva</h2>
      <form @submit.prevent="submitReservation">
        <input v-model="newReservation.customer.first_name" type="text" placeholder="Nombre" required />
        <input v-model="newReservation.customer.last_name" type="text" placeholder="Apellido" required />
        <input v-model="newReservation.customer.email" type="email" placeholder="Email" required />
        <input v-model="newReservation.customer.phone" type="text" placeholder="Teléfono" required />
        <select v-model="newReservation.room" required>
          <option v-for="room in availableRooms" :key="room.id" :value="room.id">
            {{ room.number }} ({{ room.room_type }})
          </option>
        </select>
        <input v-model="newReservation.check_in" type="date" required />
        <input v-model="newReservation.check_out" type="date" required />
        <button type="submit">Crear Reserva</button>
        <button type="button" @click="showCreatePopup = false">Cancelar</button>
      </form>
      <p v-if="createError" class="error">{{ createError }}</p>
    </div>
  </div>
    <div v-if="reservations.length === 0">
      <p id="no-reservations">No hay reservas registradas.</p>
    </div>

    <div v-else id="reservation-list">
      <div
        v-for="reservation in reservations"
        :key="reservation.id"
        class="reservation-card"
      >
        <div class="reservation-info">
          <p><strong>ID Reserva:</strong> {{ reservation.id }}</p>          
          <p><strong>Habitación:</strong> {{ reservation.room.number }} ({{ reservation.room.room_type }})</p>
          <p><strong>Cliente:</strong> {{ reservation.customer.first_name }} {{ reservation.customer.last_name }}</p>
          <p><strong>Email:</strong> {{ reservation.customer.email }}</p>
          <p><strong>Teléfono:</strong> {{ reservation.customer.phone }}</p>
          <p><strong>Check-in:</strong> {{ reservation.check_in }}</p>
          <p><strong>Check-out:</strong> {{ reservation.check_out }}</p>
        </div>
        <div class="reservation-actions">
          <button @click="editReservation(reservation.id)" title="Editar">
            <i class="fas fa-pen"></i>
          </button>
          <button @click="deleteReservation(reservation.id, reservation.room.id)" title="Eliminar">
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    name: 'PanelView',
    data() {
        return{
            reservations: [],
            showCreatePopup: false,
            newReservation: {
              customer: {
                first_name: '',
                last_name: '',
                email: '',
                phone: ''
              },
              room: '',
              check_in: '',
              check_out: '',
              hotel: null
            },
            availableRooms: [],
            createError: '',
            successMessage: '',
            successVisible: false
        }
    },
    methods: {
        async fetchAvailableRooms() {
          // Suponiendo que tienes el hotel id en this.reservations[0].hotel.id
          const token = localStorage.getItem('access');
          if (!token) return;
          const res = await fetch(`http://127.0.0.1:8001/api/rooms/`, {
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'application/json'
            }
          });
          if (res.ok) {
            this.availableRooms = await res.json();
          }
        },
        createReservation() {
          this.showCreatePopup = true;
          this.fetchAvailableRooms();
          // Asigna el hotel automáticamente si ya tienes reservas
          if (this.reservations.length > 0) {
            this.newReservation.hotel = this.reservations[0].hotel.id;
            console.log("ID HOTEL:", this.newReservation)
          }
        },
        async submitReservation() {
          try {
            const token = localStorage.getItem('access');
            console.log("RESERVATION DATA:", this.newReservation);
            const res = await fetch('http://127.0.0.1:8001/api/reserves/', {
              method: 'POST',
              headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'              
              },
              body: JSON.stringify(this.newReservation)
            });
            if (!res.ok) throw new Error('Error al crear la reserva');
            this.showCreatePopup = false;
            this.createError = '';
            this.successMessage = '¡Reserva creada con éxito!';
            this.successVisible = true;
            this.fetchReservations();
            setTimeout(() => {
              this.successVisible = false;
              setTimeout(() => {
                this.successMessage = '';
              }, 300); 
            }, 3000);
          } catch (e) {
            this.createError = 'No se pudo crear la reserva';
          }
        },
        async fetchReservations() {
            const token = localStorage.getItem('access')
            const res = await fetch('http://127.0.0.1:8001/api/reserves/', {
                headers : {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (res.ok) {
                this.reservations = await res.json()
                console.log(this.reservations)
            } else {
                this.reservations = []
            }
        },
        async deleteReservation(reservationId, roomId) {
          if (confirm('¿Estás seguro de que quieres borrar esta reserva?')) {
            const token = localStorage.getItem('access');
            // Borra la reserva
            const res = await fetch(`http://127.0.0.1:8001/api/reserves/${reservationId}/`, {
              method: 'DELETE',
              headers: {
                'Authorization': `Bearer ${token}`
              }
            });
            if (res.ok) {
              // Cambia el estado de la habitación a Disponible
              await fetch(`http://127.0.0.1:8001/api/rooms/${roomId}/`, {
                method: 'PATCH',
                headers: {
                  'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status: 'Disponible' })
              });
              this.successMessage = 'Reserva eliminada correctamente';
              this.successVisible = true;
              this.fetchReservations();
              setTimeout(() => {
                this.successVisible = false;
                setTimeout(() => {
                  this.successMessage = '';
                }, 300);
              }, 2000);
            } else {
              alert('No se pudo borrar la reserva');
            }
          }
        },
        logout() {
          localStorage.removeItem('access');
          localStorage.removeItem('refresh');
          this.$router.push({ name: 'home' });
        },   
    },
    mounted() {
        this.fetchReservations()
    },
}
</script>

<style lang="scss" src="@/assets/styles/panel.scss">

</style>