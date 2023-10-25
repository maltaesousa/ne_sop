import { createApp } from 'vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import { Quasar } from 'quasar'
import quasarLang from 'quasar/lang/fr'
import App from './App.vue'
import { store } from './store/store.js'

import ItemsList from './views/ItemsList.vue'
import EntitiesList from './views/EntitiesList.vue'
import EventsList from './views/EventsList.vue'
import Event from './views/Event.vue'
import NewEvent from './views/NewEvent.vue'
import Statistics from './views/Statistics.vue'
import Item from './views/Item.vue'
import NewItem from './views/NewItem.vue'
import Entity from './views/Entity.vue'
import NewEntity from './views/NewEntity.vue'
// import UsersList from './views/UsersList.vue'
import User from './views/User.vue'
import NewUser from './views/NewUser.vue'
import Login from './views/Login.vue'
import Admin from './views/Admin.vue'
import Help from './views/Help.vue'

const routes = [
    { path: '/', redirect: '/items' },
    { path: '/items', name: 'ItemsList', component: ItemsList },
    { path: '/items/:id', name: 'Item', component: Item, props: true },
    { path: '/items/new', name: 'NewItem', component: NewItem },
    { path: '/entities', name: 'EntitiesList', component: EntitiesList },
    { path: '/entities/:id', name: 'Entity', component: Entity, props: true },
    { path: '/entities/new', name: 'NewEntity', component: NewEntity },
    { path: '/events', name: 'EventsList', component: EventsList },
    { path: '/events/:id', name: 'Event', component: Event, props: true },
    { path: '/events/new', name: 'NewEvent', component: NewEvent },
    { path: '/statistics', name: 'Statistics', component: Statistics },
    /* { path: '/users', name: 'UsersList', component: UsersList }, */
    { path: '/login', name: 'Login', component: Login },
    { path: '/admin', name: 'Admin', component: Admin },
    { path: '/admin/users/:id', name: 'User', component: User, props: true },
    { path: '/admin/users/new', name: 'NewUser', component: NewUser },
    { path: '/help', name: 'Help', component: Help }
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

// navigation guards
router.beforeEach((to, from) => {
    // ...
    // explicitly return false to cancel the navigation
    console.log(`from: ${from}, to: ${to}`)
    if (store.warning) {
        alert('Attention - Modifications non enregistrées')
        //store.warning = true
        //console.log(`store.warning: ${store.warning}`)
        //console.log(from)
        return false
    } else {
        return true
    }
  
})

const app = createApp(App)
app.use(Quasar, {
    config: {
        plugins: {},
        lang: quasarLang
    }
})

// mconsole.log(quasarLang)
// TODO - FIND WHY LANGUAGE PACK IMPORT WITH VITE IS NOT WORKING, LINE BELOW IS A WORKAROUND
Quasar.lang.set(quasarLang)

app.use(router)
app.mount('#q-app')