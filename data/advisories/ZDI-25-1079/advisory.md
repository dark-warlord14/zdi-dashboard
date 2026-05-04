# ZDI-25-1079: (0Day) Soda PDF Desktop Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1079
- **ZDI-CAN:** ZDI-CAN-25793
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14406
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Soda PDF
- **Affected Products:** Desktop
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1079/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Soda PDF Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

04/25/25 - ZDI reported the vulnerability to Avanquest’s support team 08/11/25 - ZDI asked for updates 08/12/25 – the vendor acknowledged that the report was escalated to the proper department 11/10/25 - ZDI asked for updates 11/21/25 – the vendor indicated that they don't offer bounties or rewards 11/21/25 - ZDI confirmed not accepting any rewards or bounties and asked for the expected fix date 12/04/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-04-25 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
