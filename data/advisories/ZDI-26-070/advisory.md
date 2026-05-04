# ZDI-26-070: Adobe ColdFusion CAR File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-070
- **ZDI-CAN:** ZDI-CAN-27940
- **Date:** 2026-02-06
- **CVE:** CVE-2025-61808
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** Vladislav Berghici of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe ColdFusion. Authentication is required to exploit this vulnerability. The specific flaw exists within the parsing of CAR files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb25-105.html

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2026-02-06 - Coordinated public release of advisory
- 2026-02-06 - Advisory Updated
