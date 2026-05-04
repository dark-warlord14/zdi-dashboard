# ZDI-26-152: Docker Desktop Docker Plugins Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-152
- **ZDI-CAN:** ZDI-CAN-28304
- **Date:** 2026-03-06
- **CVE:** CVE-2025-15558
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Docker
- **Credit:** Nitesh Surana (niteshsurana.com) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-152/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the plugins directory path. The product executes a program from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the target user.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://github.com/docker/cli/security/advisories/GHSA-p436-gjf2-799p

## Disclosure Timeline

- 2025-10-16 - Vulnerability reported to vendor
- 2026-03-06 - Coordinated public release of advisory
- 2026-03-06 - Advisory Updated
