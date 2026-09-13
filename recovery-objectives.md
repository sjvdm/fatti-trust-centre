---
title: Recovery objectives
description: How Fatti evaluates achievable recovery time and recovery point objectives for Mall Wi-Fi services.
permalink: /recovery-objectives/
---

<p class="eyebrow">RTO / RPO assessment framework</p>
# Recovery objectives

Fatti establishes recovery objectives against the selected service, deployment architecture and failure scenario. The recovery time objective (RTO) describes the target time to restore an agreed service. The recovery point objective (RPO) describes the acceptable age of recovered data and therefore the potential data-loss interval.

<div class="notice"><strong>No universal SLA is stated on this page.</strong> An achievable target requires a client-specific design, confirmed dependencies and recovery evidence. A software restoration estimate does not describe physical equipment replacement or an entire venue outage.</div>

## Architecture and achievable RTO

| Assessment area | Public service position |
| --- | --- |
| Supported architecture | Standard deployments combine site-specific services with centrally managed processing and reporting. High availability, redundant paths and geographically separate recovery are design options that must be confirmed per component. |
| Active-active or active-passive | These are component-level design choices rather than a universal operating mode for the full Mall Wi-Fi service. |
| Dedicated DR environment | Selected software and data services can be recovered into alternate infrastructure. A fully independent DR environment for every site, central and cloud component must be specifically designed and tested. |
| Failover | Manual intervention is typical. Automated failover applies only where the relevant high-availability design has been selected, configured and tested. |
| Recovery process | Triage the failure, confirm power/connectivity/access, select a valid recovery point, restore prerequisites and services, validate integrity and reporting, then return to normal operation under change control. |
| Longest lead times | Customer-owned network equipment, spares, procurement, shipping and physical site access can take longer than remotely recoverable software incidents. |
| Operation during failures | Some functions may continue during isolated failures. Collection, portal access, analytics processing and reporting must be evaluated separately because one can remain available while another is interrupted. |

## Designing for a target

| Target band | Design considerations |
| --- | --- |
| Within 24 hours | Confirm recoverable backups, responsible people, secure remote access, replacement dependencies and a tested runbook. |
| Within 8 hours | Add pre-positioned recovery capacity, monitored backup freshness, clear escalation and available technical cover. |
| Within 4 hours | Reduce manual provisioning, provide resilient connectivity and spares, and test the complete dependency chain. |
| Within 1 hour | Requires suitable high availability, automated failover where feasible, resilient network and power paths, ready recovery infrastructure and repeated end-to-end exercises. It is not a standard commitment. |

The tighter the objective, the more the design must reduce dependencies on procurement, travel, manual configuration and a single connectivity or processing path.

## Data protection and achievable RPO

Fatti's recovery model can include scheduled configuration exports, application and database backups, off-site copies and asynchronous replication for applicable services. The exact mechanism, frequency, retention, encryption, monitoring and restoration evidence are confirmed in the client assessment.

Replication and backup solve different problems. Replication can reduce recovery lag but may copy corruption or deletion; independent recoverable copies and restoration testing remain necessary.

Fatti does not publish a universal minimum RPO. The chosen value must be supported by the actual capture path, replication or backup schedule, failed-job handling and the latest valid recovery point. Information never collected during a venue connectivity or equipment outage may be unrecoverable regardless of database backup frequency.

## Information needed for a scoped answer

To produce an RTO/RPO response, Fatti needs:

1. the venue and services in scope;
2. the required failure scenarios;
3. infrastructure ownership and site-access arrangements;
4. selected redundancy, connectivity and spare-equipment design;
5. the contractual service and support window; and
6. whether each requested value is an objective, tested result or binding commitment.

Send the questionnaire and scope to [sj@fatti.co.za](mailto:sj@fatti.co.za) and [jaco@fatti.co.za](mailto:jaco@fatti.co.za).
