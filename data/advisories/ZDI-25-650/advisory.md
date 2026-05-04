# ZDI-25-650: ATEN eco DC Missing Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-650
- **ZDI-CAN:** ZDI-CAN-26647
- **Date:** 2025-07-24
- **CVE:** CVE-2025-6685
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ATEN
- **Affected Products:** eco DC
- **Credit:** Vu Khanh Trinh (@_Sonicrr) from VNPT Cyber Immunity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-650/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of ATEN eco DC. Authentication is required to exploit this vulnerability. The specific flaw exists within the web-based interface. The issue results from the lack of validating the assigned user role when handling requests. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

ATEN has issued an update to correct this vulnerability. More details can be found at: https://www.aten.com/global/en/supportcenter/info/security-advisory/25/

## Disclosure Timeline

- 2025-05-13 - Vulnerability reported to vendor
- 2025-07-24 - Coordinated public release of advisory
- 2025-07-24 - Advisory Updated
