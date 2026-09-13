---
title: Resilience
description: How Fatti frames backup, recovery and venue service dependencies.
permalink: /resilience/
---

<p class="eyebrow">Continuity and recovery</p>
# Resilience

Recovery planning for venue Wi-Fi requires separate treatment of managed software, central services, information stores and physical site equipment. A single recovery time cannot accurately describe every failure scenario.

<div class="principles">
  <div><h3>Managed software and configuration</h3><p>Backup and restoration scope is recorded for the software, databases and configurations included in the service.</p></div>
  <div><h3>Central services</h3><p>Dependencies such as connectivity, processing and cloud services are considered when setting service recovery objectives.</p></div>
  <div><h3>Venue infrastructure</h3><p>Power, internet circuits, cabling, physical access, spares and customer-owned equipment affect whole-site recovery.</p></div>
  <div><h3>Verification</h3><p>Useful assurance connects recovery statements to current job results, restoration tests and the service's actual architecture.</p></div>
</div>

## Client-specific objectives

Recovery time objectives, recovery point objectives, high availability and replacement commitments must be confirmed for the selected service and site design. Software restoration estimates do not automatically include failed hardware, unavailable power or a lost internet circuit.

Fatti can provide a scoped response for a client questionnaire. The response should identify assumptions, customer dependencies and whether a value is a target, a tested result or a contractual commitment.

See [Recovery objectives]({{ '/recovery-objectives/' | relative_url }}) for the questions Fatti uses to establish an achievable RTO and RPO.
