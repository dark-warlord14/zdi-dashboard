# ZDI-22-1020: (Pwn2Own) Inductive Automation Ignition ZIP File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1020
- **ZDI-CAN:** ZDI-CAN-16949
- **Date:** 2022-07-15
- **CVE:** CVE-2022-35873
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** 20urdjk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ZIP files. Crafted data in a ZIP file can cause the application to execute arbitrary Python scripts. The user interface fails to provide sufficient indication of the hazard. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://support.inductiveautomation.com/hc/en-us/articles/7625759776653-Regarding-Pwn2Own-2022-Vulnerabilities

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-15 - Coordinated public release of advisory
