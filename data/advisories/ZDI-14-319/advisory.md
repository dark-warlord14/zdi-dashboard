# ZDI-14-319: Microsoft Internet Explorer CBackgroundCollection Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-319
- **ZDI-CAN:** ZDI-CAN-2486
- **Date:** 2014-09-16
- **CVE:** CVE-2014-4096
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AbdulAziz Hariri HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-319/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CBackgroundCollection objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://go.microsoft.com/fwlink/?LinkId=509961

## Disclosure Timeline

- 2014-08-04 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
