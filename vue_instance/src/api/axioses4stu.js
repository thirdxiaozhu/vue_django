import axios from 'axios'

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

export function initStudentinfo(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/student/initstudentinfo",
        params : param
    })
}


export function getCourseList(param){
    return axios.request({
        method: "GET",
        url: "/api/student/getcourselist",
        params: param
    })
}

export function initCourseList(param){
    return axios.request({
        method: "GET",
        url: "/api/student/initcourselist",
        params: param
    })
}

export function getRelations(param){
    return axios.request({
        method: "GET",
        url: "/api/student/getrelations",
        params: param
    })
}


export function updateChoice(data){
    console.log(data)
    return axios.request({
        method: "POST",
        url: "/api/student/updatechoice/",
        data: data
    })
}


export function getScheduled(param){
    return axios.request({
        method: "GET",
        url: "/api/student/getscheduled",
        params: param
    })
}

export function filterScheduled(param){
    return axios.request({
        method: "GET",
        url: "/api/student/getscheduled",
        params: param
    })
}


export function deleteScheduled(param){
    return axios.request({
        method: "POST",
        url: "/api/student/deletescheduled/",
        data: param
    })
}