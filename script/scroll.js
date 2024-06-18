function scroll(dummy_var_to_force_repeat_execution){
    var textAreas = parent.document.querySelectorAll('section.main');
    for (let index = 0; index < textAreas.length; index++) {
        textAreas[index].style.color = 'red'
        textAreas[index].scrollTop = textAreas[index].scrollHeight;
    }
}
scroll();
