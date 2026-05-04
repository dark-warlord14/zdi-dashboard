# ZDI-23-1014: (Pwn2Own) Inductive Automation Ignition OPC UA Quick Client Missing Authentication for Critical Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1014
- **ZDI-CAN:** ZDI-CAN-20540
- **Date:** 2023-08-01
- **CVE:** CVE-2023-38123
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** 20urdjk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1014/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Inductive Automation Ignition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the server configuration. The issue results from the lack of authentication prior to allowing access to password change functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://inductiveautomation.com/blog/inductive-automation-participates-in-pwn2own-to-strengthen-ignition-security

## Disclosure Timeline

- 2023-02-23 - Vulnerability reported to vendor
- 2023-08-01 - Coordinated public release of advisory
