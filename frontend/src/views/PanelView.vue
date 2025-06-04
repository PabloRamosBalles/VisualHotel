<template>
  <div id="reservation-page">
    <div id="reservation-header">
      <h1 id="reservation-title">Reservas</h1>
      <button id="btn-create-reservation" @click="createReservation">
        + Nueva Reserva
      </button>
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
          <p><strong>ID:</strong> {{ reservation.id }}</p>
          <p><strong>Check-in:</strong> {{ reservation.check_in }}</p>
          <p><strong>Check-out:</strong> {{ reservation.check_out }}</p>
          <p><strong>Hotel ID:</strong> {{ reservation.hotel }}</p>
          <p><strong>Habitación ID:</strong> {{ reservation.room }}</p>
          <p><strong>Cliente ID:</strong> {{ reservation.customer }}</p>
        </div>
        <div class="reservation-actions">
          <button @click="editReservation(reservation.id)" title="Editar">
            <i class="fas fa-pen"></i>
          </button>
          <button @click="deleteReservation(reservation.id)" title="Eliminar">
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
            reservations: []
        }
    },
    methods: {
        async fetchReservations() {
            const token = localStorage.getItem('access')
            const res = await fetch('http://127.0.0.1:8001/api/reserves/', {
                headers : {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (res.ok) {
                this.reservations = await res.json()
            } else {
                this.reservations = []
            }
        },
        // createReservation() {
        //     // lógica para crear reserva
        // },
        // editReservation(id) {
        //     // lógica para editar reserva
        // },
        // deleteReservation(id) {
        //     // lógica para eliminar reserva
        // }    
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
</style>