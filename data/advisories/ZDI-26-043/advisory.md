# ZDI-26-043: (0Day) npm cli Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-043
- **ZDI-CAN:** ZDI-CAN-25430
- **Date:** 2026-01-12
- **CVE:** CVE-2026-0775
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** npm
- **Affected Products:** cli
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-043/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of npm cli. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of modules. The application loads modules from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

11/13/24 - ZDI submitted the report to the vendor 11/13/24 – the vendor acknowledged the receipt of the report 11/13/24 – the vendor communicated that the reported behavior was by design 08/05/25 – ZDI encouraged the vendor to re-assess the issue 12/18/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2024-11-13 - Vulnerability reported to vendor
- 2026-01-12 - Coordinated public release of advisory
- 2026-02-02 - Advisory Updated
