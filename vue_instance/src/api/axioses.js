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


export function postCourseSubmit(data){
    return axios.request({
        method: "POST",
        url: "/api/submitcourse/",
        data: data
    })
}


export function postaddCou(data){
    return axios.request({
        method: "POST",
        url: "/api/addcourse/",
        data: data
    })
}

export function deleteCourse(param){
    console.log(param);
    return axios.request({
        method: "GET",
        url: "/api/deletecourse",
        params: param
    })
}

export function getColleges(param){
    return axios.request({
        method: "GET",
        url: "/api/getcolleges",
        params: param
    })
}


export function getMajors(param){
    return axios.request({
        method: "GET",
        url: "/api/getmajors",
        params: param
    })
}

export function getClasses(param){
    return axios.request({
        method: "GET",
        url: "/api/getclasses",
        params: param
    })
}


export function getScheduled(param){
    return axios.request({
        method: "GET",
        url: "/api/getscheduled",
        params: param
    })
}


export function filterScheduled(param){
    return axios.request({
        method: "GET",
        url: "/api/getscheduled",
        params: param
    })
}


export function getValidRooms(param){
    return axios.request({
        method: "GET",
        url: "/api/getvalidroom",
        params: param
    })
}

export function getCol_Cou(param = {}){
    return axios.request({
        method: "GET",
        url: "/api/getcolcou",
        params: param
    })
}

export function getSchBuilding(){
    return axios.request({
        method: "GET",
        url: "/api/getschbuilding",
    })
}

export function postCreateSchedule(data){
    return axios.request({
        method: "POST",
        url: "/api/addschedule/",
        data: data
    })
}

export function getCourseSch(param){
    return axios.request({
        method: "GET",
        url: "/api/getcoursesch/",
        params: param
    })
}

export function initMajorInfo(param){
    return axios.request({
        method:"GET",
        url: "/api/initmajorinfo",
        params: param
    })
}


export function editMajorOptions(param){
    return axios.request({
        method:"GET",
        url: "/api/editmajoroptions",
        params: param
    })
}

export function postMajorSubmit(data){
    return axios.request({
        method: "POST",
        url: "/api/postmajorsubmit/",
        data: data
    })
}

export function initCourseList4test(params){
    return axios.request({
        method: "get",
        url: "/api/initcourselist4test",
        params: params
    })
}

export function getCollegelist4test(params){
    return axios.request({
        method: "get",
        url: "/api/getcollegelist4test",
        params: params
    })
}


export function updateChoice(data){
    return axios.request({
        method: "POST",
        url: "/api/updatechoice/",
        data: data
    })
}


export function getCoursesAsCollege(params){
    return axios.request({
        method: "get",
        url: "/api/initcourselist4test",
        params: params
    })
}


export function initCourseList4testarr(params){
    return axios.request({
        method: "get",
        url: "/api/initcourselist4testarr",
        params: params
    })
}


export function updateChoice4arr(data){
    return axios.request({
        method: "POST",
        url: "/api/updatechoice4arr/",
        data: data
    })
}


export function getCoursesAsCollege4arr(params){
    return axios.request({
        method: "get",
        url: "/api/initcourselist4testarr",
        params: params
    })
}


export function deleteChoice(data){
    return axios.request({
        method: "POST",
        url: "/api/deletechoice4arr/",
        data: data
    })
}


export function getSendlist(params){
    return axios.request({
        method: "get",
        url: "/api/getsendlist",
        params: params
    })
}


export function replyMessage(data){
    return axios.request({
        method: "post",
        url: "/api/replymessage/",
        data: data
    })
}


export function rejectMessage(data){
    return axios.request({
        method: "post",
        url: "/api/rejectmessage/",
        data: data
    })
}