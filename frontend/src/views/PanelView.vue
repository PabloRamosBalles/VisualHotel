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
          <button class="btn-edit" @click="editReservation(reservation.id)">
            Modificar
          </button>
          <button class="btn-delete" @click="deleteReservation(reservation.id)">
            Eliminar
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
            const res = await fetch('http://127.0.0.1:8000(api/reserves/', {
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
    }
}
</script>

<style>

</style>