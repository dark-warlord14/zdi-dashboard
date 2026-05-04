# ZDI-21-417: Adobe Bridge Genuine Software Service Incorrect Permission Assignment Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-417
- **ZDI-CAN:** ZDI-CAN-12735
- **Date:** 2021-04-15
- **CVE:** CVE-2021-21096
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Bridge
- **Credit:** ikth
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-417/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Adobe Bridge. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the AdobeGCData directory by the Adobe Genuine Software Service. The issue results from incorrect permissions set on this directory. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/bridge/apsb21-23.html

## Disclosure Timeline

- 2021-02-10 - Vulnerability reported to vendor
- 2021-04-15 - Coordinated public release of advisory
