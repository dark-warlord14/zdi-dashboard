# ZDI-16-395: Foxit Reader Safe Mode Bypass Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-395
- **ZDI-CAN:** ZDI-CAN-3659
- **Date:** 2016-06-29
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Björn Ruytenberg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-395/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SWF files inside PDF files. Embedded SWF files in Foxit Reader run outside the Safe Mode context. This can be leveraged by an attacker in conjunction with other vulnerabilities to execute arbitrary code in the context of the process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-06-29 - Coordinated public release of advisory
