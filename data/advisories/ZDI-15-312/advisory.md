# ZDI-15-312: Adobe Acrobat Pro Reports Save Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-312
- **ZDI-CAN:** ZDI-CAN-2693
- **Date:** 2015-07-14
- **CVE:** CVE-2015-5115
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-312/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Report object. Attempting to save specially crafted reports can force Adobe Acrobat Pro to read memory past the end of an allocated object. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-01-20 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
