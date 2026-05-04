# ZDI-15-210: Adobe Acrobat Reader Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-210
- **ZDI-CAN:** ZDI-CAN-2713
- **Date:** 2015-05-12
- **CVE:** CVE-2015-3057
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-210/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. The issue lies in the failure to properly initialize a variable prior to using it, leading to memory corruption. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-10.html

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
