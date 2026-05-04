# ZDI-16-452: Microsoft Edge GetRefererUrl Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-452
- **ZDI-CAN:** ZDI-CAN-3751
- **Date:** 2016-08-09
- **CVE:** CVE-2016-3326
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-452/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Microsoft Edge constructs Referer headers in HTTP requests. By manipulating a document's elements an attacker can force a string in memory to be reused after it has been freed. As a result, unintended information will be included in the Referer header. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-095

## Disclosure Timeline

- 2016-05-05 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory
