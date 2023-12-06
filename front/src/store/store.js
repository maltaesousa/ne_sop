// store.js
import { reactive } from 'vue'
// import { EntityTypes } from './entity-types.js'
// import entities from '../assets/data/entities.json'
import items from '../assets/data/items.json'
// import events from '../assets/data/events.json'
import users from '../assets/data/users.json'
import { sleep } from '../store/shared.js'
// import { router } from '../router.js'

export const store = reactive({
    dev: true,
    session: { "user": null },
    valid: null,
    loading: true,
    warning: false,
    exit: false,
    navigation: { "from": null, "to": null },
    entityTypes: null,
    entities: [], // entities,
    entity: null,
    itemTypes: null,
    items: [], // items,
    events: [], // events, // items.map((x) => (x.events)).flat(1),
    event: null,
    documents: items.map((x) => (x.documents)).flat(1),
    attachements: items.map((x) => (x.attachements)).flat(1),
    users: users,
    // query parameters, number of results, page, filters
    // API - GET ALL RECORDS
    async getTemplates() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/template/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.templates = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    updateEvents() {
        this.events = this.items.map((x) => (x.events)).flat(1)
    },
    updateDocuments() {
        this.documents = this.items.map((x) => (x.documents)).flat(1)
    },
    updateAttachements() {
        this.attachements = this.items.map((x) => (x.attachements)).flat(1)
    },

    //////////////////////////////////////////////////////////////////////////////////////////////

    // GET LIST OF ENTITIES
    async getEntities(search = "", type = [], page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            // await sleep(1300)
            console.log(`http://127.0.0.1:8000/api/entity?page=${page}&size=${size}&search=${search}&type=${type}&sortby=${sortBy}&descending=${descending}`)
            const response = await fetch(`http://127.0.0.1:8000/api/entity?page=${page}&size=${size}&search=${search}&type=${type}&sortby=${sortBy}&descending=${descending}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ENTITY DETAILS
    async getEntity(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE ENTITY
    async updateEntity(id, data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // ADD ENTITY
    async addEntity(data) {
        try {

            /*
            data = {
                "name": "Didi 9",
                "type_id": 2,
                "type": "sfdsf",
                "description": "",
                "street": "Château Rue de la Collégiale 12",
                "city": "Neuchâtel",
                "postalcode": "2002",
                "region": "Neuchâtel",
                "country": "Suisse",
                "website": "https://www.ne.ch/autorites/DDTE/SDTE/",
                "email": "Secretariat.DDTE@ne.ch",
                "telephone": "+41 32 889 67 00",
                "valid": true
            }
            */

            const response = await fetch(`http://127.0.0.1:8000/api/entity/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

            // .then(response => response.json())
            // .then(result => console.log(result))
            // .catch(error => console.log('error', error))


            // this.entities = await response.json()
            // console.log(this.entities)

        } catch (error) {
            console.error(error)
        }

    },

    // DELETE ENTITY
    async deleteEntity(id) {
        // this.loading = true
        try {

            console.log(`loading: ${this.loading}`)
            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
            // this.loading = false
            // console.log(`loading: ${this.loading}`)
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ENTITY TYPES
    async getEntityTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/entity-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET LIST OF ITEMS
    async getItems(search = "", page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item?page=${page}&size=${size}&sortby=${sortBy}&descending=${descending}&search=${search}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()
            // this.items = await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM DETAILS
    async getItem(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE ITEM
    async updateItem(id, data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // ADD NEW ITEM
    async addItem(data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // DELETE ITEM
    async deleteItem(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM TYPES
    async getItemTypes() {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item-type`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM STATUS
    async getItemStatus() {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item-status`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },


    // GET LIST OF EVENTS
    async getEvents(search = "", item = "", page = 1, size = 10) {
        try {

            await sleep(1300)
            const response = await fetch(`http://127.0.0.1:8000/api/event?page=${page}&size=${size}&item=${item}&search=${search}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET EVENT DETAILS
    async getEvent(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE EVENT
    async updateEvent(id, data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // ADD NEW EVENT
    async addEvent(data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // DELETE EVENT
    async deleteEvent(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET EVENT TYPES
    async getEventTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/event-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },
})