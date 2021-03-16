const addBtn = document.getElementById('add');
const body = document.body;
const notesUL = document.getElementById('notes');
addBtn.addEventListener('click',()=>{
    addNewNote();
});
const notes = JSON.parse(localStorage.getItem('notes'));
let i = 0;
if(notes){
    notes.forEach(note=>{
        addNewNote(note);
    });
}
function margin(){
    var random_margin = ["-5px","1px", "5px", "10px","15px","20px"];
  
    return random_margin[Math.floor(Math.random() * random_margin.length)];
}
function rotate(){
    var random_degree = ["rotate(3deg)","rotate(1deg)","rotate(-1deg)","rotate(-3deg)","rotate(-5deg)", "rotate(-10deg)"];
    
    return random_degree[Math.floor(Math.random() * random_degree.length)];
}
  
function color(){
    var random_colors = ["#c2ff3d","#ff3de8","#3dc2ff","#04e022","#bc83e6","#ebb328"];
  
    if(i > random_colors.length - 1){
      i = 0;
    }
    return random_colors[i++];
}
function addNewNote(text=""){
    const note = document.createElement('div');
    note.classList.add('note');

    note.innerHTML = `
        <div class="tools">
            <button class="edit"><i class="fas fa-edit"></i></button>
            <button class="delete"><i class="fas fa-trash-alt"></i></button>
        </div>
        <div class="main ${text ? "":"hidden"}"></div>
        <textarea class="${text ? "hidden":""}"></textarea>
    `;
    const textArea = note.querySelector('textarea');
    const main = note.querySelector('.main');
    const editBtn = note.querySelector('.edit');
    const delBtn = note.querySelector('.delete');
    textArea.value = text;
    main.innerHTML = marked(text);
    main.style.fontSize = "1.3rem";
    main.style.padding = '0.5rem';
    
    note.style.margin = margin();
    note.style.transform = rotate();
    note.style.background = color();

    editBtn.addEventListener('click',()=>{
        main.classList.toggle('hidden');
        textArea.classList.toggle('hidden');
    });
    delBtn.addEventListener('click',()=>{
        note.remove();
        updateLS();
    });
    textArea.addEventListener('input',(e)=>{
        const{value} = e.target;
        main.innerHTML = marked(value);
        updateLS();
    });
    // body.appendChild(note);
    // updateLS(); 
    notesUL.style.padding = '1rem';
    notesUL.appendChild(note);
    updateLS();
}

function updateLS(){
    const notesText = document.querySelectorAll('textarea');
    const notes = [];
    notesText.forEach(noteText=>{
        notes.push(noteText.value);
    });
    localStorage.setItem('notes',JSON.stringify(notes));
}