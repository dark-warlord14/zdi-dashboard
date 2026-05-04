# ZDI-21-373: SolarWinds Orion Virtual Infrastructure Monitor OneTimeJobSchedulerEventsService Deserialization of Untrusted Data Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-373
- **ZDI-CAN:** ZDI-CAN-11955
- **Date:** 2021-03-30
- **CVE:** CVE-2021-27277
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Virtual Infrastructure Monitor
- **Credit:** Harrison Neal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-373/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds Orion Virtual Infrastructure Monitor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the OneTimeJobSchedulerEventsService WCF service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/Success_Center/SAM/Content/Release_Notes/SAM_2020-2-5_release_notes.htm#Fixed

## Disclosure Timeline

- 2020-11-13 - Vulnerability reported to vendor
- 2021-03-30 - Coordinated public release of advisory
