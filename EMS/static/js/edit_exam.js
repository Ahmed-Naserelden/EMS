function collectAndSave(pk) {
    var data = {
        subject: document.querySelector('.subject').value,
        level: document.querySelector('[name="level"]').value,
        questions: []
    };

    var questions = document.querySelectorAll('.questiondata');
    questions.forEach(function(question) {
        var qData = {
            title: question.querySelector('.question').value,
            A: question.querySelector('.A').value,
            B: question.querySelector('.B').value,
            C: question.querySelector('.C').value,
            D: question.querySelector('.D').value,
            answer: question.querySelector('.answer').value
        };
        data.questions.push(qData);
    });
    console.log(JSON.stringify(data))

    go_to_update_backend(JSON.stringify(data), pk);    
}

function go_to_update_backend(raw, pk){
    var myHeaders = new Headers();
    myHeaders.append("Cache-Control", "no-cache");
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Accept", "*/*");
    myHeaders.append("Accept-Encoding", "gzip, deflate, br");
    myHeaders.append("Connection", "keep-alive");
    myHeaders.append("Authorization", "Token f8edbc239308bd75ec431558ee6984a424b43144");

    

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(`http://127.0.0.1:8000/api/exams/exams/${pk}/`, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}