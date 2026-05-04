# ZDI-26-260: (0Day) Docker Desktop System Editor Uncontrolled Search Path Element Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-260
- **ZDI-CAN:** ZDI-CAN-27571
- **Date:** 2026-04-15
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Nitesh Surana (niteshsurana.com) & Nelson William Gamazo Sanchez of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-260/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to escape the container and execute high-privileged code within the Docker Hyper-V VM in order to exploit this vulnerability. The specific flaw exists within the the system/editor endpoint. The product executes a program from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code on the host system in the context of the current user.

## Additional Details

07/11/25 - ZDI submitted the report to the vendor 08/27/25 - ZDI asked for updates 09/05/25 - the vendor requested technical clarification 09/15/25 - ZDI provided additional details 11/11/25 - the vendor rejected the report because the exploitation required prior privileged access 04/08/26 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-10 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
