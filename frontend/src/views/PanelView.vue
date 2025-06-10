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
    <div id="filter-bar" style="margin-bottom: 1rem;">
      <label>
        Desde:
        <input type="date" v-model="filterStartDate">
      </label>
      <label>
        Hasta:
        <input type="date" v-model="filterEndDate">
      </label>
      <button @click="applyDateFilter">Filtrar</button>
      <button @click="clearDateFilter" v-if="filterStartDate || filterEndDate">Limpiar</button>
    </div>
    <div v-if="successMessage"
     :class="['success-message', { 'fade-out': !successVisible }]">
      {{ successMessage }}
    </div>
    <!-- create modal -->
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
          <div class="modal-buttons">
            <button type="submit">Crear</button>
            <button type="button" @click="showCreatePopup = false">Cancelar</button>
          </div>
        </form>
        <p v-if="createError" class="error">{{ createError }}</p>
      </div>
    </div>
    <!-- Edit modal -->
    <div v-if="showEditPopup" class="modal-overlay">
      <div class="modal">
        <h2>Editar Reserva</h2>
        <form @submit.prevent="submitEditReservation">
          <input v-model="editReservationData.customer.first_name" type="text" placeholder="Nombre" required />
          <input v-model="editReservationData.customer.last_name" type="text" placeholder="Apellido" required />
          <input v-model="editReservationData.customer.email" type="email" placeholder="Email" required />
          <input v-model="editReservationData.customer.phone" type="text" placeholder="Teléfono" required />
          <select v-model="editReservationData.room" required>
            <option v-for="room in availableRooms" :key="room.id" :value="room.id">
              {{ room.number }} ({{ room.room_type }})
            </option>
          </select>
          <input v-model="editReservationData.check_in" type="date" required />
          <input v-model="editReservationData.check_out" type="date" required />
          <div class="modal-buttons">
            <button type="submit">Guardar</button>
            <button type="button" @click="showEditPopup = false">Cancelar</button>
          </div>
        </form>
        <p v-if="editError" class="error">{{ editError }}</p>
      </div>
    </div>
    <div v-if="reservations.length === 0">
      <p id="no-reservations">No hay reservas registradas.</p>
    </div>

    <div v-else id="reservation-list">
      <div
        v-for="reservation in filteredReservations"
        :key="reservation.id"
        class="reservation-card"
      >
        <div class="reservation-info">
          <p><strong>ID Reserva:</strong> {{ reservation.id }}</p>          
          <p><strong>Habitación:</strong> {{ reservation.room.number }} ({{ reservation.room.room_type }})</p>
          <p><strong>Cliente:</strong> {{ reservation.customer.first_name }} {{ reservation.customer.last_name }}</p>
          <p><strong>Email:</strong> {{ reservation.customer.email }}</p>
          <p><strong>Teléfono:</strong> {{ reservation.customer.phone }}</p>
          <p>
            <strong>Check-in:</strong>
            <span :style="{ color: isCheckInActive(reservation.check_in) }">
              {{ reservation.check_in }}
            </span>
          </p>
          <p>
            <strong>Check-out:</strong>
            <span :style="{ color: isCheckOutActive(reservation.check_out) }">
              {{ reservation.check_out }}
            </span>
          </p>
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
            showEditPopup: false,
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
            editReservationData: {
              id: null,
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
            editError: '',
            successMessage: '',
            successVisible: false,
            filterStartDate: '',
            filterEndDate: '',
            filteredReservations: [],
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
        async editReservation(reservationId) {
          console.log('Editando reserva', reservationId);
          const reservation = this.reservations.find(r => r.id === reservationId);
          if (reservation) {
            console.log('id del cliente:', reservation.customer.id);
            this.editReservationData = {
              id: reservation.id,
              customer: { ...reservation.customer, id: reservation.customer.id },
              room: reservation.room.id,
              check_in: reservation.check_in,
              check_out: reservation.check_out,
              hotel: reservation.hotel.id
            };
            this.editError = '';
            this.showEditPopup = true;
            await this.fetchAvailableRooms();
            const exists = this.availableRooms.some(r => r.id === reservation.room.id);
            if (!exists) {
              this.availableRooms.push(reservation.room);
            }
          }
        },
        async submitEditReservation() {
          try {
            const token = localStorage.getItem('access');

            await fetch(`http://127.0.0.1:8001/api/customers/`, {
              method: 'PATCH',
              headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                customer_id: this.editReservationData.customer.id,
                first_name: this.editReservationData.customer.first_name,
                last_name: this.editReservationData.customer.last_name,
                email: this.editReservationData.customer.email,
                phone: this.editReservationData.customer.phone
              })
            });

            const res = await fetch(`http://127.0.0.1:8001/api/reserves/${this.editReservationData.id}/`, {
              method: 'PATCH',
              headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                customer: this.editReservationData.customer.id,
                room_id: this.editReservationData.room,
                check_in: this.editReservationData.check_in,
                check_out: this.editReservationData.check_out,
                hotel: this.editReservationData.hotel
              })
            });
            if (!res.ok) {
              const errorData = await res.json();
              console.log('Error backend:', errorData);
              throw new Error('Error al editar la reserva');
            }
            this.showEditPopup = false;
            this.editError = '';
            this.successMessage = '¡Reserva editada con éxito!';
            this.successVisible = true;
            this.fetchReservations();
            setTimeout(() => {
              this.successVisible = false;
              setTimeout(() => {
                this.successMessage = '';
              }, 300);
            }, 3000);
          } catch (e) {
            this.editError = 'No se pudo editar la reserva';
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
                this.reservations = (await res.json()).sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
                this.filteredReservations = this.reservations.slice();
            } else {
                this.reservations = []
                this.filteredReservations = []
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
        applyDateFilter() {
          this.filteredReservations = this.reservations
            .filter(res => {
              const checkIn = new Date(res.check_in);
              let valid = true;
              if (this.filterStartDate) {
                valid = valid && checkIn >= new Date(this.filterStartDate);
              }
              if (this.filterEndDate) {
                valid = valid && checkIn <= new Date(this.filterEndDate);
              }
              return valid;
            })
            .sort((a, b) => new Date(a.check_in) - new Date(b.check_in));
        },
        clearDateFilter() {
          this.filterStartDate = '';
          this.filterEndDate = '';
          this.filteredReservations = this.reservations.slice()
        },
        isCheckInActive(checkIn) {
          // Si el día del check-in es HOY o anterior, verde; si es futuro, rojo
          const today = new Date();
          today.setHours(0,0,0,0);
          const inDate = new Date(checkIn);
          inDate.setHours(0,0,0,0);
          return inDate <= today ? 'green' : 'red';
        },
        isCheckOutActive(checkOut) {
          // Si el día del check-out es HOY o posterior, rojo; si ya pasó, verde
          const today = new Date();
          today.setHours(0,0,0,0);
          const outDate = new Date(checkOut);
          outDate.setHours(0,0,0,0);
          return outDate >= today ? 'red' : 'green';
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