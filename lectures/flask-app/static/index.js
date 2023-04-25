fetch("/api/menu-items")
    .then(response => response.json())
    .then(function (response) {
        var menu = document.getElementById("menu")
        for (let el of response) {
            var li = document.createElement("li");
            li.classList.add("nav-item");
            li.innerHTML = "<a href='" + el.link + "' class='nav-link'>" + el.name + "</a>";
            menu.append(li);
        }
    })