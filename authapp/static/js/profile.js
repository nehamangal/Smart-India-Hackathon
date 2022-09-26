window.addEventListener('load', () => {

    const parm = (new URL(window.location)).searchParams;
    const name = parm.get('name')
    const email = parm.get('email')

    document.getElementById('res-name').innerHTML = name;
    document.getElementById('res-email').innerHTML = email;

})