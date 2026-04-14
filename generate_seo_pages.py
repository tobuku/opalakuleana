#!/usr/bin/env python3
"""
Opala Kuleana SEO Page Generator
Generates service area pages for opalakuleana.com
Run from repo root: python generate_seo_pages.py
"""

import os, json

OUTPUT_DIR = os.path.join("_pages", "service-areas")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SITE_URL = "https://opalakuleana.com"

SERVICES = [
    "Furniture Removal",
    "Appliance Removal",
    "E-Waste and Electronics Disposal",
    "Construction Debris Hauling",
    "Estate Cleanouts",
    "Yard Waste and Green Waste",
    "Hot Tub Removal",
    "Commercial Cleanouts",
    "Mattress Removal",
    "Storage Unit Cleanouts",
]

TRUST = [
    "Free On-Site Estimates",
    "No Hidden Fees",
    "Locally Owned and Operated",
    "Responsible Disposal",
    "By Appointment",
]

AREAS = [
    {
        "slug": "ahuimanu",
        "title": "Ahuimanu",
        "map": "Ahuimanu+Hawaii",
        "meta": "Junk removal in Ahuimanu, Oahu. Furniture, appliances, yard waste, and full cleanouts. Opala Kuleana serves the Windward side. Free estimates.",
        "lead": "Locally owned junk removal serving Ahuimanu and surrounding Windward communities. Free estimates, no hidden fees.",
        "paras": [
            "Ahuimanu is a valley community on the Windward side, tucked against the Ko'olau range just north of Kaneohe. It's a settled, residential area where families have lived for generations, and over the years it's easy to fill a garage, storage room, or shed with things that no longer serve a purpose. When that day comes, we are the local team to call.",
            "We make the process simple. Schedule a free estimate, we come out and look at what needs to go, give you a straight price, and haul everything away on the spot or at a time that fits your schedule. No vague quotes over the phone.",
            "From single pieces of furniture to full property cleanouts, we handle all kinds of junk removal in Ahuimanu. Our drivers know the Windward roads well and are used to working in residential neighborhoods with tight driveways and limited street access.",
        ],
        "nearby": ["Kaneohe", "Heeia", "Kahaluu", "Waiahole"],
        "faqs": [
            ("Do you serve Ahuimanu Valley properties?", "Yes. We serve Ahuimanu including the valley neighborhoods and surrounding residential areas. We know the area and can navigate tight access points."),
            ("How much does junk removal in Ahuimanu cost?", "Pricing depends on how much space your items take up in our truck. We offer free on-site estimates so you get a firm price before we start. No surprise charges."),
            ("Can you haul yard waste in Ahuimanu?", "Absolutely. Yard waste is one of our most common requests on the Windward side. We take palm fronds, branches, soil, rocks, and general garden debris."),
        ],
    },
    {
        "slug": "aina-haina",
        "title": "Aina Haina",
        "map": "Aina+Haina+Hawaii",
        "meta": "Junk removal in Aina Haina, East Honolulu. Furniture, appliances, estate cleanouts. Opala Kuleana serves East Oahu. Free estimates.",
        "lead": "Serving Aina Haina and East Honolulu with honest, reliable junk removal. Free on-site estimates always.",
        "paras": [
            "Aina Haina is one of East Honolulu's established neighborhoods, known for its quiet streets, ocean views, and a mix of older ranch-style homes and newer construction. Moving, downsizing, or clearing out after a family change? We come to you and take away what you no longer need.",
            "Our team has worked with plenty of Aina Haina homeowners who are transitioning between generations of ownership or preparing a property for sale. Estate cleanouts in particular require care and a systematic approach, and that is something we are experienced with.",
            "From the shopping center area along Kalanianaole to the residential streets above and below the highway, we cover all of Aina Haina. Free estimates, no minimum load required, and transparent pricing before we touch anything.",
        ],
        "nearby": ["Niu Valley", "Kuliouou", "Hawaii Kai", "Kalani Iki"],
        "faqs": [
            ("Do you do estate cleanouts in Aina Haina?", "Yes. Estate cleanouts are a core part of what we do. We work through the property room by room, take what needs to go, and leave the space clean."),
            ("Is there a minimum load size for pickups in Aina Haina?", "No minimum. Whether it's one sofa or a truckload, we'll come out. Pricing is based on volume."),
            ("Do you take appliances in Aina Haina?", "Yes. Refrigerators, washers, dryers, dishwashers, and other major appliances are all things we haul in East Honolulu."),
        ],
    },
    {
        "slug": "ala-moana",
        "title": "Ala Moana",
        "map": "Ala+Moana+Honolulu+Hawaii",
        "meta": "Junk removal in Ala Moana, Honolulu. Condo and apartment cleanouts, furniture removal, appliance hauling. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Ala Moana condos, apartments, and businesses. Free estimates. Honest pricing.",
        "paras": [
            "Ala Moana is one of Honolulu's most active urban neighborhoods, home to high-rise condos, apartment buildings, and a dense mix of retail and residential spaces. When you are moving out of a unit or clearing one out between tenants, junk removal becomes a real logistical challenge in a building setting.",
            "We are experienced with condo and apartment pickups in Ala Moana. We coordinate with building management when needed, work within elevator and loading dock restrictions, and haul everything to the truck cleanly without making a mess of common areas.",
            "Whether you have furniture to clear from a unit, appliances on the lanai, or just a pile of odds and ends that will not fit in the trash chute, give us a call. Free estimate, clear price, no runaround.",
        ],
        "nearby": ["Kakaako", "McCully", "Makiki", "Waikiki"],
        "faqs": [
            ("Can you do junk removal from a high-rise condo in Ala Moana?", "Yes. We handle condo pickups regularly and coordinate elevator access with building management."),
            ("Do you take furniture from apartments in Ala Moana?", "Yes. Sofas, beds, dressers, dining sets, we take it all."),
            ("Do you remove appliances from condos?", "Yes. We haul refrigerators, washers, dryers, and other appliances. For built-in units, let us know in advance so we can come prepared."),
        ],
    },
    {
        "slug": "aliamanu",
        "title": "Aliamanu",
        "map": "Aliamanu+Honolulu+Hawaii",
        "meta": "Junk removal in Aliamanu, Oahu. Furniture, appliances, military family cleanouts. Opala Kuleana serves Aliamanu. Free estimates.",
        "lead": "Serving Aliamanu with dependable junk removal. Free estimates. We handle all kinds of household junk and cleanouts.",
        "paras": [
            "Aliamanu is a quiet residential community in the Salt Lake area, home to a mix of local families and military households connected to nearby bases. Moves happen often in this neighborhood, and when they do, furniture and household goods that cannot make the next trip often need to go.",
            "We regularly help families in Aliamanu with move-out cleanouts, furniture pickup, and appliance removal. Our process is simple: reach out, we come out for a free look, give you a firm price, and haul everything away.",
            "From the military housing side to the civilian neighborhoods, we cover all of Aliamanu. No job is too small, and we will treat your property with the same care we would want for our own home.",
        ],
        "nearby": ["Salt Lake", "Moanalua", "Red Hill", "Aiea"],
        "faqs": [
            ("Do you help military families moving out of Aliamanu?", "Yes. We are familiar with the move cycles that come with military life and we work quickly and professionally to help you get out on time."),
            ("Do you take old mattresses in Aliamanu?", "Yes. Mattress removal is something we handle often. We take all sizes."),
            ("Can you clear out a full apartment in Aliamanu?", "Absolutely. Full unit cleanouts are a common request. We will take everything that needs to go and leave the space empty and clean."),
        ],
    },
    {
        "slug": "campbell-industrial-park",
        "title": "Campbell Industrial Park",
        "map": "Campbell+Industrial+Park+Kapolei+Hawaii",
        "meta": "Junk removal and commercial cleanouts in Campbell Industrial Park, Oahu. Opala Kuleana handles business debris, e-waste, and equipment removal. Free estimates.",
        "lead": "Commercial junk removal and debris hauling for Campbell Industrial Park businesses. Free estimates. Responsible disposal.",
        "paras": [
            "Campbell Industrial Park is the primary industrial zone on the West Side, home to warehouses, distribution centers, contractors, and manufacturing operations. When businesses generate excess debris, old equipment, or material waste, they need a removal crew that understands the commercial side of things.",
            "We work with businesses in Campbell Industrial Park to haul away what you cannot easily get rid of on your own. That includes old shelving and racking, broken equipment, pallets, e-waste, construction debris from tenant improvements, and general commercial junk.",
            "Commercial cleanouts require a different approach than residential jobs. We schedule around your operations, bring the right size truck, and make sure disposal is handled properly, including recycling and e-waste diversion where applicable.",
        ],
        "nearby": ["Kapolei", "Ewa Beach", "Barbers Point", "Kalaeloa"],
        "faqs": [
            ("Do you do commercial junk removal in Campbell Industrial Park?", "Yes. We work with businesses, contractors, and warehouses. We schedule around your hours and bring appropriate equipment."),
            ("Do you haul e-waste from industrial businesses?", "Yes. We handle e-waste and electronics disposal responsibly, keeping it out of the landfill when possible."),
            ("Can you remove large industrial shelving or racking?", "Reach out and describe what you have. For large or specialty items, we assess on-site and let you know what we can take."),
        ],
    },
    {
        "slug": "downtown-honolulu",
        "title": "Downtown Honolulu",
        "map": "Downtown+Honolulu+Hawaii",
        "meta": "Junk removal in Downtown Honolulu. Office cleanouts, condo furniture removal, appliance hauling. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Downtown Honolulu homes, condos, and offices. Honest pricing, free on-site estimates.",
        "paras": [
            "Downtown Honolulu is the city's business and civic core, and it is also home to a growing number of condos, lofts, and residential units. Whether you are a business clearing out an old office space or a resident moving out of a high-rise, we can handle the junk removal side of the equation.",
            "Office cleanouts are something we do often in downtown areas. We can clear out desks, filing cabinets, chairs, servers, monitors, and all the miscellaneous items that pile up over the years in a commercial space. We work efficiently so your team is not waiting around.",
            "For residential clients downtown, we handle everything from single-item pickups to full unit cleanouts before a move or sale. Parking and access in the area can be tricky, but we plan ahead and make it work.",
        ],
        "nearby": ["Kakaako", "Nuuanu", "Chinatown", "Punchbowl"],
        "faqs": [
            ("Do you handle office cleanouts in Downtown Honolulu?", "Yes. Office furniture, filing cabinets, electronics, and general office junk are things we deal with regularly."),
            ("Can you pick up from a parking garage or loading dock downtown?", "Yes. Let us know the access situation when you call and we will plan accordingly."),
            ("How do I schedule junk removal in Downtown Honolulu?", "Fill out our contact form. We will set up a free estimate at a time that works for you."),
        ],
    },
    {
        "slug": "enchanted-lake",
        "title": "Enchanted Lake",
        "map": "Enchanted+Lake+Kailua+Hawaii",
        "meta": "Junk removal in Enchanted Lake, Kailua, Oahu. Furniture, appliances, estate cleanouts. Opala Kuleana serves Windward Oahu. Free estimates.",
        "lead": "Reliable junk removal for Enchanted Lake and the greater Kailua area. Free estimates, upfront pricing.",
        "paras": [
            "Enchanted Lake is a residential neighborhood on the Windward side, adjacent to Kailua and known for its lakeside homes and family-friendly atmosphere. It is a neighborhood where people tend to stay a while, which means garages and storage areas fill up over time.",
            "We provide junk removal for Enchanted Lake homeowners on a regular basis. Whether you are doing a spring cleanout, clearing out for a renovation, or dealing with an estate, we will come out, give you a free estimate, and take care of everything.",
            "Our team is familiar with the Windward side and the residential streets in and around Enchanted Lake. We work by appointment and communicate clearly before, during, and after the job.",
        ],
        "nearby": ["Kailua", "Lanikai", "Kaneohe", "Maunawili"],
        "faqs": [
            ("Do you serve Enchanted Lake specifically, or just Kailua?", "We serve Enchanted Lake directly as well as the surrounding Kailua area."),
            ("What is the fastest way to get a junk removal quote in Enchanted Lake?", "Fill out our online form. We will schedule a free on-site estimate, usually within a day or two."),
            ("Do you take furniture from lakeside homes in Enchanted Lake?", "Yes. Furniture of all types and sizes. We bring the right equipment to handle large pieces."),
        ],
    },
    {
        "slug": "hawaii-kai",
        "title": "Hawaii Kai",
        "map": "Hawaii+Kai+Honolulu+Hawaii",
        "meta": "Junk removal in Hawaii Kai, Oahu. Furniture, appliances, estate cleanouts, and marina area pickups. Opala Kuleana. Free estimates.",
        "lead": "Serving Hawaii Kai with junk removal, estate cleanouts, and appliance hauling. Free estimates always.",
        "paras": [
            "Hawaii Kai is one of Oahu's most desirable East Side communities, known for its marina, scenic views, and well-established homes. Moving, downsizing, or dealing with a property transition in Hawaii Kai? We serve this area regularly and understand what these jobs typically involve.",
            "Estate cleanouts are especially common in Hawaii Kai, where many long-time residents eventually need help clearing out a home. We approach these jobs with care and efficiency, working through the space methodically and hauling away what needs to go.",
            "We also handle smaller jobs: furniture that will not fit in a standard truck, appliances that are past their useful life, construction debris from a renovation, or yard waste from landscaping. No job too big or too small.",
        ],
        "nearby": ["Niu Valley", "Kalama Valley", "Waimanalo", "Kuliouou"],
        "faqs": [
            ("Do you serve homes near the Hawaii Kai Marina?", "Yes, we serve all of Hawaii Kai including neighborhoods around the marina and the Kokohead area."),
            ("What types of items do you take in Hawaii Kai?", "We take furniture, appliances, mattresses, yard waste, construction debris, electronics, and general household junk."),
            ("Do you do estate cleanouts in Hawaii Kai?", "Yes. Estate cleanouts are a specialty. We work through the entire property and haul away everything that needs to go."),
        ],
    },
    {
        "slug": "hickam-housing",
        "title": "Hickam Housing",
        "map": "Hickam+Housing+Oahu+Hawaii",
        "meta": "Junk removal for Hickam Housing, Joint Base Pearl Harbor-Hickam, Oahu. Furniture, appliances, PCS move cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Hickam Housing military families. We understand PCS timelines. Free estimates.",
        "paras": [
            "Hickam Housing, part of Joint Base Pearl Harbor-Hickam, is home to Air Force and other service members and their families. PCS moves come with tight timelines and a lot of logistics, and getting rid of furniture and household items that will not make the move is often one of the last things people deal with.",
            "We work with military families in the Hickam area to make the cleanout part of a PCS move as fast and stress-free as possible. We come prepared to haul multiple items in a single trip and are used to working under time pressure.",
            "We are a civilian business and do not operate on base. For off-base housing areas associated with Hickam, contact us directly and we will confirm access and schedule a visit.",
        ],
        "nearby": ["Pearl Harbor", "Iroquois Point", "Ewa Beach", "Aiea"],
        "faqs": [
            ("Can you access Hickam Housing for junk removal?", "Access depends on the specific housing area. Contact us and we will work out the logistics based on your situation."),
            ("Do you help with PCS move cleanouts near Hickam?", "Yes. We understand the time pressure of military moves and work quickly and efficiently."),
            ("What items can you take from Hickam-area housing?", "Furniture, appliances, mattresses, electronics, and general household junk. Let us know what you have when you reach out."),
        ],
    },
    {
        "slug": "iroquois-point",
        "title": "Iroquois Point",
        "map": "Iroquois+Point+Oahu+Hawaii",
        "meta": "Junk removal for Iroquois Point, Oahu. Military family cleanouts, furniture and appliance removal. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Iroquois Point and the Ewa area. Free estimates, dependable service.",
        "paras": [
            "Iroquois Point is a residential community on a peninsula at the entrance to Pearl Harbor, primarily home to military families. The pace of military life means frequent moves, and clearing out a home quickly and properly is a recurring need.",
            "We assist Iroquois Point residents with furniture removal, appliance hauling, and full household cleanouts. We work by appointment and make sure the job is done right the first time so you can check it off your move-out list.",
            "Reach out through our contact form with details on what you need removed and your general availability. We will get back to you quickly to set up a free estimate.",
        ],
        "nearby": ["Ewa Beach", "Hickam Housing", "Barbers Point", "Kapolei"],
        "faqs": [
            ("Do you serve Iroquois Point for junk removal?", "Yes. We serve Iroquois Point and surrounding Ewa area communities."),
            ("What is the best way to schedule a pickup at Iroquois Point?", "Fill out our contact form. We will confirm the location and schedule your free estimate."),
            ("Do you haul furniture and large items at Iroquois Point?", "Yes. Furniture, appliances, mattresses, and general household junk."),
        ],
    },
    {
        "slug": "kaimuki",
        "title": "Kaimuki",
        "map": "Kaimuki+Honolulu+Hawaii",
        "meta": "Junk removal in Kaimuki, Honolulu. Furniture, appliances, cleanouts for older homes. Opala Kuleana serves East Honolulu. Free estimates.",
        "lead": "Junk removal in Kaimuki and surrounding East Honolulu neighborhoods. Free on-site estimates, upfront pricing.",
        "paras": [
            "Kaimuki is a beloved East Honolulu neighborhood with a mix of small bungalows, craftsman homes, and some newer construction. It has a tight-knit community feel, and many homes here have been owned by the same families for decades, which means storage areas, garages, and sheds tend to fill up over the years.",
            "We work with Kaimuki homeowners to clear out furniture, appliances, yard debris, and all the odds and ends that accumulate in a well-lived home. Our team shows up on time, gives you a straight price, and gets the work done without leaving a mess behind.",
            "Kaimuki's streets can be narrow and driveways are often small or shared. That is not new to us. We are experienced with older Honolulu neighborhoods and know how to work in tight spaces.",
        ],
        "nearby": ["Kapahulu", "Palolo", "Aina Haina", "Diamond Head"],
        "faqs": [
            ("Do you serve older homes in Kaimuki with limited driveway access?", "Yes. Tight driveways and narrow streets are common in Kaimuki and not a problem for our team."),
            ("Can you haul old furniture from a Kaimuki bungalow?", "Absolutely. Furniture removal is one of our most common jobs in older Honolulu neighborhoods."),
            ("Do you take yard waste in Kaimuki?", "Yes. Garden debris, palm fronds, branches, and general yard waste are all things we haul."),
        ],
    },
    {
        "slug": "kakaako",
        "title": "Kakaako",
        "map": "Kakaako+Honolulu+Hawaii",
        "meta": "Junk removal in Kakaako, Honolulu. Condo cleanouts, furniture removal, appliance hauling. Opala Kuleana. Free estimates.",
        "lead": "Condo and apartment junk removal in Kakaako. Honest pricing, free estimates, clean and efficient service.",
        "paras": [
            "Kakaako has transformed over the last decade into one of Honolulu's most active condo development zones. Ward Village and surrounding developments have brought thousands of new units to the area, and with that comes steady demand for move-out cleanouts and furniture removal.",
            "We handle junk removal from Kakaako condos regularly. We work within building rules, coordinate elevator access when needed, and haul everything out without disturbing neighbors or making a mess of common areas.",
            "Whether you are a property manager clearing a unit between tenants or a resident moving on to the next chapter, we will give you a fair price and take everything that needs to go.",
        ],
        "nearby": ["Ala Moana", "Downtown Honolulu", "Ward", "McCully"],
        "faqs": [
            ("Do you do condo cleanouts in Kakaako?", "Yes. We handle Kakaako condo cleanouts often and are familiar with the building access requirements in the area."),
            ("Can you remove furniture from a high-rise in Kakaako?", "Yes. We coordinate with building management for elevator and loading dock access."),
            ("What does junk removal cost in Kakaako?", "Pricing is based on volume. Get a free on-site estimate and we will give you a firm number before starting."),
        ],
    },
    {
        "slug": "kaneohe-bay",
        "title": "Kaneohe Bay",
        "map": "Kaneohe+Bay+Hawaii",
        "meta": "Junk removal near Kaneohe Bay, Oahu. Windward furniture removal, yard waste, estate cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Serving the Kaneohe Bay area with junk removal and cleanouts. Free estimates, dependable Windward-side service.",
        "paras": [
            "The Kaneohe Bay area covers a stretch of Windward Oahu with scenic bayfront communities, residential neighborhoods, and rural properties. Whether you are near the bay itself or up in one of the inland areas, we provide junk removal throughout this region.",
            "We haul furniture, appliances, green waste, and debris from homes throughout the Kaneohe Bay corridor. Properties near the water often have older items stored outdoors that need to go, and we are happy to take them.",
            "Free estimates and honest pricing apply here just like everywhere else we work. Contact us, tell us what you have, and we will set up a time to come out and take a look.",
        ],
        "nearby": ["Kaneohe", "Heeia", "Ahuimanu", "Kaaawa"],
        "faqs": [
            ("Do you serve properties near the bay shoreline?", "Yes. We serve bayfront properties and all neighborhoods in the Kaneohe Bay area."),
            ("Can you remove outdoor items stored near the water?", "Yes. We take outdoor furniture, equipment, debris, and other items stored outside, subject to weight and size."),
            ("Do you haul yard waste on the Windward side?", "Yes. Yard and green waste is common in this area. We take it all."),
        ],
    },
    {
        "slug": "kapahulu",
        "title": "Kapahulu",
        "map": "Kapahulu+Honolulu+Hawaii",
        "meta": "Junk removal in Kapahulu, Honolulu. Furniture, appliances, apartment and home cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Kapahulu and the surrounding Honolulu corridor. Free estimates, clear pricing.",
        "paras": [
            "Kapahulu runs between Waikiki and Kaimuki, a busy commercial and residential corridor with everything from small homes to apartment buildings. Junk removal in this area often involves tight spaces, street parking challenges, and building-specific access rules.",
            "We are comfortable working in Kapahulu's mixed-use environment. We have done plenty of pickups from apartment units, small homes, and commercial spaces along this corridor. We adapt to the situation and make it work.",
            "Tell us what you need removed and where you are located. We will give you a free estimate and schedule a pickup at a time that works.",
        ],
        "nearby": ["Kaimuki", "Waikiki", "Manoa", "Diamond Head"],
        "faqs": [
            ("Do you serve apartment buildings along Kapahulu?", "Yes. We handle pickups from apartment units and work within building access requirements."),
            ("Can you remove furniture from small homes in Kapahulu?", "Yes. Small homes, bungalows, and older properties are a regular part of our work in this area."),
            ("How do I get a quote for junk removal in Kapahulu?", "Contact us through our form. We will schedule a free on-site estimate."),
        ],
    },
    {
        "slug": "lanikai",
        "title": "Lanikai",
        "map": "Lanikai+Kailua+Hawaii",
        "meta": "Junk removal in Lanikai, Oahu. Estate cleanouts, furniture removal, appliance hauling. Opala Kuleana serves Windward Oahu. Free estimates.",
        "lead": "Junk removal for Lanikai and the Kailua area. Respectful service for residential properties. Free estimates.",
        "paras": [
            "Lanikai is a small, exclusive beachside community on the Windward side, just south of Kailua. The neighborhood is made up of private homes, many of which have been in families for years. When cleanout time comes, whether for a move, sale, or estate, we handle it with care.",
            "We understand that Lanikai properties are often significant, and we treat every job with the professionalism it deserves. Our team is punctual, respectful, and focused on getting the work done right.",
            "Free estimates apply to Lanikai just like everywhere else we work. Give us a call or fill out the contact form and we will set up a time.",
        ],
        "nearby": ["Kailua", "Enchanted Lake", "Waimanalo", "Maunawili"],
        "faqs": [
            ("Do you serve Lanikai for junk removal?", "Yes. We serve Lanikai and all of the Kailua area on the Windward side."),
            ("Do you take furniture from beachside homes in Lanikai?", "Yes. All types of furniture, regardless of size or material."),
            ("Can you handle an estate cleanout in Lanikai?", "Yes. We have experience with estate cleanouts and approach them carefully and methodically."),
        ],
    },
    {
        "slug": "mccully",
        "title": "McCully",
        "map": "McCully+Honolulu+Hawaii",
        "meta": "Junk removal in McCully, Honolulu. Apartment cleanouts, furniture removal, appliances. Opala Kuleana serves McCully and Moiliili. Free estimates.",
        "lead": "Junk removal in McCully and Moiliili. Free estimates, dependable service for apartments and homes.",
        "paras": [
            "McCully is one of Honolulu's densely populated urban neighborhoods, filled with apartment buildings, small homes, and a high turnover of renters. Junk removal in McCully tends to involve a lot of apartment move-outs and unit cleanouts between tenants.",
            "We work with both individual tenants and property managers in McCully. Our process is the same regardless of scale: come out, assess, give a firm price, and haul it away. We are efficient because we have to be in a neighborhood where parking is limited and loading windows are short.",
            "Contact us with your address and a general sense of what needs to go. We will schedule a quick estimate visit and get it handled.",
        ],
        "nearby": ["Moiliili", "Ala Moana", "Kapahulu", "Manoa"],
        "faqs": [
            ("Do you do apartment move-out cleanouts in McCully?", "Yes. Apartment cleanouts are a regular part of our McCully work. We haul everything left behind."),
            ("Can you pick up from a unit without elevator access?", "Yes. We handle walk-up buildings. Let us know the floor when you contact us."),
            ("Do you work with property managers in McCully?", "Yes. We work with property management companies for multiple-unit and recurring cleanout needs."),
        ],
    },
    {
        "slug": "moanalua",
        "title": "Moanalua",
        "map": "Moanalua+Honolulu+Hawaii",
        "meta": "Junk removal in Moanalua, Oahu. Furniture, appliances, full household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Moanalua and surrounding neighborhoods. Free estimates, local team, honest pricing.",
        "paras": [
            "Moanalua is a residential community between Honolulu and Aiea, home to military families and local residents in a mix of single-family homes and apartment complexes. The proximity to Tripler Army Medical Center and Fort Shafter means we see a fair share of military-related move-out cleanouts here.",
            "We provide junk removal in Moanalua for homes, apartments, and families in transition. From a single sofa pickup to a full property cleanout, we quote upfront and get the work done on schedule.",
            "If you are in Moanalua Gardens or the surrounding neighborhoods, we are familiar with the area and can accommodate most pickup situations.",
        ],
        "nearby": ["Aliamanu", "Salt Lake", "Aiea", "Fort Shafter"],
        "faqs": [
            ("Do you serve the Moanalua Gardens neighborhood?", "Yes. We serve Moanalua Gardens and all surrounding residential areas."),
            ("Can you help with military move-out cleanouts in Moanalua?", "Yes. We are experienced with fast, efficient cleanouts for military transitions."),
            ("What items can you take in Moanalua?", "Furniture, appliances, electronics, mattresses, yard waste, and general household junk."),
        ],
    },
    {
        "slug": "niu-valley",
        "title": "Niu Valley",
        "map": "Niu+Valley+Honolulu+Hawaii",
        "meta": "Junk removal in Niu Valley, East Honolulu. Furniture removal, appliances, estate cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Niu Valley and East Honolulu. Free estimates, upfront pricing, reliable service.",
        "paras": [
            "Niu Valley is a quiet, established neighborhood on the East Side of Honolulu, tucked between Aina Haina and Hawaii Kai. It is a predominantly residential area with homes that have stood for decades, and when people need to clear out a property, we are the local team they call.",
            "We handle all kinds of removal in Niu Valley: furniture, appliances, yard debris, construction leftovers, and full estate cleanouts. We work by appointment and always give you a firm price before we start.",
            "If you are in Niu Valley and need to get rid of something, reach out. We will come out for a free look and let you know exactly what it will cost.",
        ],
        "nearby": ["Aina Haina", "Hawaii Kai", "Kuliouou", "Kalani Iki"],
        "faqs": [
            ("Do you serve Niu Valley for junk removal?", "Yes. Niu Valley is within our East Honolulu service area."),
            ("Can you do a full home cleanout in Niu Valley?", "Yes. We do full property and estate cleanouts throughout East Honolulu."),
            ("Do you take appliances from Niu Valley homes?", "Yes. All major appliances, including refrigerators, washers, and dryers."),
        ],
    },
    {
        "slug": "palolo",
        "title": "Palolo",
        "map": "Palolo+Honolulu+Hawaii",
        "meta": "Junk removal in Palolo Valley, Honolulu. Furniture, appliances, full household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Palolo and surrounding Honolulu neighborhoods. Free estimates, straightforward pricing.",
        "paras": [
            "Palolo Valley is a residential valley community in East Honolulu, bordered by Manoa and Kaimuki. Like many valley neighborhoods in Honolulu, it has a dense residential character with lots of long-term residents and older housing stock that can accumulate a lifetime of belongings.",
            "We regularly provide junk removal in Palolo for homeowners clearing out extra rooms, landlords turning over rental units, and families dealing with estate situations. We haul furniture, appliances, yard waste, and all kinds of general junk.",
            "Palolo streets can be narrow in places, but navigating tight residential neighborhoods is something we do every day. Contact us and we will schedule a free estimate.",
        ],
        "nearby": ["Kaimuki", "Manoa", "Diamond Head", "St. Louis Heights"],
        "faqs": [
            ("Do you serve Palolo Valley for junk removal?", "Yes. Palolo is within our service area and we do pickups there regularly."),
            ("Do you haul furniture from rental properties in Palolo?", "Yes. Landlords and property managers use our service regularly for unit turnovers."),
            ("Is there a minimum load for Palolo pickups?", "No minimum. Whether it is one piece or a full truckload, we will come out."),
        ],
    },
    {
        "slug": "punchbowl",
        "title": "Punchbowl",
        "map": "Punchbowl+Honolulu+Hawaii",
        "meta": "Junk removal in Punchbowl, Honolulu. Furniture removal, appliances, household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Punchbowl and Nuuanu. Free estimates, local team that knows the neighborhood.",
        "paras": [
            "Punchbowl is one of Honolulu's historic residential craters, home to a tight community of long-established families and a number of older homes on narrow, winding streets. It is the kind of neighborhood where properties have history and storage spaces have been building up for years.",
            "We serve Punchbowl for furniture removal, appliance hauling, and full property cleanouts. The winding roads and limited access at certain addresses are not new territory for us. We assess the logistics before committing to a price and we show up with the right equipment.",
            "Whether you are clearing out a room, downsizing, or handling an estate, we will make the junk removal part simple.",
        ],
        "nearby": ["Downtown Honolulu", "Nuuanu", "Makiki", "Pacific Heights"],
        "faqs": [
            ("Can you access homes on the steep streets in Punchbowl?", "We assess access during the free estimate. Most Punchbowl properties are accessible with our equipment."),
            ("Do you take large furniture from older Punchbowl homes?", "Yes. We take all types and sizes of furniture, including bulky pieces from older homes."),
            ("How do I get a junk removal estimate in Punchbowl?", "Fill out our contact form. We will schedule a visit and give you a firm price before any work starts."),
        ],
    },
    {
        "slug": "salt-lake",
        "title": "Salt Lake",
        "map": "Salt+Lake+Honolulu+Hawaii",
        "meta": "Junk removal in Salt Lake, Honolulu. Condo cleanouts, furniture removal, appliances. Opala Kuleana serves Salt Lake and Aliamanu. Free estimates.",
        "lead": "Junk removal in Salt Lake. Condos, apartments, single-family homes. Free estimates, upfront pricing.",
        "paras": [
            "Salt Lake is an urban neighborhood in the Moanalua corridor, home to a dense mix of condos, apartments, and smaller single-family homes. It is a practical, working neighborhood with a lot of rental turnover, and junk removal is a frequent need when units change hands.",
            "We serve Salt Lake for apartment and condo cleanouts, furniture removal, appliance hauling, and all types of household junk pickup. Our process is simple and transparent: we visit, quote, and haul.",
            "Property managers in Salt Lake use us regularly. If you manage multiple units and need a reliable removal service, reach out and we can talk about how we work with recurring clients.",
        ],
        "nearby": ["Aliamanu", "Moanalua", "Red Hill", "Aiea"],
        "faqs": [
            ("Do you serve condo buildings in Salt Lake?", "Yes. We handle condo and apartment pickups throughout Salt Lake."),
            ("Can you do a move-out cleanout in Salt Lake on short notice?", "Contact us and we will do our best to fit you in. We know move timelines can be tight."),
            ("Do you work with property managers in Salt Lake?", "Yes. We work with property managers for regular and one-time cleanouts."),
        ],
    },
    {
        "slug": "schofield-barracks",
        "title": "Schofield Barracks",
        "map": "Schofield+Barracks+Hawaii",
        "meta": "Junk removal near Schofield Barracks, Oahu. Military family furniture removal, PCS cleanouts. Opala Kuleana serves Central Oahu. Free estimates.",
        "lead": "Junk removal for military families near Schofield Barracks. Fast, dependable service. Free estimates.",
        "paras": [
            "Schofield Barracks is the U.S. Army's largest installation in Hawaii, located in central Oahu near Wahiawa. Military families stationed here go through the same PCS cycles as anywhere else, and furniture or household items that cannot make the move often need to be dealt with quickly.",
            "We help military families in the Schofield Barracks area clear out before a move. We work by appointment, we are punctual, and we get the job done without a lot of back-and-forth. Just tell us what you have and when you need it gone.",
            "We are a civilian business and do not operate on post. For housing in off-post areas associated with Schofield, contact us and we will confirm access and schedule accordingly.",
        ],
        "nearby": ["Wahiawa", "Wheeler Army Airfield", "Mililani", "Whitmore Village"],
        "faqs": [
            ("Do you serve off-post housing near Schofield Barracks?", "Yes. We serve off-post and community housing areas. Contact us to confirm your specific address."),
            ("Can you help with a PCS move cleanout near Schofield?", "Yes. We are experienced with military move timelines and work efficiently."),
            ("What items do you take near Schofield Barracks?", "Furniture, appliances, mattresses, electronics, yard waste, and general household items."),
        ],
    },
    {
        "slug": "tripler-army-medical-center",
        "title": "Tripler Army Medical Center",
        "map": "Tripler+Army+Medical+Center+Honolulu+Hawaii",
        "meta": "Junk removal near Tripler Army Medical Center, Oahu. Military community furniture removal and cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for the Tripler Army Medical Center community. Free estimates, dependable service.",
        "paras": [
            "Tripler Army Medical Center sits on the Moanalua Ridge above Honolulu, and the surrounding area is home to military staff, medical personnel, and their families. Transitions are frequent in this community, whether from reassignments or changes in housing status.",
            "We serve the residential communities in and around Tripler with junk removal, furniture hauling, and cleanouts. Our team is professional, efficient, and familiar with working in military-adjacent communities.",
            "For specific housing areas, contact us with your address and we will confirm service availability and schedule a free estimate.",
        ],
        "nearby": ["Moanalua", "Aliamanu", "Salt Lake", "Red Hill"],
        "faqs": [
            ("Do you serve the Tripler area for junk removal?", "Yes. We serve residential areas in and around Tripler Army Medical Center."),
            ("Can you help with move-out cleanouts near Tripler?", "Yes. We are experienced with fast, efficient cleanouts for military transitions."),
            ("What is the process for scheduling junk removal near Tripler?", "Fill out our contact form. We will confirm your location and schedule a free estimate."),
        ],
    },
    {
        "slug": "wheeler-army-airfield",
        "title": "Wheeler Army Airfield",
        "map": "Wheeler+Army+Airfield+Hawaii",
        "meta": "Junk removal near Wheeler Army Airfield, Oahu. Military family furniture removal, PCS cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for military families near Wheeler Army Airfield. Fast, honest service. Free estimates.",
        "paras": [
            "Wheeler Army Airfield is located in Wahiawa in central Oahu, near Schofield Barracks. Military families in the Wheeler community often need quick junk removal help during PCS moves when furniture or household items cannot come along.",
            "We provide junk removal for the Wheeler-area community, focusing on fast scheduling, clear pricing, and getting the work done right so families can focus on the move itself.",
            "We are a civilian business and do not operate on post. For off-post or community housing, contact us and we will confirm access and schedule a visit.",
        ],
        "nearby": ["Schofield Barracks", "Wahiawa", "Mililani", "Whitmore Village"],
        "faqs": [
            ("Do you serve off-post housing near Wheeler?", "Yes. For community and off-post housing areas, contact us to confirm access and scheduling."),
            ("How quickly can you do a junk removal in the Wheeler area?", "We schedule based on current availability. Contact us and we will find the earliest slot."),
            ("What types of items do you take near Wheeler?", "Furniture, appliances, mattresses, yard waste, electronics, and general household junk."),
        ],
    },
    {
        "slug": "aiea",
        "title": "Aiea",
        "map": "Aiea+Hawaii",
        "meta": "Junk removal in Aiea, Oahu. Furniture, appliances, full household cleanouts near Pearl Harbor. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Aiea and the Pearl Harbor corridor. Free estimates, local crew, honest pricing.",
        "paras": [
            "Aiea sits along the Pearl Harbor waterway and is one of Oahu's established mid-island communities. It is a mix of longtime local families and newer residents, with a range of housing from older single-family homes to newer condos and townhouses.",
            "We provide junk removal throughout Aiea on a regular basis. Whether it is clearing out a garage that has been accumulating for years or handling a full estate cleanout, we come out, give you a fair price, and get it done.",
            "Aiea is centrally located, which makes scheduling easy for us. We are typically able to get out for estimates quickly, and we do not charge extra for the Pearl Harbor corridor area.",
        ],
        "nearby": ["Pearl City", "Halawa", "Waimalu", "Moanalua"],
        "faqs": [
            ("Do you serve all of Aiea for junk removal?", "Yes. We serve Aiea Heights, lower Aiea, and all surrounding neighborhoods."),
            ("Can you haul construction debris from an Aiea renovation?", "Yes. Construction debris hauling is one of our core services."),
            ("Do you take appliances in Aiea?", "Yes. All major appliances, picked up and properly disposed of."),
        ],
    },
    {
        "slug": "ewa-beach",
        "title": "Ewa Beach",
        "map": "Ewa+Beach+Hawaii",
        "meta": "Junk removal in Ewa Beach, Oahu. Furniture, appliances, yard waste, and full cleanouts. Opala Kuleana serves West Oahu. Free estimates.",
        "lead": "Serving Ewa Beach with dependable junk removal. Free estimates, no hidden fees.",
        "paras": [
            "Ewa Beach has grown rapidly over the past two decades into one of Oahu's largest master-planned communities. New homes are great until you realize the garage is full and you need to clear things out. We help Ewa Beach residents with exactly that.",
            "We haul furniture, appliances, yard waste, construction debris, mattresses, and all kinds of household junk from Ewa Beach homes. We are on the West Side regularly and know the neighborhoods well.",
            "Free estimates apply to Ewa Beach just like everywhere else. Fill out the form, we will come out and give you a price before we start.",
        ],
        "nearby": ["Ewa Gentry", "Kapolei", "Iroquois Point", "Ocean Pointe"],
        "faqs": [
            ("Do you serve all of Ewa Beach for junk removal?", "Yes. We cover Ocean Pointe, Kalaeloa, and all Ewa Beach subdivisions."),
            ("Can you take yard waste and green waste in Ewa Beach?", "Yes. Yard waste is a common request. We haul palm fronds, branches, and garden debris."),
            ("What does junk removal cost in Ewa Beach?", "It depends on volume. We give free on-site estimates so you know the price before we start."),
        ],
    },
    {
        "slug": "ewa-gentry",
        "title": "Ewa Gentry",
        "map": "Ewa+Gentry+Oahu+Hawaii",
        "meta": "Junk removal in Ewa Gentry, Oahu. Furniture, appliances, yard waste, and full household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Ewa Gentry and West Oahu. Free estimates, straight pricing, local team.",
        "paras": [
            "Ewa Gentry is one of the newer planned communities on West Oahu, with a lot of young families settling into homes for the first time or the second. Over time, things pile up, renovations happen, and suddenly you need to clear out a lot more than the trash bins can handle.",
            "We serve Ewa Gentry with furniture removal, appliance hauling, yard waste pickup, and full cleanouts. We are in this part of the island regularly and can usually schedule estimates quickly.",
            "Fill out the contact form with what you need and your preferred timing. We will get back to you to confirm the visit.",
        ],
        "nearby": ["Ewa Beach", "Kapolei", "Makakilo", "Ho'opili"],
        "faqs": [
            ("Do you serve the Ewa Gentry planned community?", "Yes. We cover all of Ewa Gentry and surrounding West Oahu neighborhoods."),
            ("Can you haul furniture from a newer home in Ewa Gentry?", "Yes. All furniture types, regardless of size."),
            ("Do you take yard waste in Ewa Gentry?", "Yes. Yard and garden debris, palm fronds, and green waste."),
        ],
    },
    {
        "slug": "haleiwa",
        "title": "Haleiwa",
        "map": "Haleiwa+Hawaii",
        "meta": "Junk removal in Haleiwa, North Shore Oahu. Furniture, appliances, yard waste, and farm debris. Opala Kuleana. Free estimates.",
        "lead": "Serving Haleiwa and the North Shore with junk removal. Free estimates, no runaround.",
        "paras": [
            "Haleiwa is the historic heart of Oahu's North Shore, a town that mixes old plantation-era character with a modern surf culture. Properties here range from small bungalows to larger rural lots, and cleanout needs vary widely.",
            "We serve Haleiwa and the surrounding North Shore area for junk removal. We haul furniture, appliances, yard and farm debris, and general household junk. The longer drive from town is factored into our pricing, and we tell you upfront.",
            "If you are on the North Shore and need something hauled away, reach out. We work by appointment and make the trip worth it.",
        ],
        "nearby": ["Waialua", "Pupukea", "Waimea", "Kahuku"],
        "faqs": [
            ("Do you serve rural properties in Haleiwa and the North Shore?", "Yes. Rural lots and larger properties are something we handle. Let us know what you have."),
            ("Is there a travel fee for Haleiwa?", "We price based on volume and haul distance. We will be upfront about any trip charge when you get your estimate."),
            ("Do you take farm or agricultural debris in Haleiwa?", "Some types, yes. Contact us with specifics and we will let you know what we can take."),
        ],
    },
    {
        "slug": "hauula",
        "title": "Hauula",
        "map": "Hauula+Hawaii",
        "meta": "Junk removal in Hauula, North Shore Oahu. Furniture, appliances, yard waste. Opala Kuleana serves Windward and North Shore communities. Free estimates.",
        "lead": "Junk removal in Hauula and surrounding North Shore communities. Free estimates, honest pricing.",
        "paras": [
            "Hauula is a small coastal community on the Windward side of Oahu, between Laie and Kaaawa. It is a rural, community-oriented area where properties tend to have more outdoor space and storage than urban Honolulu homes.",
            "We provide junk removal in Hauula for households dealing with accumulated items, outdoor furniture and equipment, appliances, and yard debris. The drive out is longer, but we factor that in fairly and make the trip worth your time.",
            "Contact us with your address and what needs to go. We will schedule a free estimate and discuss timing.",
        ],
        "nearby": ["Laie", "Kaaawa", "Punaluu", "Kahuku"],
        "faqs": [
            ("Do you make the drive to Hauula for junk removal?", "Yes. We serve Hauula and nearby Windward North Shore communities."),
            ("What types of items do you take in Hauula?", "Furniture, appliances, yard debris, outdoor items, electronics, and general junk."),
            ("Is there a minimum for a Hauula pickup?", "We price by volume. Contact us and we will give you a fair estimate based on what you have."),
        ],
    },
    {
        "slug": "honolulu",
        "title": "Honolulu",
        "map": "Honolulu+Hawaii",
        "meta": "Junk removal in Honolulu, Oahu. Furniture, appliances, estate cleanouts, commercial cleanouts. Opala Kuleana serves all of Honolulu. Free estimates.",
        "lead": "Full-service junk removal throughout Honolulu. Free estimates, honest pricing, local crew.",
        "paras": [
            "Honolulu is the urban core of Oahu and our primary service area. From Kalihi to Diamond Head, from Nuuanu to the waterfront, we cover the full city for junk removal. Whether you are in a high-rise condo, a small bungalow, or a commercial space, we have got you covered.",
            "Our Honolulu jobs range from single-item pickups to full estate cleanouts, office clearances, and apartment unit turnovers. We are comfortable navigating the city's various access situations, from underground parking to loading docks to narrow residential lanes.",
            "Same formula applies city-wide: contact us, we come out for a free estimate, give you a firm price, and haul everything away on schedule.",
        ],
        "nearby": ["Waikiki", "Kalihi", "Manoa", "Downtown Honolulu", "Nuuanu"],
        "faqs": [
            ("Do you serve all Honolulu neighborhoods?", "Yes. We cover the full city of Honolulu from Kalihi to Hawaii Kai."),
            ("Can you do same-week junk removal in Honolulu?", "Often yes. Contact us and we will find the nearest available slot."),
            ("Do you haul junk from commercial properties in Honolulu?", "Yes. Office cleanouts, retail spaces, and commercial junk removal are all within our scope."),
        ],
    },
    {
        "slug": "kaaawa",
        "title": "Kaaawa",
        "map": "Kaaawa+Hawaii",
        "meta": "Junk removal in Kaaawa, Oahu. Windward community furniture removal, appliances, yard waste. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Kaaawa and the Windward Coast. Free estimates, local service.",
        "paras": [
            "Kaaawa is a small, tight-knit community on the Windward Coast, known for its scenic beauty and slow pace. Properties here are often larger and more rural than what you find in town, and junk removal needs tend to reflect that: more outdoor furniture, farm equipment, and yard debris.",
            "We make the trip to Kaaawa for junk removal pickups. It is a longer drive, but we factor that in fairly and will not charge you more than is reasonable. Contact us with what you have and we will discuss pricing honestly.",
            "If you are dealing with a full property cleanout or just a few large items in Kaaawa, we are the team to call.",
        ],
        "nearby": ["Hauula", "Punaluu", "Kahuku", "Kaneohe Bay"],
        "faqs": [
            ("Do you travel to Kaaawa for junk removal?", "Yes. We serve Kaaawa and the surrounding Windward Coast communities."),
            ("How is pricing handled for distant areas like Kaaawa?", "We factor in travel distance in our pricing. You will get a full, transparent estimate before we start."),
            ("Do you take outdoor or agricultural items in Kaaawa?", "Many types, yes. Contact us with specifics so we can confirm what we can take."),
        ],
    },
    {
        "slug": "kahala",
        "title": "Kahala",
        "map": "Kahala+Honolulu+Hawaii",
        "meta": "Junk removal in Kahala, Honolulu. Estate cleanouts, furniture removal, appliance hauling in East Honolulu. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Kahala and East Honolulu. Professional, discreet, and dependable. Free estimates.",
        "paras": [
            "Kahala is one of Honolulu's most prestigious residential neighborhoods, known for its large estate-style homes, beachfront properties, and established community. When cleanouts happen in Kahala, they often involve substantial volumes of furniture and goods.",
            "We serve Kahala for estate cleanouts, furniture removal, appliance hauling, and property preparation. We understand the expectations that come with working in an area like this: discretion, professionalism, and leaving the property exactly as clean as we found it.",
            "Free estimates apply to Kahala just as anywhere else. Call or use the contact form and we will schedule a visit at your convenience.",
        ],
        "nearby": ["Aina Haina", "Diamond Head", "Waialae", "Hawaii Kai"],
        "faqs": [
            ("Do you handle estate cleanouts in Kahala?", "Yes. Estate cleanouts in Kahala are something we are experienced with and approach carefully."),
            ("Can you be discreet during a Kahala property cleanout?", "Yes. We operate professionally and respect the privacy of our clients and their properties."),
            ("Do you take furniture from large Kahala homes?", "Yes. We haul all types of furniture and dispose of everything responsibly."),
        ],
    },
    {
        "slug": "kahuku",
        "title": "Kahuku",
        "map": "Kahuku+Hawaii",
        "meta": "Junk removal in Kahuku, North Shore Oahu. Furniture, appliances, rural property cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Kahuku and the far North Shore. Free estimates, honest pricing for rural areas.",
        "paras": [
            "Kahuku is at the northernmost point of Oahu, a rural community that is home to shrimp farms, agricultural operations, and longtime local families. Properties out here are often larger and more rural, and cleanout needs reflect that.",
            "We serve Kahuku for junk removal, though it is the farthest reach of our service area. We will be upfront about any distance-related pricing, and we will make the trip worth your while.",
            "If you are in Kahuku and have been putting off dealing with a pile of junk, reach out. We will discuss what you have and figure out a plan.",
        ],
        "nearby": ["Laie", "Hauula", "Haleiwa", "Punaluu"],
        "faqs": [
            ("Do you travel all the way to Kahuku?", "Yes, we serve Kahuku. It is a longer drive and we price accordingly. We will be transparent about the full cost before starting."),
            ("What types of items do you take in Kahuku?", "Furniture, appliances, yard debris, and general junk. Contact us for specifics."),
            ("Do you handle rural property cleanouts in Kahuku?", "Yes. Rural properties with larger accumulations of items are something we can assist with."),
        ],
    },
    {
        "slug": "kailua",
        "title": "Kailua",
        "map": "Kailua+Hawaii",
        "meta": "Junk removal in Kailua, Oahu. Furniture, appliances, estate cleanouts on the Windward side. Opala Kuleana. Free estimates.",
        "lead": "Serving Kailua and Windward Oahu with junk removal. Free estimates, upfront pricing, local team.",
        "paras": [
            "Kailua is one of Oahu's most beloved communities, known for its beautiful beach and strong sense of neighborhood pride. It is also a place where families put down roots and stay a long time, which means eventually you need help clearing out decades of accumulated belongings.",
            "We serve Kailua regularly for furniture removal, appliance hauling, estate cleanouts, and general junk pickup. Our team is familiar with the Windward side and treats every job with care.",
            "Whether you are in one of Kailua's older neighborhoods or a newer development, we cover the whole town. Free estimates, clear pricing, no surprises.",
        ],
        "nearby": ["Enchanted Lake", "Lanikai", "Kaneohe", "Maunawili"],
        "faqs": [
            ("Do you serve all of Kailua town for junk removal?", "Yes. We cover Kailua town, surrounding neighborhoods, and nearby Windward communities."),
            ("Can you do estate cleanouts in Kailua?", "Yes. Estate cleanouts are a regular part of our Windward-side work."),
            ("Do you haul yard waste and debris in Kailua?", "Yes. Garden and yard debris removal is a common request throughout Kailua."),
        ],
    },
    {
        "slug": "kalama-valley",
        "title": "Kalama Valley",
        "map": "Kalama+Valley+Hawaii+Kai+Hawaii",
        "meta": "Junk removal in Kalama Valley, Oahu. East Side furniture removal, appliances, and cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Kalama Valley and East Oahu. Free estimates, dependable service.",
        "paras": [
            "Kalama Valley is a residential neighborhood on Oahu's East Side, nestled in the hills between Hawaii Kai and Niu Valley. It is a quiet suburban community where families have often settled for the long haul.",
            "We provide junk removal in Kalama Valley for homeowners clearing out storage areas, landlords turning over properties, and families dealing with estate transitions. Our process is simple and transparent.",
            "Contact us with your address and a description of what needs to go. We will schedule a free estimate and get back to you quickly.",
        ],
        "nearby": ["Hawaii Kai", "Niu Valley", "Waimanalo", "Kuliouou"],
        "faqs": [
            ("Do you serve Kalama Valley for junk removal?", "Yes. Kalama Valley is within our East Oahu service area."),
            ("What kinds of items do you take in Kalama Valley?", "Furniture, appliances, electronics, yard waste, mattresses, and general household junk."),
            ("Is there a minimum load for Kalama Valley pickups?", "No minimum. We will come out for any amount."),
        ],
    },
    {
        "slug": "kalihi",
        "title": "Kalihi",
        "map": "Kalihi+Honolulu+Hawaii",
        "meta": "Junk removal in Kalihi, Honolulu. Furniture, appliances, apartment and home cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Kalihi. No-nonsense service, fair prices, free estimates.",
        "paras": [
            "Kalihi is a large, working-class Honolulu neighborhood with a dense mix of single-family homes, apartments, and small businesses. It is one of the city's most culturally diverse communities, and junk removal needs here are as varied as the neighborhood itself.",
            "We serve all of Kalihi for furniture removal, appliance hauling, apartment cleanouts, and general junk pickup. We do not add unnecessary fees or complications. We come out, give you a price, and get the work done.",
            "Upper Kalihi, lower Kalihi, Kalihi Kai, Kalihi Valley, all of it is within our service area. Contact us to schedule your free estimate.",
        ],
        "nearby": ["Liliha", "Nuuanu", "Kapalama", "Moanalua"],
        "faqs": [
            ("Do you serve upper and lower Kalihi for junk removal?", "Yes. We cover all of Kalihi, including Kalihi Valley and Kalihi Kai."),
            ("Can you clear out an apartment in Kalihi quickly?", "Yes. Contact us and we will schedule the earliest available appointment."),
            ("Do you haul appliances in Kalihi?", "Yes. Refrigerators, washing machines, dryers, and other appliances."),
        ],
    },
    {
        "slug": "kaneohe",
        "title": "Kaneohe",
        "map": "Kaneohe+Hawaii",
        "meta": "Junk removal in Kaneohe, Oahu. Furniture, appliances, yard waste, estate cleanouts. Opala Kuleana serves Windward Oahu. Free estimates.",
        "lead": "Serving Kaneohe and Windward Oahu with junk removal. Free estimates, local team.",
        "paras": [
            "Kaneohe is the main town on the Windward side of Oahu, known for its lush landscape, strong community, and mix of longtime local families and newer residents. It is also our most active Windward service area, with jobs ranging from single-item pickups to full estate cleanouts.",
            "We haul furniture, appliances, yard debris, construction leftovers, and all kinds of household junk in Kaneohe. Our team is familiar with the area, including the hillside neighborhoods above the highway and the flatland communities near the bay.",
            "Free estimates, clear pricing, and a crew that shows up on time. That is what we bring to every Kaneohe job.",
        ],
        "nearby": ["Ahuimanu", "Heeia", "Kailua", "Kahaluu"],
        "faqs": [
            ("Do you serve all of Kaneohe for junk removal?", "Yes. We cover all Kaneohe neighborhoods, from Haiku Road to the bay areas."),
            ("Do you take yard waste in Kaneohe?", "Yes. Yard and garden debris removal is a frequent request on the Windward side."),
            ("Can you handle a full estate cleanout in Kaneohe?", "Yes. Estate cleanouts are something we do regularly on the Windward side."),
        ],
    },
    {
        "slug": "kapolei",
        "title": "Kapolei",
        "map": "Kapolei+Hawaii",
        "meta": "Junk removal in Kapolei, Oahu. Furniture, appliances, yard waste, commercial cleanouts. Opala Kuleana serves West Oahu. Free estimates.",
        "lead": "Serving Kapolei and West Oahu with junk removal. Free estimates, no hidden fees.",
        "paras": [
            "Kapolei has grown into Oahu's second city, with a large and expanding residential population, a growing business community, and a lot of new construction. Whether you are moving in, moving out, or just clearing out space in an established home, we are here for the junk removal side of it.",
            "We serve Kapolei regularly and are familiar with the west side neighborhoods, from Makakilo to Ko Olina. Furniture, appliances, yard waste, construction debris, we take it all.",
            "Get your free estimate by filling out the contact form. We will come out, give you a firm price, and schedule the haul at a time that works.",
        ],
        "nearby": ["Makakilo", "Ewa Beach", "Ko Olina", "Ewa Gentry"],
        "faqs": [
            ("Do you serve all of Kapolei for junk removal?", "Yes. We cover Kapolei Town Center, Makakilo, Ko Olina, and surrounding west side neighborhoods."),
            ("Can you do yard waste removal in Kapolei?", "Yes. Yard debris, palm fronds, and green waste are regular requests in this area."),
            ("Do you handle commercial junk removal in Kapolei?", "Yes. We work with businesses and commercial properties throughout West Oahu."),
        ],
    },
    {
        "slug": "laie",
        "title": "Laie",
        "map": "Laie+Hawaii",
        "meta": "Junk removal in Laie, North Shore Oahu. Furniture, appliances, household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Laie and North Shore Oahu communities. Free estimates, honest pricing.",
        "paras": [
            "Laie is a close-knit community on the North Shore, home to BYU Hawaii and a strong Polynesian community. It is a place with deep roots, and properties here often have accumulated belongings over many years.",
            "We serve Laie for junk removal, including furniture, appliances, household cleanouts, and yard debris. The drive from town is longer, and we factor that into our pricing transparently.",
            "If you are in Laie and need something hauled away, reach out. We will discuss what you have and find a solution that works.",
        ],
        "nearby": ["Hauula", "Kahuku", "Punaluu", "Malaekahana"],
        "faqs": [
            ("Do you travel to Laie for junk removal?", "Yes. Laie is within our service area. Distance is factored into pricing transparently."),
            ("Can you do a full household cleanout in Laie?", "Yes. Full household and estate cleanouts are within our scope."),
            ("What items do you take in Laie?", "Furniture, appliances, mattresses, electronics, yard waste, and general household junk."),
        ],
    },
    {
        "slug": "maili",
        "title": "Maili",
        "map": "Maili+Waianae+Hawaii",
        "meta": "Junk removal in Maili, Waianae Coast, Oahu. Furniture, appliances, and household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Maili and the Waianae Coast. Free estimates, straightforward pricing.",
        "paras": [
            "Maili is a Waianae Coast community between Nanakuli and Waianae town. It is a predominantly local neighborhood with a strong community identity and a mix of longtime homeowners and younger families.",
            "We serve Maili for junk removal, hauling furniture, appliances, yard waste, and general household items. We treat every community on Oahu with the same respect, and Maili is no exception.",
            "Contact us with your address and what you need removed. We will set up a free estimate and give you a straight price.",
        ],
        "nearby": ["Nanakuli", "Waianae", "Makaha", "Ko Olina"],
        "faqs": [
            ("Do you serve Maili on the Waianae Coast?", "Yes. We serve Maili and surrounding Waianae Coast communities."),
            ("What types of items do you take in Maili?", "Furniture, appliances, mattresses, electronics, yard waste, and general junk."),
            ("Is there a minimum load for Maili pickups?", "No minimum. Pricing is based on volume."),
        ],
    },
    {
        "slug": "makaha",
        "title": "Makaha",
        "map": "Makaha+Hawaii",
        "meta": "Junk removal in Makaha, Oahu. Waianae Coast furniture removal, appliances, and household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Makaha and far West Oahu. Free estimates, honest pricing.",
        "paras": [
            "Makaha is at the far end of the Waianae Coast, known for its famous surf break and a community with deep local roots. Properties here tend to be more spread out than in town, and junk removal needs reflect the rural character of the area.",
            "We serve Makaha for junk removal. It is a longer haul from our base, and we factor that into pricing fairly and upfront. Whether it is furniture, appliances, yard debris, or a larger cleanout, we will discuss what you have and give you an honest quote.",
            "If you are in Makaha and have been putting off dealing with a pile of junk, reach out. We will make the trip and get it handled.",
        ],
        "nearby": ["Waianae", "Maili", "Nanakuli", "Kaena Point area"],
        "faqs": [
            ("Do you serve Makaha for junk removal?", "Yes. We cover Makaha and the far West Coast of Oahu."),
            ("Is there a travel fee for Makaha?", "We factor in distance in our pricing. We will be transparent about the full cost before starting."),
            ("What items do you haul in Makaha?", "Furniture, appliances, yard debris, and general household junk."),
        ],
    },
    {
        "slug": "makakilo",
        "title": "Makakilo",
        "map": "Makakilo+Hawaii",
        "meta": "Junk removal in Makakilo, Oahu. Furniture, appliances, yard waste removal on West Oahu hillsides. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Makakilo and the Kapolei area. Free estimates, local crew, honest pricing.",
        "paras": [
            "Makakilo sits on the hillsides above Kapolei, offering sweeping views of West Oahu. It is a residential community that has been growing steadily, with a mix of newer developments and older established homes. When you are ready to clear out the garage or deal with leftover renovation debris, we are nearby.",
            "We serve Makakilo for furniture removal, appliance hauling, yard waste pickup, and full property cleanouts. The hillside location is not a problem for us. We plan the logistics before we commit to a price.",
            "Get a free estimate by reaching out through the contact form. We are in the West Side often and can usually schedule estimates quickly.",
        ],
        "nearby": ["Kapolei", "Ewa Gentry", "Kalaeloa", "Ko Olina"],
        "faqs": [
            ("Do you serve Makakilo hillside properties?", "Yes. We are comfortable with hillside access and plan it as part of the estimate."),
            ("Can you take yard waste from Makakilo homes?", "Yes. Yard and garden debris removal is a common request in this area."),
            ("Do you haul appliances from Makakilo?", "Yes. All major appliances, including refrigerators, washers, and dryers."),
        ],
    },
    {
        "slug": "manoa",
        "title": "Manoa",
        "map": "Manoa+Honolulu+Hawaii",
        "meta": "Junk removal in Manoa, Honolulu. Furniture, appliances, student move-outs, and estate cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Serving Manoa with junk removal for homes, rentals, and student housing. Free estimates always.",
        "paras": [
            "Manoa is a lush valley neighborhood home to the University of Hawaii at Manoa, a large student and faculty population, and well-established residential streets. The combination of long-term homeowners and high rental turnover means there is always a steady demand for junk removal in this area.",
            "We serve Manoa for student move-out cleanouts, furniture removal from rental units, estate cleanouts for longtime residents, and all standard household junk pickup. We are familiar with the neighborhood and its mix of older homes and apartment buildings.",
            "Contact us to schedule your free estimate. We will come out, assess what needs to go, and give you a firm price before anything gets loaded on the truck.",
        ],
        "nearby": ["McCully", "Palolo", "Kapahulu", "St. Louis Heights"],
        "faqs": [
            ("Do you help with student move-outs in Manoa?", "Yes. End-of-semester cleanouts in and around the University of Hawaii area are something we handle regularly."),
            ("Can you clear out a rental unit in Manoa between tenants?", "Yes. Landlords and property managers in Manoa use us regularly for this."),
            ("Do you take furniture from older Manoa homes?", "Yes. All types of furniture, including large, bulky pieces from older homes."),
        ],
    },
    {
        "slug": "mililani",
        "title": "Mililani",
        "map": "Mililani+Hawaii",
        "meta": "Junk removal in Mililani, Oahu. Furniture, appliances, estate cleanouts, yard waste. Opala Kuleana. Free estimates.",
        "lead": "Serving Mililani with junk removal. Free estimates, dependable service for Central Oahu.",
        "paras": [
            "Mililani is Oahu's largest planned community, a well-maintained Central Oahu neighborhood with strong community organization and a lot of family-oriented households. It is a neighborhood where people settle in and stay, which means over time there is always something that needs to go.",
            "We serve all of Mililani for junk removal, from Mililani Mauka to Mililani Town. We haul furniture, appliances, yard debris, construction materials, and general household junk. Our service is appointment-based and we give you a firm price before starting.",
            "Fill out the contact form with your Mililani address and what needs to go. We will get back to you quickly to schedule a free estimate.",
        ],
        "nearby": ["Waipio", "Wahiawa", "Mililani Mauka", "Waikele"],
        "faqs": [
            ("Do you serve both Mililani Town and Mililani Mauka?", "Yes. We cover both sections of Mililani."),
            ("Can you haul yard waste in Mililani?", "Yes. Yard and garden debris, including palm fronds and branches."),
            ("Do you take estate cleanouts in Mililani?", "Yes. Estate cleanouts are a service we offer throughout Central Oahu."),
        ],
    },
    {
        "slug": "nanakuli",
        "title": "Nanakuli",
        "map": "Nanakuli+Hawaii",
        "meta": "Junk removal in Nanakuli, Waianae Coast, Oahu. Furniture, appliances, household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Nanakuli and the Waianae Coast. Free estimates, fair pricing, local values.",
        "paras": [
            "Nanakuli is a close-knit community on the Waianae Coast with strong local ties and a mix of families who have been there for generations. Like many West Side communities, it has its own character and deserves service from a company that respects that.",
            "We serve Nanakuli for junk removal including furniture, appliances, yard debris, and household cleanouts. We are straightforward about pricing and we do the work right.",
            "Reach out with what you need and when you are available. We will schedule a free estimate and take it from there.",
        ],
        "nearby": ["Waianae", "Maili", "Kapolei", "Ko Olina"],
        "faqs": [
            ("Do you serve Nanakuli for junk removal?", "Yes. We serve Nanakuli and surrounding Waianae Coast communities."),
            ("What items can you haul in Nanakuli?", "Furniture, appliances, mattresses, electronics, yard waste, and general junk."),
            ("How do I schedule a Nanakuli pickup?", "Use the contact form. We will schedule a free estimate at a time that works."),
        ],
    },
    {
        "slug": "pearl-city",
        "title": "Pearl City",
        "map": "Pearl+City+Hawaii",
        "meta": "Junk removal in Pearl City, Oahu. Furniture, appliances, yard waste, and full cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Serving Pearl City with dependable junk removal. Free estimates, fair pricing, local team.",
        "paras": [
            "Pearl City is one of Oahu's most populated suburban communities, located along the Pearl Harbor waterway. It is a family-oriented neighborhood with a wide range of housing, from older plantation-era homes to newer subdivisions, and a steady demand for junk removal services.",
            "We serve Pearl City regularly, hauling furniture, appliances, yard waste, construction debris, mattresses, and general household junk. Whether it is a single item or a full property cleanout, we quote upfront and work on your schedule.",
            "Contact us for a free estimate in Pearl City. We are in the area often and can usually schedule quickly.",
        ],
        "nearby": ["Aiea", "Waimalu", "Pearlridge", "Waipio"],
        "faqs": [
            ("Do you cover all of Pearl City for junk removal?", "Yes. We cover all Pearl City neighborhoods, including Waimalu and Pearlridge."),
            ("Can you haul furniture from Pearl City homes quickly?", "Yes. Contact us and we will find the earliest available appointment."),
            ("Do you take construction debris in Pearl City?", "Yes. Renovation and construction debris hauling is part of our service."),
        ],
    },
    {
        "slug": "pearl-harbor",
        "title": "Pearl Harbor",
        "map": "Pearl+Harbor+Hawaii",
        "meta": "Junk removal near Pearl Harbor, Oahu. Military and civilian cleanouts, furniture removal, appliance hauling. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for the Pearl Harbor area. Military and civilian households. Free estimates.",
        "paras": [
            "The Pearl Harbor area is home to one of the most significant military installations in the Pacific, and the surrounding communities include both military housing and civilian neighborhoods. Move cycles here are frequent, and junk removal is a recurring need.",
            "We serve civilian neighborhoods in and around the Pearl Harbor area for furniture removal, appliance hauling, and full household cleanouts. For military housing, contact us with your specific address and we will confirm access and scheduling.",
            "Whether you are a military family heading to the next duty station or a local civilian clearing out a property, we are here to help.",
        ],
        "nearby": ["Aiea", "Pearl City", "Hickam Housing", "Ewa Beach"],
        "faqs": [
            ("Do you serve civilian homes near Pearl Harbor?", "Yes. We serve civilian residential areas throughout the Pearl Harbor corridor."),
            ("Can you assist military families with cleanouts near Pearl Harbor?", "Yes. Contact us with your address and we will confirm what we can access."),
            ("What items do you haul in the Pearl Harbor area?", "Furniture, appliances, mattresses, electronics, yard waste, and general junk."),
        ],
    },
    {
        "slug": "waialua",
        "title": "Waialua",
        "map": "Waialua+Hawaii",
        "meta": "Junk removal in Waialua, North Shore Oahu. Furniture, appliances, agricultural debris. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Waialua and the North Shore. Free estimates, honest pricing for rural areas.",
        "paras": [
            "Waialua is a small plantation-era town on the North Shore, known for its sugar mill history and agricultural character. Properties in Waialua tend to be larger and more rural, with more outdoor storage and equipment than you would find in town.",
            "We serve Waialua for junk removal, hauling furniture, appliances, yard and farm debris, and general household items. The drive is longer than from central Honolulu, and we are upfront about how that factors into pricing.",
            "If you are in Waialua and ready to deal with the pile that has been sitting there, reach out. We will schedule a free estimate and make the trip count.",
        ],
        "nearby": ["Haleiwa", "Mokuleia", "Waimea", "Kahuku"],
        "faqs": [
            ("Do you serve Waialua for junk removal?", "Yes. We travel to Waialua and the surrounding North Shore area."),
            ("Is there a trip fee for Waialua?", "Distance is factored into our pricing and disclosed upfront."),
            ("Can you take farm or agricultural equipment in Waialua?", "Some items, yes. Contact us with specifics and we will let you know what we can take."),
        ],
    },
    {
        "slug": "waianae",
        "title": "Waianae",
        "map": "Waianae+Hawaii",
        "meta": "Junk removal in Waianae, Oahu. Furniture, appliances, yard waste, and household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Waianae and the Waianae Coast. Free estimates, fair and transparent pricing.",
        "paras": [
            "Waianae is the main town on the Waianae Coast, a community with a strong local character and a population that values honest, respectful service. We are a small local business, not a faceless corporation, and we treat every community on Oahu the same way.",
            "We serve Waianae for furniture removal, appliance hauling, yard debris, and full household cleanouts. We give you a straight price and we do the work right.",
            "Reach out with what you need removed and we will schedule a free estimate. We will be honest about what we can take and what it will cost.",
        ],
        "nearby": ["Maili", "Nanakuli", "Makaha", "Kapolei"],
        "faqs": [
            ("Do you serve Waianae town for junk removal?", "Yes. We serve Waianae and the surrounding Waianae Coast."),
            ("What types of items do you haul in Waianae?", "Furniture, appliances, mattresses, yard waste, electronics, and general household junk."),
            ("How do I get a quote for junk removal in Waianae?", "Fill out our contact form. We will schedule a free on-site estimate."),
        ],
    },
    {
        "slug": "waikiki",
        "title": "Waikiki",
        "map": "Waikiki+Honolulu+Hawaii",
        "meta": "Junk removal in Waikiki, Honolulu. Condo cleanouts, furniture removal, commercial pickups. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Waikiki. Condo cleanouts, furniture removal, commercial pickups. Free estimates.",
        "paras": [
            "Waikiki is Honolulu's most recognized neighborhood, a dense mix of hotels, high-rise condos, retail, and a resident population that often gets overlooked beneath the tourist surface. For condo residents and property managers in Waikiki, junk removal presents specific logistical challenges.",
            "We handle condo cleanouts in Waikiki regularly. We coordinate with building management for elevator access, work cleanly in common areas, and haul everything to the truck without creating issues for neighboring units or staff.",
            "Whether you are a long-term resident clearing out a unit or a property manager turning over a rental, we are the efficient and professional choice for Waikiki junk removal.",
        ],
        "nearby": ["Ala Moana", "Kapahulu", "McCully", "Diamond Head"],
        "faqs": [
            ("Do you do condo cleanouts in Waikiki?", "Yes. High-rise and mid-rise condo cleanouts in Waikiki are something we handle often."),
            ("Can you work around building rules for elevator access in Waikiki?", "Yes. We coordinate with building management and work within their guidelines."),
            ("Do you take furniture from Waikiki condos?", "Yes. All types and sizes of furniture."),
        ],
    },
    {
        "slug": "waimanalo",
        "title": "Waimanalo",
        "map": "Waimanalo+Hawaii",
        "meta": "Junk removal in Waimanalo, Oahu. Windward rural properties, furniture removal, appliances. Opala Kuleana. Free estimates.",
        "lead": "Junk removal for Waimanalo and East Oahu. Free estimates, dependable service for rural properties.",
        "paras": [
            "Waimanalo is a rural-residential community on the Windward side, known for its open land, horse farms, and some of Oahu's most beautiful beach scenery. Properties here tend to be larger with more outdoor storage, and cleanout needs often reflect that character.",
            "We serve Waimanalo for junk removal, including furniture, appliances, yard debris, outdoor equipment, and general cleanouts. Rural access is not an obstacle for us. We assess the logistics during the free estimate and come prepared.",
            "If you are in Waimanalo and need a reliable removal crew, reach out. We will schedule a visit and give you a fair price.",
        ],
        "nearby": ["Kailua", "Lanikai", "Kalama Valley", "Makapuu"],
        "faqs": [
            ("Do you serve Waimanalo for junk removal?", "Yes. We serve Waimanalo and surrounding East Oahu communities."),
            ("Can you handle rural property cleanouts in Waimanalo?", "Yes. We are experienced with larger rural properties and plan the job accordingly."),
            ("Do you take outdoor or agricultural items in Waimanalo?", "Many types, yes. Contact us with specifics so we can confirm what we can take."),
        ],
    },
    {
        "slug": "waipahu",
        "title": "Waipahu",
        "map": "Waipahu+Hawaii",
        "meta": "Junk removal in Waipahu, Oahu. Furniture, appliances, yard waste, and full household cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Serving Waipahu with junk removal. Free estimates, no hidden fees, local crew.",
        "paras": [
            "Waipahu is a large Central Oahu community with deep plantation heritage and a diverse, working-class character. It is home to a wide range of housing types, from older single-family homes to newer subdivisions, and junk removal needs are steady throughout the year.",
            "We serve Waipahu for furniture removal, appliance hauling, yard waste pickup, construction debris, and full property cleanouts. We are in this part of Oahu regularly and treat every job the same: show up, give a fair price, haul it away.",
            "Contact us to schedule your free estimate. We will come out, see what needs to go, and get it done.",
        ],
        "nearby": ["Pearl City", "Waikele", "Ewa Beach", "Waipio"],
        "faqs": [
            ("Do you serve all of Waipahu for junk removal?", "Yes. We cover Waipahu town and surrounding neighborhoods."),
            ("Can you haul construction debris from a Waipahu renovation?", "Yes. Construction and renovation debris hauling is one of our core services."),
            ("Do you take yard waste in Waipahu?", "Yes. Yard and garden debris, green waste, and landscaping leftovers."),
        ],
    },
    {
        "slug": "whitmore-village",
        "title": "Whitmore Village",
        "map": "Whitmore+Village+Wahiawa+Hawaii",
        "meta": "Junk removal in Whitmore Village, Oahu. Central Oahu furniture removal, appliances, cleanouts. Opala Kuleana. Free estimates.",
        "lead": "Junk removal in Whitmore Village and Central Oahu. Free estimates, honest pricing.",
        "paras": [
            "Whitmore Village is a small, historic community in central Oahu near Wahiawa, with roots in the plantation era. It is a tight-knit neighborhood where properties have character and history, and cleanouts here sometimes involve clearing out a lot of accumulated years.",
            "We serve Whitmore Village for junk removal, hauling furniture, appliances, yard debris, and general household items. We are in the Central Oahu area regularly and can usually schedule estimates without a long wait.",
            "Reach out with what you need and your general availability. We will schedule a free estimate and take care of the rest.",
        ],
        "nearby": ["Wahiawa", "Schofield Barracks", "Mililani", "Wheeler Army Airfield"],
        "faqs": [
            ("Do you serve Whitmore Village for junk removal?", "Yes. Whitmore Village is within our Central Oahu service area."),
            ("What types of items do you take in Whitmore Village?", "Furniture, appliances, mattresses, yard waste, electronics, and general household junk."),
            ("Is there a minimum load for Whitmore Village pickups?", "No minimum. Pricing is based on volume."),
        ],
    },
]


def services_html():
    items = "".join(f'<li>{s}</li>' for s in SERVICES)
    return f'<ul class="ok-sa-services-list">{items}</ul>'


def trust_html():
    items = "".join(f'<div class="ok-sa-trust-item">{t}</div>' for t in TRUST)
    return f'<div class="ok-sa-trust">{items}</div>'


def nearby_html(nearby):
    items = "".join(f'<span class="ok-sa-tag">{n}</span>' for n in nearby)
    return f'<div class="ok-sa-nearby">{items}</div>'


def faq_html(faqs):
    items = ""
    for q, a in faqs:
        items += f"""<div class="ok-sa-faq-item">
<h3>{q}</h3>
<p>{a}</p>
</div>"""
    return items


def schema_json(area):
    lb = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Opala Kuleana",
        "description": f"Junk removal services in {area['title']}, Oahu, Hawaii.",
        "url": f"{SITE_URL}/service-areas/{area['slug']}/",
        "areaServed": {"@type": "City", "name": f"{area['title']}, Hawaii"},
        "priceRange": "$$",
        "image": f"{SITE_URL}/assets/images/ok-logo.jpg",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00",
            "closes": "17:00"
        }
    }
    bc = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": "Service Areas", "item": SITE_URL + "/service-areas/"},
            {"@type": "ListItem", "position": 3, "name": area["title"]},
        ]
    }
    return (
        f'<script type="application/ld+json">{json.dumps(lb)}</script>\n'
        f'<script type="application/ld+json">{json.dumps(bc)}</script>'
    )


PAGE_CSS = """<style>
.ok-sa-breadcrumb{background:var(--c-bg);border-bottom:1px solid var(--c-border);padding:12px 0;font-size:.85rem;color:var(--c-text-muted)}
.ok-sa-breadcrumb .container{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.ok-sa-breadcrumb a{color:var(--c-primary);text-decoration:none}
.ok-sa-breadcrumb a:hover{text-decoration:underline}
.ok-sa-breadcrumb span.sep{color:var(--c-border)}
.ok-sa-layout{display:grid;grid-template-columns:1fr 340px;gap:48px;align-items:start}
.ok-sa-main p{color:var(--c-text-muted);line-height:1.75;margin-bottom:1.1rem}
.ok-sa-main h2{font-family:var(--ff-display);font-weight:800;font-size:clamp(1.25rem,2vw,1.6rem);color:var(--c-primary);margin:2rem 0 .75rem}
.ok-sa-services-list{margin:0 0 1rem 1.25rem;color:var(--c-text-muted);line-height:2}
.ok-sa-trust{display:flex;flex-wrap:wrap;gap:10px;margin:1.5rem 0}
.ok-sa-trust-item{background:var(--c-bg);border:1px solid var(--c-border);border-left:4px solid var(--c-accent);padding:8px 14px;border-radius:var(--r-sm);font-size:.85rem;font-weight:600;color:var(--c-primary)}
.ok-sa-faq-item{border-bottom:1px solid var(--c-border);padding-bottom:1.25rem;margin-bottom:1.25rem}
.ok-sa-faq-item:last-child{border-bottom:none}
.ok-sa-faq-item h3{font-size:1rem;font-weight:700;color:var(--c-text);margin-bottom:.4rem}
.ok-sa-faq-item p{font-size:.9rem;color:var(--c-text-muted);margin:0;line-height:1.65}
.ok-sa-nearby{display:flex;flex-wrap:wrap;gap:8px;margin:1rem 0}
.ok-sa-tag{background:var(--c-bg-alt);border:1px solid var(--c-border);padding:5px 12px;border-radius:var(--r-full);font-size:.82rem;color:var(--c-text-muted)}
.ok-sa-map{width:100%;height:340px;border:0;border-radius:var(--r-md);margin:1.5rem 0;display:block;border:1px solid var(--c-border)}
.ok-sa-sidebar{position:sticky;top:88px;display:flex;flex-direction:column;gap:20px}
.ok-sa-card{background:var(--c-bg);border:1px solid var(--c-border);border-radius:var(--r-md);padding:24px}
.ok-sa-card h3{font-family:var(--ff-display);font-weight:800;font-size:1.1rem;color:var(--c-primary);margin-bottom:8px}
.ok-sa-card p{font-size:.9rem;color:var(--c-text-muted);line-height:1.6;margin-bottom:16px}
.ok-sa-card .btn{display:block;text-align:center;width:100%}
.ok-sa-links{list-style:none;padding:0;margin:0}
.ok-sa-links li{border-bottom:1px solid var(--c-border);padding:8px 0}
.ok-sa-links li:last-child{border-bottom:none}
.ok-sa-links a{font-size:.9rem;color:var(--c-primary);font-weight:500}
.ok-sa-links a:hover{color:var(--c-accent)}
@media(max-width:860px){.ok-sa-layout{grid-template-columns:1fr}.ok-sa-sidebar{position:static}}
</style>"""


def build_page(area):
    slug = area["slug"]
    title = area["title"]
    paras = "".join(f"<p>{p}</p>" for p in area["paras"])
    faq = faq_html(area["faqs"])
    nearby = nearby_html(area["nearby"])

    content = f"""---
layout: default
title: "{title} Junk Removal Services"
description: "{area['meta']}"
permalink: /service-areas/{slug}/
---
{PAGE_CSS}
{schema_json(area)}

<nav class="ok-sa-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <a href="/">Home</a>
    <span class="sep">&rsaquo;</span>
    <a href="/service-areas/">Service Areas</a>
    <span class="sep">&rsaquo;</span>
    <span aria-current="page">{title}</span>
  </div>
</nav>

<section class="page-hero">
  <div class="container">
    <span class="post-category">Oahu Junk Removal</span>
    <h1>{title} Junk Removal Services</h1>
    <p class="page-lead">{area['lead']}</p>
  </div>
</section>

<section class="section-pad bg-white">
  <div class="container">
    <div class="ok-sa-layout">

      <div class="ok-sa-main">

        {paras}

        <h2>Services Available in {title}</h2>
        {services_html()}

        <h2>Why Choose Us</h2>
        {trust_html()}

        <h2>Nearby Areas We Also Serve</h2>
        {nearby}

        <h2>Common Questions About Junk Removal in {title}</h2>
        {faq}

        <iframe
          class="ok-sa-map"
          src="https://maps.google.com/maps?q={area['map']}&output=embed&hl=en"
          allowfullscreen
          loading="lazy"
          title="Map of {title}, Hawaii"
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>

      </div>

      <aside class="ok-sa-sidebar">

        <div class="ok-sa-card">
          <h3>Get a Free Estimate</h3>
          <p>We serve {title} and all of Oahu. Contact us and we will come out, take a look, and give you a firm price before we start.</p>
          <a href="/contact/" class="btn btn-primary">Request Free Estimate</a>
        </div>

        <div class="ok-sa-card">
          <h3>Our Services</h3>
          <ul class="ok-sa-links">
            <li><a href="/services/">Furniture Removal</a></li>
            <li><a href="/services/">Appliance Removal</a></li>
            <li><a href="/services/">Estate Cleanouts</a></li>
            <li><a href="/services/">Construction Debris</a></li>
            <li><a href="/services/">E-Waste and Electronics</a></li>
            <li><a href="/services/">Yard Waste</a></li>
            <li><a href="/services/">View All Services</a></li>
          </ul>
        </div>

        <div class="ok-sa-card">
          <h3>Service Hours</h3>
          <p>Monday through Friday, 8 AM to 5 PM, by appointment only. Free on-site estimates available.</p>
        </div>

      </aside>

    </div>
  </div>
</section>

<section class="section-pad" style="background:var(--c-primary);">
  <div class="container" style="text-align:center;">
    <h2 style="font-family:var(--ff-display);font-weight:800;font-size:clamp(1.6rem,3vw,2.2rem);color:#fff;margin-bottom:12px;">Ready to Clear Out in {title}?</h2>
    <p style="color:rgba(255,255,255,0.85);max-width:560px;margin:0 auto 28px;line-height:1.7;">Contact us for a free on-site estimate. We serve {title} and all of Oahu. No hidden fees, no vague quotes, just a fair price and a crew that shows up.</p>
    <a href="/contact/" class="btn btn-primary" style="background:#fff;color:var(--c-primary);border-color:#fff;font-weight:700;">Get Your Free Estimate</a>
  </div>
</section>
"""
    return content


# Generate individual area pages
for area in AREAS:
    filepath = os.path.join(OUTPUT_DIR, f"{area['slug']}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(build_page(area))
    print(f"  Created: {filepath}")

# Generate service areas index page
index_cards = ""
for area in AREAS:
    index_cards += f"""<a href="/service-areas/{area['slug']}/" class="ok-sa-index-card">
  <h3>{area['title']}</h3>
  <p>Junk removal in {area['title']}, Oahu</p>
  <span class="ok-sa-index-link">Learn more &rarr;</span>
</a>
"""

index_page = f"""---
layout: default
title: "Service Areas — Oahu Junk Removal"
description: "Opala Kuleana provides junk removal throughout Oahu, Hawaii. View all service areas including Honolulu, Kaneohe, Kailua, Kapolei, Ewa Beach, and more."
permalink: /service-areas/
---
<style>
.ok-sa-index-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px;margin-top:32px}}
.ok-sa-index-card{{display:block;background:var(--c-bg);border:1px solid var(--c-border);border-top:4px solid var(--c-accent);border-radius:var(--r-md);padding:20px;text-decoration:none;transition:box-shadow .2s,transform .2s}}
.ok-sa-index-card:hover{{box-shadow:var(--shadow-md);transform:translateY(-2px)}}
.ok-sa-index-card h3{{font-family:var(--ff-display);font-weight:700;font-size:1rem;color:var(--c-primary);margin-bottom:4px}}
.ok-sa-index-card p{{font-size:.85rem;color:var(--c-text-muted);margin:0 0 12px}}
.ok-sa-index-link{{font-size:.82rem;font-weight:600;color:var(--c-accent)}}
</style>

<section class="page-hero">
  <div class="container">
    <span class="post-category">Where We Work</span>
    <h1>Service Areas Across Oahu</h1>
    <p class="page-lead">We provide junk removal throughout the island of Oahu, from the North Shore to the Waianae Coast, Windward side to downtown Honolulu.</p>
  </div>
</section>

<section class="section-pad bg-white">
  <div class="container">
    <div class="ok-sa-index-grid">
      {index_cards}
    </div>
  </div>
</section>
"""

index_path = os.path.join(OUTPUT_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_page)
print(f"  Created: {index_path}")

print(f"\nDone. {len(AREAS)} area pages + 1 index page generated in {OUTPUT_DIR}/")
