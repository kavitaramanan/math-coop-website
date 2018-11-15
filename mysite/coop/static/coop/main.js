function deleteObject(obj, name) {
    $.ajax({
        url: "/coop/delete",
        datatype: "json",
        data: {"obj": obj, "name": name},
        success: function(result){
            document.getElementById(`delete${name}`).parentElement.parentElement.remove();
        }});
}

function uploadTopic() {
    name = document.getElementById("newTopicNameInput").value;
    $.ajax({
        url: "/coop/upload_topic",
        datatype: "json",
        data: {"name": name},
        success: function(result){
            newLi = document.createElement("li");
            newLi.innerHTML = `
                <!-- 
                Note div is because of how delete functionality works
                The parent of the parent is removed which we want to be the li not the ul
                -->
                <div>
                    <b>Name</b>: ${name}
                    <button type="submit">Edit</button>
                    <button id="delete${name}" onclick="deleteObject('topic', '${name}')">Delete</button>
                </div>
            `;
            document.getElementById(`manageTopicUL`).appendChild(newLi);
        }});
}

function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

function appendFileInput(i) {
    form = document.getElementById("uploadPresForm");
    button = document.getElementById("addFileInput");
    label = button.parentElement
    
    button.onclick = function() {
        appendFileInput(i+1);
    }
    newInput = document.createElement("input");
    newInput.type = "file";
    newInput.accept = "application/vnd.ms-powerpoint, application/pdf";
    newInput.name = "fileInput";
    newInput.id = `fileInput${i}`;
    form.insertBefore(newInput, label);

    br1 = document.createElement("br");
    br2 = br1.cloneNode();
    form.insertBefore(br1, label);
    form.insertBefore(br2, label);
}

function editTopic(e) {
    
}