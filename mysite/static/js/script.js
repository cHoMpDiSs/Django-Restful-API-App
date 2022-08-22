console.log('its working')

main = 'static/css/main.css'
blue = 'static/css/blue.css'
green = 'static/css/green.css'
purple = 'static/css/purple.css'

let theme = localStorage.getItem('theme')

if(theme == null){
    setTheme('light')
}else{
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

for (var i=0; themeDots.length > i; i++){
    themeDots[i].addEventListener('click', function(){
        let mode = this.dataset.mode
        console.log('Option clicked', mode)
        setTheme(mode)
    })
}

function setTheme(mode){
    if(mode == 'light'){
        document.getElementById('theme-style').href=main
    }
    if(mode == 'blue'){
        document.getElementById('theme-style').href=blue
    }
    if(mode == 'green'){
        document.getElementById('theme-style').href=green
    }
    if(mode == 'purple'){
        document.getElementById('theme-style').href=purple
    }

    localStorage.setItem('theme', mode)
}

