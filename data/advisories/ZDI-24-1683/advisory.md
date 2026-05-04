# ZDI-24-1683: Wacom Center WTabletServicePro Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1683
- **ZDI-CAN:** ZDI-CAN-25359
- **Date:** 2024-12-12
- **CVE:** CVE-2024-12552
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wacom
- **Affected Products:** Center
- **Credit:** Vladislav Berghici and Amol Dosanjh of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1683/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Wacom Center. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within WTabletServicePro.exe. By creating a symbolic link, an attacker can abuse the service to create an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Wacom has issued an update to correct this vulnerability. More details can be found at: https://cdn.wacom.com/u/productsupport/drivers/win/professional/releasenotes/Windows_6.4.8-2.html

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2024-12-12 - Coordinated public release of advisory
- 2024-12-12 - Advisory Updated
