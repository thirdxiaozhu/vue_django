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
        mathod: "GET",
        url: "/api/student/getcourselist",
        params: param
    })
}