---
layout: default
title: Home
---

# Welcome to Ōpala Kuleana

## Professional Junk Removal Services

We help you clear out unwanted items and create the space you deserve. With years of experience serving the community, Ōpala Kuleana is your trusted partner for hassle-free junk removal.

### Our Services

- **Residential Junk Removal** - Clear your home of unwanted items
- **Commercial Cleanup** - Professional disposal for businesses
- **Yard Waste Removal** - Haul away branches, leaves, and landscaping debris
- **Demolition Services** - Safe and efficient removal of structures

### Recent Blog Posts

<ul class="post-list">
{% for post in site.posts limit:5 %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span class="post-meta">{{ post.date | date: '%B %d, %Y' }}</span>
  </li>
{% endfor %}
</ul>

### Ready to Get Started?

Contact us today for a free estimate. We're committed to providing professional, efficient, and affordable junk removal services.

[View Our Services](/opalakuleana/services/) | [Learn More About Us](/opalakuleana/about/)
