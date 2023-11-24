document.addEventListener("DOMContentLoaded", function() {
    let allData = [];
    const container = document.getElementById('music-videos');
    const searchBox = document.getElementById('search-box');
    const videoCountElement = document.getElementById('video-count');
    const loadMoreButton = document.getElementById('load-more');

    function updateVideoCount() {
        videoCountElement.textContent = `Musiques affichées: ${container.children.length}`;
    }

    function displayVideos(videos, append = true) {
        if (!append) {
            container.innerHTML = '';
        }
        videos.forEach(video => {
            const videoDiv = document.createElement('div');
            videoDiv.classList.add('music-video');
            videoDiv.innerHTML = `
                <h2>${video.song_name} - ${video.artist}</h2>
                <p>Date: ${video.date}</p>
                <p>Lien vers le MV: <a href="${video.video}" target="_blank">${video.video}</a></p>
            `;
            container.appendChild(videoDiv);
        });
        updateVideoCount();
    }

    function loadAllVideos() {
        displayVideos(allData, true);
        updateLoadMoreButton();
    }

    function updateLoadMoreButton() {
        // Afficher le bouton seulement s'il reste des vidéos à charger
        loadMoreButton.style.display = container.children.length < allData.length ? 'block' : 'none';
    }

    function filterVideos() {
        const searchText = searchBox.value.toLowerCase();
        const filteredVideos = allData.filter(video =>
            video.artist.toLowerCase().includes(searchText) || video.song_name.toLowerCase().includes(searchText)
        );
        displayVideos(filteredVideos, false);
        updateLoadMoreButton();
    }

    fetch('/music_videos/')
    .then(response => response.json())
    .then(data => {
        allData = data;
        displayVideos(allData.slice(0, 32), false); // Charger les 32 premiers éléments
        updateLoadMoreButton();
    })
    .catch(error => console.error('Erreur lors de la récupération des données:', error));

    searchBox.addEventListener('input', filterVideos);
    loadMoreButton.addEventListener('click', loadAllVideos);
});
