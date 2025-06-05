import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PanelView from '@/views/PanelView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/panel',
    name: 'panel',
    component: PanelView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const access = localStorage.getItem('access')
  if (access && to.name === 'home') {
    // Si hay token y va a Home, redirige a panel
    console.log('Token encontrado, redirigiendo a panel')
    next({ name: 'panel' })
  } else if (!access && to.name === 'panel') {
    // Si no hay token y va a panel, redirige a home
    console.log('No hay token, redirigiendo a home')
    next({ name: 'home' })
  } else {
    next()
  }
})
export default router
