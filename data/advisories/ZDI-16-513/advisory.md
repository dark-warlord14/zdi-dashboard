# ZDI-16-513: Microsoft Edge CSS white-space Property Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-513
- **ZDI-CAN:** ZDI-CAN-3874
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3247
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-513/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the CSS white-space property. By manipulating a document's elements an attacker can trigger a read past the end of an allocated buffer. An attacker could leverage this vulnerability to disclose information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-104

## Disclosure Timeline

- 2016-07-08 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
