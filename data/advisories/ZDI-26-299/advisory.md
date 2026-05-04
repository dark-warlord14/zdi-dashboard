# ZDI-26-299: Docker Desktop Enhanced Container Isolation Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-299
- **ZDI-CAN:** ZDI-CAN-28822
- **Date:** 2026-04-23
- **CVE:** CVE-2026-6406
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Nitesh Surana (niteshsurana.com) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-299/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code within a container in order to exploit this vulnerability. The specific flaw exists within the processing of Docker CLI arguments. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges to resources normally protected by Enhanced Container Isolation.

## Additional Details

Fixed in Docker Desktop 4.59.0

## Disclosure Timeline

- 2026-01-09 - Vulnerability reported to vendor
- 2026-04-23 - Coordinated public release of advisory
- 2026-04-23 - Advisory Updated
