# ZDI-26-263: Adobe ColdFusion subscribeToEndpoints Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-263
- **ZDI-CAN:** ZDI-CAN-30200
- **Date:** 2026-04-15
- **CVE:** CVE-2026-27282
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** Jonathan Lein of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-263/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Adobe ColdFusion. Authentication is not required to exploit this vulnerability. The specific flaw exists within the subscribeToEndpoints method. The issue results from a missing critical step during authentication. An attacker can leverage this in conjunction with other vulnerabilities to delete arbitrary files in the context of the service account.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb26-38.html

## Disclosure Timeline

- 2026-03-26 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
