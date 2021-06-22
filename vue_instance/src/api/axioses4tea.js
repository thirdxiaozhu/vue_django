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

export function initTeacherinfo(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/teacher/initteacherinfo",
        params : param
    })
}


export function getScheduled(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/teacher/getscheduled",
        params : param
    })
}


export function initStudentList(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/teacher/initstudentlist",
        params : param
    })
}