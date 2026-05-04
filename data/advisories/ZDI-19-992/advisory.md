# ZDI-19-992: TP-LINK TL-WR841N Web Service http_parser_main Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-992
- **ZDI-CAN:** ZDI-CAN-8457
- **Date:** 2019-11-26
- **CVE:** CVE-2019-17147
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR841N
- **Credit:** Nguyen Hoang Thach - Security Researcher at VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-992/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TP-LINK TL-WR841N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 80 by default. When parsing the Host request header, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length static buffer. An attacker can leverage this vulnerability to execute code in the context of the admin user.

## Additional Details

TP-Link has issued an update to correct this vulnerability. More details can be found at: https://www.tp-link.com/us/support/download/tl-wr841n/#Firmware

## Disclosure Timeline

- 2019-07-04 - Vulnerability reported to vendor
- 2019-11-26 - Coordinated public release of advisory
