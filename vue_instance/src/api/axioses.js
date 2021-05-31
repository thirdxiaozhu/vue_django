import axios from 'axios'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed';
axios.defaults.headers.get['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.transformRequest = [function (data) {
    let src = ''
    for (let item in data) {
      src += encodeURIComponent(item) + '=' + encodeURIComponent(data[item]) + '&'
    }
    return src
}]

export function getLocation(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/getlocation",
        params : param
    })
}

export function getClass(param = {}){
    console.log(param);
    return axios.request({
        method: "GET",
        url: "/api/getclass",
        params: param
    })
}

export function postLogin(param = {}){
    return axios.request({
        method: "POST",
        url: "/api/login/",
        params: param
    })
}