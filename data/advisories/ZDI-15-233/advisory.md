# ZDI-15-233: Valve Steam Client Detection Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-233
- **ZDI-CAN:** ZDI-CAN-2627
- **Date:** 2015-05-19
- **CVE:** CVE-2015-4016
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Valve
- **Affected Products:** Steam
- **Credit:** Elvis Collado - HP DVLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-233/
## Vulnerability Details

This vulnerability allows remote attackers to execute a denial of service attack on vulnerable installations of Valve Steam. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Steam client detection protocol. By responding to a broadcast packet with a crafted response, an attacker can cause the Steam process to crash.

## Additional Details

Valve has issued an update to correct this vulnerability. More details can be found at: http://store.steampowered.com/news/16801/

## Disclosure Timeline

- 2015-05-14 - Vulnerability reported to vendor
- 2015-05-19 - Coordinated public release of advisory
