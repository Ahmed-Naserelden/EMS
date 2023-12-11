function deleteTeacher(pk){
    var myHeaders = new Headers();
    myHeaders.append("Cookie", "csrftoken=Nu3Dhcu233ze5ZylKU2m90J62cnzW6dM");
    myHeaders.append("Authorization", "Token f8edbc239308bd75ec431558ee6984a424b43144");

    var requestOptions = {
        method: 'DELETE',
        headers: myHeaders,
        body: "",
        redirect: 'follow'
    };

    fetch(`http://127.0.0.1:8000/api/accounts/teachers/${pk}`, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}




