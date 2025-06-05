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

<style>
#reservation-page {
  padding: 24px;
  font-family: 'Segoe UI', sans-serif;
}

#reservation-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  margin-top: 28px;
}

#reservation-title {
  font-size: 28px;
  color: #2c2c2c;
}

#btn-create-reservation {
  background-color: #3f3d56;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

#btn-create-reservation:hover {
  background-color: #2e2c44;
}

#no-reservations {
  font-style: italic;
  color: #888;
}

#reservation-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.reservation-card {
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 8px #ff8c00;
  width: 350px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  border-left: 8px solid #ff8c00;
  transition: transform 0.2s ease;
}

.reservation-card:hover {
  transform: translateY(-4px);
}

.reservation-info p {
  margin: 6px 0;
  font-size: 14px;
  color: #333;
}

.reservation-info p strong {
  color: #111;
}

.reservation-actions {
  position: absolute;
  bottom: 16px;
  right: 16px;
  display: flex;
  gap: 12px;
}

.reservation-actions button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 18px;
  color: #3f3d56;
  transition: color 0.2s ease;
}

.reservation-actions button:hover {
  color: #ff4d4d;
}

#logout-btn {
  position: absolute;
  top: 24px;
  left: 24px;
  background: linear-gradient(90deg, #ff8c00 60%, #ffb366 100%);
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 10px 18px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 2px 8px rgba(255,140,0,0.08);
  transition: background 0.2s, color 0.2s;
  z-index: 10;
}
#logout-btn i {
  font-size: 18px;
}
#logout-btn:hover {
  background: linear-gradient(90deg, #ffb366 0%, #ff8c00 100%);
  color: #fff;
}
.success-message {
  background: linear-gradient(90deg, #ffb366 0%, #ff8c00 100%);
  color: #fff;
  padding: 14px 24px;
  border-radius: 8px;
  font-weight: bold;
  font-size: 1.1rem;
  margin-bottom: 18px;
  box-shadow: 0 2px 8px rgba(255,140,0,0.10);
  text-align: center;
  animation: fadeIn 0.5s;
  opacity: 1;
  transition: opacity 0.5s;
}
.success-message.fade-out {
  opacity: 0;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px);}
  to { opacity: 1; transform: translateY(0);}
}
</style>