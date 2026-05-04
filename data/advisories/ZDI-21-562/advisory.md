# ZDI-21-562: Schneider Electric C-Bus Toolkit Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-562
- **ZDI-CAN:** ZDI-CAN-12714
- **Date:** 2021-05-11
- **CVE:** CVE-2021-22716
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** C-Bus Toolkit
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-562/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Schneider Electric C-Bus Toolkit. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on product folders created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-105-01

## Disclosure Timeline

- 2020-12-22 - Vulnerability reported to vendor
- 2021-05-11 - Coordinated public release of advisory
