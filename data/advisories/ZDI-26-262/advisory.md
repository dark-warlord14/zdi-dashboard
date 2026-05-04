# ZDI-26-262: Adobe ColdFusion deleteVersion Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-262
- **ZDI-CAN:** ZDI-CAN-29549
- **Date:** 2026-04-15
- **CVE:** CVE-2026-34619
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** Jonathan Lein of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-262/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Adobe ColdFusion. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the deleteVersion method. The issue results from the lack of proper validation of user-supplied data prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of the service account.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb26-38.html

## Disclosure Timeline

- 2026-03-25 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
