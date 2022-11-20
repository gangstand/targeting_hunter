const instance = axios.create({
    baseURL: '../api/v1/',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.getCookies('csrftoken')
})



const PersonalPage = {
    delimiters: ['[[', ']]'],
    data: () => ({
        search: '',
        userVisible: true,
        userid: null,
        users: [],
        filteredUsers: [],
        currentUser: null,

        preferences: [],
        preferencesSchem: {},
        maxVal: 0,
        numbers: [],
        baseHeight: 300,

        products: [],

        page: 'user_data'
    }),
    methods: {
        filteredProducts() {
            const schem = this.preferences.reduce((accumulator, currentValue) => {
                if(!(accumulator.includes(currentValue))) return [...accumulator, currentValue.id]
            }, [])
            console.log(schem)
            const products = this.products
            const filteredProducts = products.filter(product => {
                    console.log(product)
                return schem.some(category => category === product.category_id)

            }

            )
            console.log(filteredProducts)
            return filteredProducts
        },
        setProducts(products) {
            console.log(products)
            this.products = products
        },
        setUsers(users) {
            this.users = users
            this.filteredUsers = users
        },
        setUserVisibleTrue() {
            this.userVisible=true
        },
        setUserVisibleFalse() {
            this.userVisible=false
        },
        setPage(e) {
            this.page = e.currentTarget.id
        },

        setPreferences(preferences) {
            this.preferences = preferences
        },

        setPreferencesSchem(schem) {
            this.preferencesSchem = schem
        },
        setMaxVal(val) {
            this.maxVal = val

            let numbers = []
            for (let i = 0; i <= val; i++) {
                numbers = [...numbers, i]
            }

            this.numbers = numbers
        },
        createHeight(value) {
            const height = (this.baseHeight / this.maxVal) * value

            return `height: ${height}px`
        },
        fetchPreferences(userid) {
            instance.get(`docs/prefer?user_id=${userid}`).then(({data}) => {
                    const preferences = data.map(item => {
                        console.log(item)
                            const {name, male, animal, kid, age} = item.category
                            const categoryId = item.prefer.category_id


                            return {name, male, animal, kid, age, id:categoryId}
                        })
                    const schem = {}
                    preferences.map(({name}) => {
                        if(!(schem.keys?.find(name))) {
                                schem[name] = preferences.filter(pref => pref.name === name).length
                        }
                    })



                    let max = 0;
                    for (let key in schem) {
                        if(schem[key] > max) {
                            max = schem[key]
                        }
                    }

                    console.log(schem)
                    console.log(preferences)
                    console.log(max)
                    this.setMaxVal(max)
                    this.setPreferences(preferences)
                    this.setPreferencesSchem(schem)
            })
        },
        fetchProducts() {
            console.log(this.preferences)
            instance.get(`docs/product`)
                .then(res => {
                    this.setProducts(res.data)
                })
        }

    },
    created() {
        instance.get('docs/user').then(({data}) => {
            const users = data.filter(user => (user.username !== 'admin'  && user.username !== 'moderator'))
            this.setUsers(users)

        })

        this.fetchProducts()


    },
    computed: {
        usersDisplay() {
            return this.userVisible ? 'display: flex;' : 'display: none;'
        },
        searchStyle() {
            console.log(this.userVisible)
            return this.userVisible ? 'search-users__field search-users__field--active' : 'search-users__field'
        },
    },
    watch: {
        userid(newId) {
            this.currentUser = this.users.filter(user => user.id === newId)[0];


            this.fetchPreferences(newId)
        },
        page(newPage) {
            if(newPage === 'preferences') {
                this.fetchPreferences(this.userid)
            } else if (newPage === 'products') {
                this.fetchProducts()
            }
        },
        search(value) {
            const fields = ['username', 'email','last_name','first_name', 'patronymic']

            this.filteredUsers = this.users.filter(user => fields.some(field => user[field].includes(value)))
        }
    },


}

Vue.createApp(PersonalPage).mount('#personal')