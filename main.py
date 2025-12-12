from pyscript import document

def show_club_info(event):
    club = document.querySelector("#club-select").value
    info_box = document.querySelector("#club-info")

    info = "No information available."

    # --- Existing Clubs ---
    if club == "Mutant Rights Club":
        info = (
            "Mutant Rights Club\n"
            "Description: Advocates for equal treatment and safety of mutants.\n"
            "Meeting Time: Mondays 4:00–5:00 PM\n"
            "Location: Peace Hall\n"
            "Advisor: Prof. Xavier\n"
            "Category: Advocacy"
        )

    elif club == "Danger Room Training Club":
        info = (
            "Danger Room Training Club\n"
            "Description: Tactical combat, team exercises, and survival scenarios.\n"
            "Meeting Time: Wednesdays 3:30–5:30 PM\n"
            "Location: Danger Room\n"
            "Advisor: Wolverine\n"
            "Category: Physical Training"
        )

    elif club == "X-Gene Science Society":
        info = (
            "X-Gene Science Society\n"
            "Description: Genetic studies, mutation research, biology workshops.\n"
            "Meeting Time: Fridays 4:00–5:30 PM\n"
            "Location: Science Wing\n"
            "Advisor: Beast\n"
            "Category: Academic"
        )

    elif club == "Cerebro Tech Club":
        info = (
            "Cerebro Tech Club\n"
            "Description: Tech innovation, psychic interface systems, engineering.\n"
            "Meeting Time: Saturday 9:00–11:00 AM\n"
            "Location: Cerebro Chamber Annex\n"
            "Advisor: Forge\n"
            "Category: Technology"
        )

    elif club == "School for Gifted Writers":
        info = (
            "School for Gifted Writers\n"
            "Description: Creative writing using enhanced perception and imagination.\n"
            "Meeting Time: Thursdays 4:00–5:00 PM\n"
            "Location: Library\n"
            "Advisor: Jean Grey\n"
            "Category: Creative"
        )

    elif club == "Holodrome Simulation Club":
        info = (
            "Holodrome Simulation Club\n"
            "Description: Build and test custom holo-environments.\n"
            "Meeting Time: Tuesdays 3:45–5:00 PM\n"
            "Location: Holodrome Wing\n"
            "Advisor: Kitty Pryde\n"
            "Category: Technology"
        )

    elif club == "New Mutants Art Club":
        info = (
            "New Mutants Art Club\n"
            "Description: Visual arts, mutant-inspired creativity, illustration.\n"
            "Meeting Time: Friday 3:00–4:00 PM\n"
            "Location: Art Studio\n"
            "Advisor: Magma\n"
            "Category: Arts"
        )

    elif club == "Alpha Flight Athletics Club":
        info = (
            "Alpha Flight Athletics Club\n"
            "Description: Fitness training, mutant-friendly sports.\n"
            "Meeting Time: Monday & Thursday 3:30–5:00 PM\n"
            "Location: Outdoor Training Grounds\n"
            "Advisor: Northstar\n"
            "Category: Athletics"
        )
    elif club == "Limbo Sorcery Club":
        info = (
            "Limbo Sorcery Club\n"
            "Description: Learn basic mystical theory, portal creation exercises, "
            "and dimensional safety.\n"
            "Meeting Time: Sundays 2:00–4:00 PM\n"
            "Location: Enchanted Room (sealed)\n"
            "Advisor: Magik\n"
            "Category: Mystical Arts"
        )

    elif club == "Phoenix Force Studies":
        info = (
            "Phoenix Force Studies\n"
            "Description: Explore cosmic energy, emotional regulation workshops, "
            "and discussions on power responsibility.\n"
            "Meeting Time: Saturdays 1:00–2:30 PM\n"
            "Location: Meditation Garden\n"
            "Advisor: Jean Grey\n"
            "Category: Cosmic / Emotional Discipline"
        )

    info_box.innerText = info
    document.querySelector("#club-select").addEventListener("change", show_club_info)

