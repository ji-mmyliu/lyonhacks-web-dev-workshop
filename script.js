const button = document.querySelector("#push");
const taskInput = document.querySelector("#newtask input");
const tasksContainer = document.querySelector("#tasks");

button.onclick = function(){
    if(taskInput.value.length == 0){
        alert("Please Enter a Task");
    }
    else{
        tasksContainer.innerHTML += `
            <div class="task">
                <span>${taskInput.value}</span>
                <button>Delete</button>
            </div>
        `;
    }

    taskInput.value = "";
}
tasksContainer.onclick = function(e){
    if (e.target.matches(".task button")){
        e.target.parentNode.remove();
    }
    else if (e.target.matches(".task span")){
        e.target.classList.toggle("completed");
    }
}