# DA NAPRAVITE MAIN FUNKCIJU KOJA OMOGUCAVA KORISNIKU
# DA ZATRAZI AKCIJU: like, share, subscribe ili save
# I DA SE TA AKCIJA PREKO SAMO JEDNE FUNKCIJE ( Call to action )
# prebacuje u log ( actions listu ) kao dictionary koji ima id
# i name mu je ime akcije. Nakon toga, pitajte korisnika da
# li zeli da ponogi proces. Ako da, onda opet pokrenite funkciju
# rekurzijom

actions_log = []


def main():
    def call_to_action(action_name):
        action_id = 0
        for x in actions_log:
            if x["id"] > action_id:
                action_id = x["id"]

        action_id += 1

        data = {"id": action_id, "name": action_name}
        actions_log.append(data)

    akcija = input("Unesite zeljenu akciju: ")

    if akcija == "like":
        call_to_action("like")
    elif akcija == "share":
        call_to_action("share")
    elif akcija == "subscribe":
        call_to_action("subscribe")
    elif akcija == "save":
        call_to_action("save")

    ponavljanje = input("Da li zelite da ponovite proces: ")
    if ponavljanje == "da":
        main()
