# File: timetable_manager.py
# Author: Siyuan Liu
# Student ID: 110459091
# Email ID: liusy088@mymail.unisa.edu.au
# This is my own work as defined by
#   the University's Academic Misconduct Policy.

def create_event(timetable):
    """
    Prompt user to create an event and add it to the timetable.
    Each event has title, day, start time, end time, and optional location.
    """
    print("\nCreate New Event")
    day = input("Enter day (Sun, Mon, Tue, Wed, Thu, Fri, Sat): ").strip()
    if day not in timetable:
        print("Invalid day. Event not created.")
        return
    title = input("Enter event title: ").strip()
    start = input("Enter start time (e.g. 09:00): ").strip()
    end = input("Enter end time (e.g. 10:30): ").strip()
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
    Display timetable in a grid from 9 am to 4 pm with days as columns.
    """
    times = ["12am","1am","2am","3am","4am","5am","6am","7am","8am","9am", "10am", "11am",
             "12pm", "1pm", "2pm", "3pm", "4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm"]
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # Print header
    header = ["     "] + [f"{d:^15}" for d in days]
    print("│".join(header))
    print("─" * len("".join(header)))

    # For each time slot, build row
    for t in times:
        row = [f"{t:<5}"]
        for d in days:
            cell_events = []
            for e in timetable[d]:
                # if event covers this hour
                ev_hour = e['start'].split(':')[0]
                ev_label = ev_hour + ("am" if int(ev_hour) < 12 else "pm")
                if ev_label == t:
                    title = e['title']
                    cell_events.append(title)
            if cell_events:
                cell = "; ".join(cell_events)
                if len(cell) > 15:
                    cell = cell[:12] + "..."
                row.append(f"{cell:^15}")
            else:
                row.append(" " * 15)
        print("│".join(row))

def select_event(timetable, action):
    """
    Helper to select an event by day and index for update or delete.
    Returns (day, index) or (None, None) if invalid.
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
    Prompt user to update an existing event's details.
    """
    print("\nUpdate Event")
    day, idx = select_event(timetable, "update")
    if day is None:
        return
    evt = timetable[day][idx]
    print("Leave blank to keep current value.")
    title = input(f"Title [{evt['title']}]: ").strip()
    start = input(f"Start [{evt['start']}]: ").strip()
    end = input(f"End [{evt['end']}]: ").strip()
    loc = input(f"Location [{evt['location']}]: ").strip()
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
    Prompt user to delete an existing event.
    """
    print("\nDelete Event")
    day, idx = select_event(timetable, "delete")
    if day is None:
        return
    evt = timetable[day].pop(idx)
    print(f"Deleted event: {evt['title']}")

def main():
    """
    Main function for timetable manager.
    Displays menu and handles user commands.
    """
    # initialize empty timetable
    timetable = {
        'Sun': [], 'Mon': [], 'Tue': [], 'Wed': [],
        'Thu': [], 'Fri': [], 'Sat': []
    }

    continuing = True

    while continuing:
        print("\nSchedule Manager")
        print("1. View schedule")
        print("2. Create event")
        print("3. Update event")
        print("4. Delete event")
        print("5. Quit")
        choice = input("Enter choice [1-5]: ").strip()
        if choice == '1':
            view_schedule(timetable)
        elif choice == '2':
            create_event(timetable)
        elif choice == '3':
            update_event(timetable)
        elif choice == '4':
            delete_event(timetable)
        elif choice == '5':
            continuing = False
        else:
            print("Invalid choice.")

# Start the program
main()