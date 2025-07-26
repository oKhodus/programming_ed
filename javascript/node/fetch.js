// import axios from "axios"
const axios = require('axios')

axios.get('http://localhost:3001/notes').then(res => {
        console.log(res.data.map(obj => obj.content))
})

const promise = axios.get('http://localhost:3001/notes')
console.log(promise)