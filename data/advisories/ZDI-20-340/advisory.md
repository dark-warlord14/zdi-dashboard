# ZDI-20-340: (Pwn2Own) TP-Link Archer A7 SSH Port Forwarding Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-340
- **ZDI-CAN:** ZDI-CAN-9664
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10888
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** F-Secure Labs - Mark Barnes, Toby Drew, Max Van Amerongen, and James Loureiro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-340/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SSH port forwarding requests during initial setup. The issue results from the lack of proper authentication prior to establishing SSH port forwarding rules. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the WAN interface.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
