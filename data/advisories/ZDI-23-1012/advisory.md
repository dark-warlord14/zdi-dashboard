# ZDI-23-1012: (Pwn2Own) Inductive Automation Ignition OPC UA Quick Client Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1012
- **ZDI-CAN:** ZDI-CAN-20355
- **Date:** 2023-08-01
- **CVE:** CVE-2023-38121
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** 20urdjk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the id parameter provided to the Inductive Automation Ignition web interface. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://inductiveautomation.com/blog/inductive-automation-participates-in-pwn2own-to-strengthen-ignition-security

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-01 - Coordinated public release of advisory
