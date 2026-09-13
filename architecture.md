---
title: Architecture
description: A high-level view of Fatti's venue Wi-Fi and analytics service architecture.
permalink: /architecture/
---

<p class="eyebrow">Service model</p>
# Architecture

Fatti combines venue Wi-Fi infrastructure with location processing, captive portal services and analytics reporting. The exact component placement and resilience design vary by venue.

<div class="architecture" role="img" aria-label="Visitor devices connect to venue Wi-Fi and a captive portal. Wireless observations pass through a location engine and managed processing into analytics storage and client reporting.">
  <div class="stage"><strong>1. Venue interaction</strong><span>Visitor devices connect to venue Wi-Fi. A configured captive portal may collect registration information for Wi-Fi access and other stated purposes.</span></div>
  <div class="stage"><strong>2. Wireless observations</strong><span>Venue infrastructure supplies observations used by a location engine to estimate device positions over time.</span></div>
  <div class="stage"><strong>3. Managed processing</strong><span>Fatti-managed services process location events and configured portal data within the deployment's service boundaries.</span></div>
  <div class="stage"><strong>4. Analytics and reporting</strong><span>Selected information is prepared for authorised client dashboards and reports.</span></div>
</div>

## Deployment boundaries

On-site equipment commonly depends on venue power, connectivity, cabling and physical access. Equipment ownership, spares, high availability and support scope are set by the client design and agreement. Some software functions may run at the venue and others centrally.

Fatti maintains a more detailed architecture and data-flow record for internal assurance. Sensitive topology, access methods and security findings are not published here.

## Responsibility follows the service

The applicable agreement records responsibilities for site infrastructure, Fatti-managed software, support, information processing and client users. A client-specific review should confirm these boundaries before relying on a recovery target or control statement.

