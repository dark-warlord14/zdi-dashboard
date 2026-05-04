# ZDI-25-306: Docker Desktop Helper Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-306
- **ZDI-CAN:** ZDI-CAN-23513
- **Date:** 2025-05-21
- **CVE:** CVE-2024-5652
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** Hashim Jawad (@ihack4falafel)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-306/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the WindowsContainersController class. By creating a junction, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Docker has issued an update to correct this vulnerability. More details can be found at: https://docs.docker.com/desktop/release-notes/#for-windows-19

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
