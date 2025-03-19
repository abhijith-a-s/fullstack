
// Store uploaded songs
const songs = [];

window.uploadFile = function() {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert('Please select a file.');
        return;
    }

    const file = fileInput.files[0];
    const songUrl = URL.createObjectURL(file);

    // Store the song and update UI
    songs.push({ name: file.name, url: songUrl });
    updateSongList();
    alert(`Uploaded: ${file.name}`);
};

function updateSongList() {
    const songList = document.getElementById('songList');
    songList.innerHTML = '';

    songs.forEach((song, index) => {
        const listItem = document.createElement('li');
        listItem.className = "flex justify-between items-center bg-gray-700 p-3 rounded-lg";
        listItem.innerHTML = `
            <span>${song.name}</span>
            <button onclick="playSong(${index})" class="px-4 py-1 bg-blue-600 rounded-lg hover:bg-blue-700 transition">Play</button>
        `;
        songList.appendChild(listItem);
    });
}

window.playSong = function(index) {
    const audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.src = songs[index].url;
    audioPlayer.play();
};
