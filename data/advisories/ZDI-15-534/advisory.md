# ZDI-15-534: Adobe Acrobat Reader DC CMAP Table Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-534
- **ZDI-CAN:** ZDI-CAN-3334
- **Date:** 2015-11-02
- **CVE:** CVE-2015-7650
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-534/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way CMAP tables are parsed. A specially crafted CMAP table embedded in a PDF file can force Adobe Acrobat Reader to read memory past the end of an allocated object. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-10-01 - Vulnerability reported to vendor
- 2015-11-02 - Coordinated public release of advisory
