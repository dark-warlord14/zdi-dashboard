# ZDI-23-1166: ASUS RT-AX92U lighttpd mod_webdav.so SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1166
- **ZDI-CAN:** ZDI-CAN-16078
- **Date:** 2023-08-23
- **CVE:** CVE-2023-35720
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** ASUS
- **Affected Products:** RT-AX92U
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1166/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected ASUS RT-AX92U routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mod_webdav.so module. When parsing a request, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

ASUS has issued an update to correct this vulnerability. More details can be found at: https://www.asus.com/networking-iot-servers/whole-home-mesh-wifi-system/aimesh-wifi-routers-and-systems/rt-ax92u/helpdesk_bios/?model2Name=RT-AX92U

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2023-08-23 - Coordinated public release of advisory
