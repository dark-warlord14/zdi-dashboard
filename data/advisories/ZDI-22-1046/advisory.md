# ZDI-22-1046: Docker Desktop Exposed Dangerous Method Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1046
- **ZDI-CAN:** ZDI-CAN-15361
- **Date:** 2022-08-04
- **CVE:** CVE-2022-23774
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1046/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the com.docker.service module. The module exposes a dangerous function to unprivileged users. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://docs.docker.com/desktop/release-notes/#docker-desktop-450

## Disclosure Timeline

- 2022-01-12 - Vulnerability reported to vendor
- 2022-08-04 - Coordinated public release of advisory
