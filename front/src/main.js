import { createApp } from 'vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import { Quasar } from 'quasar'
import App from './App.vue'
import ItemsList from '@/views/ItemsList.vue'
import EntitiesList from '@/views/EntitiesList.vue'
import EventsList from '@/views/EventsList.vue'
import Statistics from '@/views/Statistics.vue'
import Item from '@/views/Item.vue'
import Entity from '@/views/Entity.vue'
import Login from '@/views/Login.vue'

const routes = [
    { path: '/items', name: 'ItemsList', component: ItemsList },
    { path: '/items/:id', name: 'Item', component: Item, props: true },
    { path: '/entities', name: 'EntitiesList', component: EntitiesList },
    { path: '/entities/:id', name: 'Entity', component: Entity, props: true },
    { path: '/events', name: 'EventsList', component: EventsList },
    { path: '/statistics', name: 'Statistics', component: Statistics },
    { path: '/login', name: 'Login', component: Login }
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

const app = createApp(App)
app.use(Quasar, {
    config: {
    },

})
app.use(router)
app.mount('#q-app')