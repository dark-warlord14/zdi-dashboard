# ZDI-24-966: Docker Desktop Daemon CLI External Control of File Path Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-966
- **ZDI-CAN:** ZDI-CAN-23533
- **Date:** 2024-07-26
- **CVE:** CVE-2024-5652
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-966/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Daemon CLI. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://docs.docker.com/desktop/release-notes/#for-windows-5

## Disclosure Timeline

- 2024-05-22 - Vulnerability reported to vendor
- 2024-07-26 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
