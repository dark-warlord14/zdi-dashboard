# ZDI-18-438: Adobe Acrobat Pro DC EMF EMR_STRETCHDIBITS Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-438
- **ZDI-CAN:** ZDI-CAN-5469
- **Date:** 2018-05-15
- **CVE:** CVE-2018-4950
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-438/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the EMR_STRETCHDIBITS record in EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-09.html

## Disclosure Timeline

- 2018-01-26 - Vulnerability reported to vendor
- 2018-05-15 - Coordinated public release of advisory
- 2018-05-15 - Advisory Updated
