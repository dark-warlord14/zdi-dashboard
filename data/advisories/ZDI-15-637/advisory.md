# ZDI-15-637: Adobe Reader DC AGM Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-637
- **ZDI-CAN:** ZDI-CAN-3019
- **Date:** 2015-12-14
- **CVE:** CVE-2015-8458
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Fritz Sands - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-637/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within AGM.dll. A specially crafted PDF with multiple layers can force a heap buffer overflow condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2015-12-14 - Coordinated public release of advisory
