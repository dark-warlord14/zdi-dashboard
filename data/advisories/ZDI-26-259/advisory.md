# ZDI-26-259: (0Day) Docker Desktop cli-plugins Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-259
- **ZDI-CAN:** ZDI-CAN-27430
- **Date:** 2026-04-15
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Nitesh Surana (niteshsurana.com) & Nelson William Gamazo Sanchez of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-259/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop for Windows. An attacker must first obtain the ability to escape the container and execute low-privileged code within the Docker Hyper-V VM in order to exploit this vulnerability. The specific flaw exists within the the implemention of the Docker cli-plugins functionality. The issue results from incorrect permissions on folders. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code on the host system in the context of the current user.

## Additional Details

07/11/25 - ZDI submitted the report to the vendor 08/27/25 - ZDI asked for updates 09/05/25 - the vendor requested technical clarification 09/15/25 - ZDI provided additional details 11/11/25 - the vendor rejected the report because the exploitation required prior privileged access 04/08/26 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-09 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
