from pyscript import when, document


@when("change", "#player_lists")
def update_player_list(e):
        selected_list_key = document.querySelector('#player_lists').value

        print(f"User selected key: {selected_list_key}")

        output_text = PLAYER_LIST.get(selected_list_key, "")
        
        
        document.querySelector('#output').innerText = output_text

PLAYER_LIST = {
           'BB': """
        Enzo Villegas
        Koby Bylon
        Tarcisius Cañete
        Zakari Dimaculangan
        Samantha Nacino
        Charlize Galang
        Aisha Ledesma
        Jade Cabatingan
        """,

          'GH': """
        Seth Ngo
        Vito De Guzman
        Marcus Law
        Ishan Shreshtha
        Jillian Grospe
        Atasha Ko
        Sofia Padojinog
        Selena Galvez
        """,

          'RB': """
        Jalainie Abdullah
        Deryck Tan
        Alejandro Enriquez
        Chili Ong
        Martina Cajucom
        Simrandip Kaur
        Beatrix Vilale
        Khloe Espina
        """,

          'YT': """
        Oscar Barrientos
        Gino Ramos
        Gurnoor Sidhu
        Juanico Ibay
        Ashley Gozum
        Julia Lozano
        Clarisse Casal
        Franzeska Dela Cruz
        """
}
    
