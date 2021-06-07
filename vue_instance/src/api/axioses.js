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

export function getRooms(param){
    console.log(param);
    return axios.request({
        method: "GET",
        url: "/api/roomlist",
        params: param
    })
}

export function getFunctions(param){
    return axios.request({
        mathod: "GET",
        url: "/api/getfunctions",
        params: param
    })
}


export function getRoomInfo(param){
    return axios.request({
        mathod: "GET",
        url: "/api/getroominfo",
        params: param
    })
}
            
export function filterroomlist(param){
    return axios.request({
        method: "GET",
        url: "/api/filterroom",
        params: param
    })
}


export function getTeacherlist(param){
    return axios.request({
        method: "GET",
        url: "/api/getteacher",
        params: param
    })
}


export function getCourse(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/getCourse",
        params: param
    })
}


export function initTeacherinfo(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/getteacherinfo",
        params: param
    })
}

export function editTeacherOptions(){
    return axios.request({
        url: "/api/editteaoptions",
        method: "GET",
    })
}

export function postTeacherSubmit(data){
    console.log(data.courses)
    return axios.request({
        method: "POST",
        url: "/api/editteacher/",
        data: data,
    })
}

export function postaddTea(data){
    console.log(typeof(data.ifadd));
    return axios.request({
        method: "POST",
        url: "/api/addteacher/",
        data: data,
    })
}

export function changeTeaCollege(param){
    return axios.request({
        method: "GET",
        url: "/api/collegechange/",
        params: param
    })
}


export function getCourseList(param){
    return axios.request({
        method: "GET",
        url: "/api/getcourselist/",
        params: param
    })
}

export function filterCourseList(param){
    return axios.request({
        method: "GET",
        url: "/api/filtercourselist",
        params: param
    })
}

export function initCourseInfo(param){
    return axios.request({
        method: "GET",
        url: "/api/initcourseinfo",
        params: param
    })
}

export function getCourseOption(param){
    return axios.request({
        mentod: "GET",
        url: "/api/getcourseoption",
        params: param
    })
}