# ZDI-26-297: Siemens SINEC NMS Improper Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-297
- **ZDI-CAN:** ZDI-CAN-28759
- **Date:** 2026-04-23
- **CVE:** CVE-2026-25654
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** SINEC NMS
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-297/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Siemens SINEC NMS. Authentication is required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 443 by default. The issue results from improper authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-605717.html

## Disclosure Timeline

- 2026-01-22 - Vulnerability reported to vendor
- 2026-04-23 - Coordinated public release of advisory
- 2026-04-23 - Advisory Updated
