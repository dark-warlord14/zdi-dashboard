# ZDI-16-402: Foxit Reader ConvertToPDF BMP Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-402
- **ZDI-CAN:** ZDI-CAN-3815
- **Date:** 2016-06-29
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-402/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ConvertToPDF plugin. A crafted BMP image can trigger a read past the end of an allocated buffer. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-06-29 - Coordinated public release of advisory
