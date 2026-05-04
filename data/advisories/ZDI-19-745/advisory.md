# ZDI-19-745: Adobe Acrobat Reader DC Protected View Text Copy Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-745
- **ZDI-CAN:** ZDI-CAN-8763
- **Date:** 2019-08-19
- **CVE:** CVE-2019-8027
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-745/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the Copy menu command in Protected View. This command can trigger a memory access at an invalid address. An attacker can leverage this vulnerability to execute code in the context of the current AppContainer process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-41.html

## Disclosure Timeline

- 2019-05-29 - Vulnerability reported to vendor
- 2019-08-19 - Coordinated public release of advisory
