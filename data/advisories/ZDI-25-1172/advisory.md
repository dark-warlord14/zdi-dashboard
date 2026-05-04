# ZDI-25-1172: RealDefense SUPERAntiSpyware Exposed Dangerous Function Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1172
- **ZDI-CAN:** ZDI-CAN-27668
- **Date:** 2025-12-19
- **CVE:** CVE-2025-14492
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** RealDefense
- **Affected Products:** SUPERAntiSpyware
- **Credit:** gongjae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1172/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of RealDefense SUPERAntiSpyware. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SAS Core Service. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 10.0.1280 https://secure.superantispyware.com/content/producthistory.html#:~:text=Product%20Changes%20and%20Enhancements,10.0.1278

## Disclosure Timeline

- 2025-09-04 - Vulnerability reported to vendor
- 2025-12-19 - Coordinated public release of advisory
- 2025-12-19 - Advisory Updated
