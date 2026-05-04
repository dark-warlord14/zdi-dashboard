# ZDI-24-670: (0Day) Famatech Advanced IP Scanner Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-670
- **ZDI-CAN:** ZDI-CAN-20768
- **Date:** 2024-06-13
- **CVE:** CVE-2024-30376
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Famatech
- **Affected Products:** Advanced IP Scanner
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-670/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Famatech Advanced IP Scanner. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the application's use of Qt. The application loads Qt plugins from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

05/12/23 – ZDI reported the vulnerability to the vendor 05/16/23 –The vendor acknowledged the receipt of the report 12/01/23 – ZDI asked for updates 01/10/24 –The vendor communicated that the development team was working on a fix 05/16/24 – ZDI asked for updates and notified the vendor of the intention to publish the case as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-05-12 - Vulnerability reported to vendor
- 2024-06-13 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
