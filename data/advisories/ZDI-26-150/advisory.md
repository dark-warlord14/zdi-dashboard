# ZDI-26-150: Docker Desktop for Mac Docker Model Runner Exposed Dangerous Function Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-150
- **ZDI-CAN:** ZDI-CAN-28379
- **Date:** 2026-03-03
- **CVE:** CVE-2026-28400
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:L/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Nitesh Surana (niteshsurana.com) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-150/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within Docker Model Runner. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://github.com/docker/model-runner/security/advisories/GHSA-m456-c56c-hh5c#advisory-comment-165261

## Disclosure Timeline

- 2025-11-05 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
