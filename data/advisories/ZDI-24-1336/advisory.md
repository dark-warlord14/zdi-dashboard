# ZDI-24-1336: Wacom Center WTabletServicePro Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1336
- **ZDI-CAN:** ZDI-CAN-24304
- **Date:** 2024-10-11
- **CVE:** CVE-2024-9766
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wacom
- **Affected Products:** Center
- **Credit:** Amol Dosanjh of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1336/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Wacom Center. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within WTabletServicePro process. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 6.4.7 https://www.wacom.com/en-gb/support/product-support/drivers?driver-search=571

## Disclosure Timeline

- 2024-05-30 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
