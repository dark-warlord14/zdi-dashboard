# ZDI-16-410: Microsoft Internet Explorer CTableLayout AddRow Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-410
- **ZDI-CAN:** ZDI-CAN-3668
- **Date:** 2016-07-12
- **CVE:** CVE-2016-3242
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 62600BCA031B9EB5CB4A74ADDDD6771E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-410/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer keeps track of table rows when performing layout of HTML tables. By manipulating a document's elements an attacker can cause Internet Explorer to read beyond the end of an array of pointers to CTableRow objects. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-084

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
