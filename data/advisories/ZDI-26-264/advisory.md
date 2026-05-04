# ZDI-26-264: Adobe ColdFusion fetchCFSettingFile Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-264
- **ZDI-CAN:** ZDI-CAN-29550
- **Date:** 2026-04-15
- **CVE:** CVE-2026-27305
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** Jonathan Lein of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-264/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe ColdFusion. Authentication is not required to exploit this vulnerability. The specific flaw exists within the fetchCFSettingFile method. The issue results from the lack of proper validation of user-supplied path parameters prior to using them in file operations. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb26-38.html

## Disclosure Timeline

- 2026-03-20 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
