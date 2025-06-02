def display_contacts(contacts):
    for c in contacts:
        props = c.properties
        print(f"{props.get('firstname', '')} {props.get('lastname', '')} – {props.get('email', '')}")

def display_one_contact(contact):
    props = contact.properties
    print(f"{props.get('firstname', '')} {props.get('lastname', '')} – {props.get('email', '')}")