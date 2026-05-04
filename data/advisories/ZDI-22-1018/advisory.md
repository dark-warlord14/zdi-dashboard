# ZDI-22-1018: (Pwn2Own) Inductive Automation Ignition Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1018
- **ZDI-CAN:** ZDI-CAN-17206
- **Date:** 2022-07-15
- **CVE:** CVE-2022-35871
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Daan Keuper & Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1018/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authenticateAdSso method. The issue results from the lack of authentication prior to allowing the execution of python code. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://support.inductiveautomation.com/hc/en-us/articles/7625759776653-Regarding-Pwn2Own-2022-Vulnerabilities

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-15 - Coordinated public release of advisory
