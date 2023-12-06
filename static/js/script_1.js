const api ={
    key: "17df00420ac53c2f7044906a5dd6664a",
    base: "http://127.0.0.1:8000/exams/exam/answers/",
};

grade = document.getElementById("grade")

d = document.getElementsByClassName("quest");

function getData(contest){
    
    var myHeaders = new Headers();
    myHeaders.append("Cookie", "csrftoken=Lgfd97i1hM10MLgxuF3RK2gqFInMW0Qp");

    var formdata = new FormData();

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    //   body: formdata,
    //   redirect: 'follow'
    };

    fetch(`${api.base}${contest}`, requestOptions)
    .then(response => response.json())
    .then(displayData)
    .catch(error => console.log('error', error));
}

maper = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
}

function displayData(response){
    let _grade = 0; 
    console.log(response.length)
    

    for (let i = 0; i < response.length; i++){

        let pk = response[i]['pk'];
        let ans = response[i]['answer'];

        var kame = document.getElementsByName(pk);
        if(kame[ans-1].checked){
            _grade ++;
            console.log(`question number ${i+1} is correct.`);
        }else{
            console.log(`question number ${i+1} is not correct.`);
        }
        
    }

    var _color = 'green; font-size: 22px; font-weight: bold';
    if(_grade < response.length * 0.9) _color = 'balck';
    if(_grade < response.length * 0.251) _color = 'red';
    
    grade.innerHTML = `<b><span style="color:${_color};">` + `Your Grade: ${_grade} / ${response.length}.</span></b>`;
}