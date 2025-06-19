# File: timetable_manager.py
# Author: Siyuan Liu
# Student ID: 110459091
# Email ID: liusy088@mymail.unisa.edu.au
# This is my own work as defined by
#   the University's Academic Misconduct Policy.

# ---------- Helper utilities ----------
def _normalize_ampm(s):
    """
    Turn a time like ' 3:5Pm ' into '3:05pm'.
    Return None if the format is wrong.
    """
    if not s:
        return None
    s = s.strip().lower().replace(" ", "")
    if s.endswith("am"):
        hm = s[:-2]
        period = "am"
    elif s.endswith("pm"):
        hm = s[:-2]
        period = "pm"
    else:
        return None
    if ":" not in hm:
        return None
    h, m = hm.split(":")
    if not (h.isdigit() and m.isdigit()):
        return None
    h, m = int(h), int(m)
    if h < 1 or h > 12 or m < 0 or m > 59:
        return None
    return f"{h}:{m:02d}{period}"

def time_to_minutes(t):
    """Change time like '3:15pm' into minutes after midnight."""
    t = t.strip().lower()
    period = t[-2:]
    h_m = t[:-2]
    h, m = h_m.split(":")
    h, m = int(h), int(m)
    if period == "am":
        if h == 12:
            h = 0
    else:  # pm
        if h != 12:
            h += 12
    return h * 60 + m
# ----- Week ordering -----
WEEK_DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# This variable can be changed at runtime (set in main)
WEEK_START = 'Sun'

def _get_day_order():
    """Give a list of days that begins from WEEK_START."""
    idx = WEEK_DAYS.index(WEEK_START)
    return WEEK_DAYS[idx:] + WEEK_DAYS[:idx]

def _day_to_index(day):
    """Index of day according to WEEK_START."""
    return _get_day_order().index(day)
# -------------------------
# --------------------------------------

def _has_overlap(day_events, new_start, new_end, skip_index=None):
    """
    Check if new event time crosses with other events.
    skip_index lets us ignore one event (for update).
    """
    ns, ne = time_to_minutes(new_start), time_to_minutes(new_end)
    for idx, ev in enumerate(day_events):
        if skip_index is not None and idx == skip_index:
            continue
        es, ee = time_to_minutes(ev['start']), time_to_minutes(ev['end'])
        if ns < ee and es < ne:
            return True
    return False

def create_event(timetable):
    """
    Ask the user to add a new event to the schedule.
    Event needs a title, day, start time, end time, and maybe a location.
    """
    print("\nCreate New Event")
    day = input("Enter day (Sun, Mon, Tue, Wed, Thu, Fri, Sat): ").strip()
    if day not in timetable:
        print("Invalid day. Event not created.")
        return
    title = input("Enter event title: ").strip()
    while True:
        raw_start = input("Enter start time (e.g. 9:00am): ")
        start = _normalize_ampm(raw_start)
        if start:
            break
        print("Invalid time format. Please use h:mmam/pm.")

    while True:
        raw_end = input("Enter end time (e.g. 10:30am): ")
        end = _normalize_ampm(raw_end)
        if end:
            break
        print("Invalid time format. Please use h:mmam/pm.")
    if time_to_minutes(start) >= time_to_minutes(end):
        print("Start time must be before end time. Event not created.")
        return
    if _has_overlap(timetable[day], start, end):
        print("Event overlaps with an existing event on that day. Event not created.")
        return
    loc = input("Enter location (optional): ").strip()
    event = {
        'title': title,
        'start': start,
        'end': end,
        'location': loc
    }
    timetable[day].append(event)
    print("Event added.")

def view_schedule(timetable):
    """
    Show the schedule as a list by day.
    Each event shows time and details.
    No extra modules are needed.
    """
    # days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days = _get_day_order()

    print("\nYour Weekly Schedule (List View):")
    print("=" * 40)

    for day in days:
        print(f"\n{day}:")
        if not timetable[day]:
            print("  [No events]")
            continue

        sorted_events = sorted(timetable[day], key=lambda e: time_to_minutes(e['start']))

        for event in sorted_events:
            start = event['start']
            end = event['end']
            title = event['title']
            loc = event.get('location', '')
            desc = f"{start} - {end} | {title}"
            if loc:
                desc += f" ({loc})"
            print(f"  {desc}")

def search_events(timetable):
    """
    Search for a word in title or location (not case-sensitive).
    Show results by time. Return (day, index) or (None, None).
    """
    kw = input("Keyword: ").strip().lower()
    if not kw:
        print("Empty keyword.")
        return None, None
    found = []
    for d in timetable:
        for i, ev in enumerate(timetable[d]):
            if kw in ev['title'].lower() or kw in ev.get('location', '').lower():
                found.append((d, i, ev))
    if not found:
        print("No matches.")
        return None, None
    found.sort(key=lambda x: (_day_to_index(x[0]), time_to_minutes(x[2]['start'])))
    print("\nMatches:")
    for n, (d, i, ev) in enumerate(found, 1):
        loc = f" ({ev['location']})" if ev.get('location') else ""
        print(f"  {n}. {d}  {ev['start']}‑{ev['end']} | {ev['title']}{loc}")
    choice = input("Select # to proceed: ").strip()
    if not choice.isdigit():
        print("Invalid choice.")
        return None, None
    sel = int(choice) - 1
    if sel < 0 or sel >= len(found):
        print("Choice out of range.")
        return None, None
    return found[sel][0], found[sel][1]

def select_event(timetable, action):
    """
    Let user choose an event by day and number.
    Return (day, index) or (None, None) if input is wrong.
    """
    day = input(f"Enter day of event to {action}: ").strip()
    if day not in timetable:
        print("Invalid day.")
        return None, None
    events = timetable[day]
    if not events:
        print("No events on that day.")
        return None, None
    for idx, evt in enumerate(events, 1):
        print(f"  {idx}. {evt['start']}-{evt['end']} {evt['title']}")
    choice = input(f"Select event number to {action}: ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return None, None
    idx = int(choice) - 1
    if idx < 0 or idx >= len(events):
        print("Choice out of range.")
        return None, None
    return day, idx

def update_event(timetable):
    """
    Let user to update an existing event's details.
    """
    print("\nUpdate Event")
    use_kw = input("Locate event by (1) day list  (2) keyword [1/2]: ").strip()
    if use_kw == "2":
        day, idx = search_events(timetable)
    else:
        day, idx = select_event(timetable, "update")
    if day is None:
        return
    evt = timetable[day][idx]
    print("Leave blank to keep current value.")
    title = input(f"Title [{evt['title']}]: ").strip()
    start = input(f"Start [{evt['start']}] (e.g. 9:00am): ").strip()
    end = input(f"End [{evt['end']}] (e.g. 10:30am): ").strip()
    loc = input(f"Location [{evt['location']}]: ").strip()

    new_start = start if start else evt['start']
    new_end   = end   if end   else evt['end']

    if time_to_minutes(new_start) >= time_to_minutes(new_end):
        print("Start time must be before end time. Update cancelled.")
        return
    if _has_overlap(timetable[day], new_start, new_end, skip_index=idx):
        print("Updated time overlaps with another event. Update cancelled.")
        return

    if title:
        evt['title'] = title
    if start:
        evt['start'] = start
    if end:
        evt['end'] = end
    if loc or loc == "":
        evt['location'] = loc
    print("Event updated.")

def delete_event(timetable):
    """
    Let user to delete an existing event.
    """
    print("\nDelete Event")
    use_kw = input("Locate event by (1) day list  (2) keyword [1/2]: ").strip()
    if use_kw == "2":
        day, idx = search_events(timetable)
    else:
        day, idx = select_event(timetable, "delete")
    if day is None:
        return
    evt = timetable[day].pop(idx)
    print(f"Deleted event: {evt['title']}")

def main():
    # File: timetable_manager.py
    # Author: Siyuan Liu
    # Student ID: 110459091
    # Email ID: liusy088@mymail.unisa.edu.au
    print("Title: timetable manager")
    print("Author: Siyuan Liu")
    print("Email: liusy088@mymail.unisa.edu.au")

    """
    Main function for timetable manager.
    Displays menu and handles user commands.
    """
    # initialize empty timetable
    timetable = {
        'Sun': [], 'Mon': [], 'Tue': [], 'Wed': [],
        'Thu': [], 'Fri': [], 'Sat': []
    }

    # Ask user which day is considered the first day of the week
    global WEEK_START
    while True:
        first_day = input("Choose first day of week "
                          "(Sun/Mon/Tue/Wed/Thu/Fri/Sat) [Sun]: ").strip().title()
        if not first_day:
            first_day = 'Sun'
        if first_day in WEEK_DAYS:
            WEEK_START = first_day
            break
        print("Invalid day. Please enter a valid three‑letter day abbreviation (e.g., Tue).")

    continuing = True

    while continuing:
        print("\nSchedule Manager")
        print("1. View schedule")
        print("2. Create event")
        print("3. Update event")
        print("4. Delete event")
        print("5. Search events")
        print("6. Quit")
        choice = input("Enter choice [1-6]: ").strip()
        if choice == '1':
            view_schedule(timetable)
        elif choice == '2':
            create_event(timetable)
        elif choice == '3':
            update_event(timetable)
        elif choice == '4':
            delete_event(timetable)
        elif choice == '5':
            search_events(timetable)
        elif choice == '6':
            continuing = False
        else:
            print("Invalid choice.")

# Start the program
main()