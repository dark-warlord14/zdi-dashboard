# ZDI-22-927: Advantech iView addDeviceTreeItem SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-927
- **ZDI-CAN:** ZDI-CAN-16746
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2137
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-927/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. When parsing the device_get_community and device_set_community elements of the addDeviceTreeItem action, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
