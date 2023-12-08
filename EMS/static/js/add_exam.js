
function addQuestion(){
    questions = document.getElementsByClassName('questions')[0]
    var questionTemplate = document.createElement('div');

    question_form = `<br><hr><br><div class="questiondata">
<label for="question_name">
    <span>Question:</span>
    <input type="text" name="question" class="question">
</label>

<div class="choices">
    <label for="choiceA">
        <span>A:</span>
        <input type="text" class="A">
    </label>

    <label for="choiceB">
        <span>B:</span>
        <input type="text" class="B">
    </label>

    <label for="choiceC">
        <span>C:</span>
        <input type="text" class="C">
    </label>

    <label for="choiceD">
        <span>D:</span>
        <input type="text" class="D">
    </label>
</div>

<label for="answer">
    <span>Answer:</span>
    <input type="text" class="answer">
</label>
</div>`
    questionTemplate.innerHTML = question_form;
    questions.appendChild(questionTemplate);
}



function collectAndSubmit() {
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

    go_to_backend(JSON.stringify(data));    
}


function go_to_backend(raw) {
    var myHeaders = new Headers();
    myHeaders.append("Cache-Control", "no-cache");
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Accept", "*/*");
    myHeaders.append("Accept-Encoding", "gzip, deflate, br");
    myHeaders.append("Connection", "keep-alive");
    myHeaders.append("Authorization", "Token f8edbc239308bd75ec431558ee6984a424b43144");

    

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/exams/exams/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));

}
