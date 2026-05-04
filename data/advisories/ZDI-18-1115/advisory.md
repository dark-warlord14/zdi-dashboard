# ZDI-18-1115: Adobe Acrobat Pro DC ImageConversion EMF Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1115
- **ZDI-CAN:** ZDI-CAN-6669
- **Date:** 2018-10-03
- **CVE:** CVE-2018-12868
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Lin Wang of Beihang University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-30.html

## Disclosure Timeline

- 2018-07-17 - Vulnerability reported to vendor
- 2018-10-03 - Coordinated public release of advisory
- 2018-10-03 - Advisory Updated
