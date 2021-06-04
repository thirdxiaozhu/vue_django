import axios from 'axios'
import qs from 'qs'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
/* axios.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'; */
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

export function postSubmit(data){
    console.log(typeof(data.ifadd));
    return axios.request({
        method: "POST",
        url: "/api/editstudent/",
        data: data,
    })
}

export function getOrganize(param){
    console.log(param);
    return axios.request({
        method: "GET",
        url: "/api/getOrganize",
        params: param
    })
}

export function postaddStu(data){
    console.log(typeof(data.ifadd));
    return axios.request({
        method: "POST",
        url: "/api/addstudent/",
        data: data,
    })
}

export function initStudentList(param){
    console.log(param);
    return axios.request({
        method: "GET",
        url: "/api/studentlist",
        params: param
    })
}

export function deleteStudent(param){
    console.log(param);
    return axios.request({
        method: "GET",
        url: "/api/deletestudent",
        params: param
    })
}