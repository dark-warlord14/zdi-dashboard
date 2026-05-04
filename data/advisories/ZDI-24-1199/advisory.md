# ZDI-24-1199: Adobe After Effects AVI File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1199
- **ZDI-CAN:** ZDI-CAN-24048
- **Date:** 2024-09-10
- **CVE:** CVE-2024-39382
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1199/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of AVI files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb24-55.html

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-09-10 - Coordinated public release of advisory
- 2024-09-10 - Advisory Updated
