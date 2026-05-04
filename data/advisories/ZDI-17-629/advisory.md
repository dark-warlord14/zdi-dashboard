# ZDI-17-629: Adobe Acrobat Pro DC ImageConversion EMF Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-629
- **ZDI-CAN:** ZDI-CAN-4847
- **Date:** 2017-08-08
- **CVE:** CVE-2017-11271
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-629/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-24.html

## Disclosure Timeline

- 2017-06-14 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
