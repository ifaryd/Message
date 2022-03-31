const countEl = document.getElementById('count');

updateCount();

function updateCount() {
	fetch('https://api.countapi.xyz/hit/sunilbehera.online/visits')
	.then(res => res.json())
	.then(res => {
    console.log('Res', res);
		countEl.innerHTML = res.value;
	})
}