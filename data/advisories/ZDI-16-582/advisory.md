# ZDI-16-582: Foxit Reader JBIG2 Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-582
- **ZDI-CAN:** ZDI-CAN-4028
- **Date:** 2016-11-02
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-582/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within JBIG2 parsing. The issue results from the lack of proper validation of user-supplied data which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code under the context of current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2016-11-02 - Coordinated public release of advisory
