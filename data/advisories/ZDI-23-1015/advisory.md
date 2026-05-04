# ZDI-23-1015: (Pwn2Own) Inductive Automation Ignition OPC UA Quick Client Task Scheduling Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1015
- **ZDI-CAN:** ZDI-CAN-20541
- **Date:** 2023-08-01
- **CVE:** CVE-2023-38124
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** 20urdjk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Authentication is required to exploit this vulnerability. The specific flaw exists within the Ignition Gateway server. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://inductiveautomation.com/blog/inductive-automation-participates-in-pwn2own-to-strengthen-ignition-security

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-01 - Coordinated public release of advisory
