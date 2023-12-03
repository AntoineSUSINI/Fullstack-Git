document.addEventListener("DOMContentLoaded", function() {
    let allData = [];
    const container = document.getElementById('music-videos');
    const searchBox = document.getElementById('search-box');
    const videoCountElement = document.getElementById('video-count');
    const loadMoreButton = document.getElementById('load-more');
    const sortSelect = document.getElementById('sort-select');

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

    function sortData(criteria) {
        switch (criteria) {
            case 'name-asc':
                allData.sort((a, b) => a.song_name.localeCompare(b.song_name));
                break;
            case 'name-desc':
                allData.sort((a, b) => b.song_name.localeCompare(a.song_name));
                break;
            case 'artist-asc':
                allData.sort((a, b) => a.artist.localeCompare(b.artist));
                break;
            case 'artist-desc':
                allData.sort((a, b) => b.artist.localeCompare(a.artist));
                break;
            case 'date-asc':
                allData.sort((a, b) => new Date(a.date) - new Date(b.date));
                break;
            case 'date-desc':
                allData.sort((a, b) => new Date(b.date) - new Date(a.date));
                break;
        }
        displayVideos(allData, false);
        updateLoadMoreButton();
    }

    function loadAllVideos() {
        displayVideos(allData, true);
        updateLoadMoreButton();
    }

    function updateLoadMoreButton() {
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
        displayVideos(allData.slice(0, 32), false);
        updateLoadMoreButton();
    })
    .catch(error => console.error('Erreur lors de la récupération des données:', error));

    searchBox.addEventListener('input', filterVideos);
    loadMoreButton.addEventListener('click', loadAllVideos);
    sortSelect.addEventListener('change', () => sortData(sortSelect.value));
});
