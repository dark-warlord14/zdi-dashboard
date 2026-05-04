# ZDI-16-579: Foxit Reader GIF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-579
- **ZDI-CAN:** ZDI-CAN-3951
- **Date:** 2016-11-02
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-579/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of GIF images embedded in PDF files. A crafted GIF image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2016-11-02 - Coordinated public release of advisory
