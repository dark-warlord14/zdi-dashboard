# ZDI-24-1019: (Pwn2Own) Docker Desktop extension-manager Exposed Dangerous Function Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1019
- **ZDI-CAN:** ZDI-CAN-23779
- **Date:** 2024-07-29
- **CVE:** CVE-2024-6222
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Billy Jheng Bing-Jhong, Đỗ Minh Tuấn, Muhammad Alifa Ramdhan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1019/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute high-privileged code within the container in order to exploit this vulnerability. The specific flaw exists within the the implemention of the Docker Extensions functionality. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the host.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://docs.docker.com/desktop/release-notes/#4290

## Disclosure Timeline

- 2024-05-21 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
