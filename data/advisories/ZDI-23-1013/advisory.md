# ZDI-23-1013: (Pwn2Own) Inductive Automation Ignition OPC UA Quick Client Permissive Cross-domain Policy Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1013
- **ZDI-CAN:** ZDI-CAN-20539
- **Date:** 2023-08-01
- **CVE:** CVE-2023-38122
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** 20urdjk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the web server. The issue results from the lack of appropriate Content Security Policy headers. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://inductiveautomation.com/blog/inductive-automation-participates-in-pwn2own-to-strengthen-ignition-security

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-01 - Coordinated public release of advisory
