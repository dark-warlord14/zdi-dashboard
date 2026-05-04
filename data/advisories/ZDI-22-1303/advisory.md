# ZDI-22-1303: Docker Desktop Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1303
- **ZDI-CAN:** ZDI-CAN-15310
- **Date:** 2022-09-29
- **CVE:** CVE-2022-23774
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1303/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Docker Desktop Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://docs.docker.com/desktop/release-notes/#security-3

## Disclosure Timeline

- 2022-02-09 - Vulnerability reported to vendor
- 2022-09-29 - Coordinated public release of advisory
