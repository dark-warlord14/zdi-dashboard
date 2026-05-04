# ZDI-07-059: Verity KeyView SDK Multiple File Format Parsing Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-07-059
- **ZDI-CAN:** ZDI-CAN-047
- **Date:** 2007-10-31
- **CVE:** CVE-2007-5909
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM, Verity
- **Affected Products:** Lotus Notes KeyView SDK
- **Credit:** Eric DETOISIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-059/
## Vulnerability Details

Several vulnerabilities exist in the popular Verity KeyView SDK used in many enterprise applications like IBM Lotus Notes. When parsing several different file formats a standard stack overflow occurs allowing a malicious user to gain complete control of the affected machine under the rights of the currently logged in user. The problem lies when copying user supplied data to a stack based buffer without any boundary conditions. The following file formats have been identified as vulnerable: Adobe Acrobat FrameMaker - .mif Applix Words - .aw Microsoft Rich Text Format - .rtf Portable Executable - .exe Dynamic Link Library - .dll Applix Presents - .ag Microsoft Word - .doc

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-1.ibm.com/support/docview.wss?rs=899&uid=swg21272836

## Disclosure Timeline

- 2006-06-16 - Vulnerability reported to vendor
- 2007-10-31 - Coordinated public release of advisory
