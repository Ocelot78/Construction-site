function addlist() {
    let name = "test1"
    let lists = document.getElementById("lists")
    let newButton = document.createElement("button");
    newButton.id = name; 
    newButton.className = "list"
    newButton.onclick = appearlist()
    newButton.innerHTML = "<img src='assets/medium.svg' alt=''><h1>|  </h1>" + name;
    lists.appendChild(newButton)
    
}
