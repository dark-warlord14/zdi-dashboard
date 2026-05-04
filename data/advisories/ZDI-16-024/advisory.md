# ZDI-16-024: Foxit Reader Font Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-024
- **ZDI-CAN:** ZDI-CAN-3465
- **Date:** 2016-01-25
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** Mario Gomes(@NetFuzzer)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within font parsing. A specially crafted font embedded in a PDF file can force a dangling pointer to be reused after it has been freed. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-01-05 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
