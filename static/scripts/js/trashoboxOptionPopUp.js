var pop = document.getElementById("popmenu");

            function openmenu() {
                var eventy = (event.clientY - 17) + 'px';
                pop.style.top = eventy;
                anim;
                var anim = setInterval(function () {
                    pop.style.right = '10px';
                    clearInterval(anim);
                }, 150);
            }

            function closemenu() {
                pop.style.right = -450 + 'px';
                console.log('close');
            }

            function openfile(link) {
                window.location.href='/trashview?id=' + link;
            }
