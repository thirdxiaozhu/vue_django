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

export function getScheduled4test(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/teacher/getscheduled4test",
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

export function ifarrange(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/teacher/ifarrange",
        params : param
    })
}


export function updateGrade(data){
    return axios.request({
        method: "POST",
        url: "/api/teacher/updategrade/",
        data : data
    })
}


export function getSendlist(params){
    return axios.request({
        method: "GET",
        url: "/api/teacher/getsendlist",
        params: params
    })
}

export function getSavelist(params){
    return axios.request({
        method: "get",
        url: "/api/teacher/getsavelist",
        params: params
    })
}


export function replyMessage(data){
    return axios.request({
        method: "post",
        url: "/api/teacher/replymessage/",
        data: data
    })
}


export function rejectMessage(data){
    return axios.request({
        method: "post",
        url: "/api/teacher/rejectmessage/",
        data: data
    })
}

export function postMessage(params){
    return axios.request({
        method: "POST",
        url: "/api/teacher/postmessage/",
        data: params
    })
}