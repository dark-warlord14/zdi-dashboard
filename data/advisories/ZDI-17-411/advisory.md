# ZDI-17-411: Foxit Reader JPXDecode stream Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-411
- **ZDI-CAN:** ZDI-CAN-4376
- **Date:** 2017-06-15
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-411/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPXDecode streams. The issue results from the lack of proper validation of user-supplied data which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2017-01-03 - Vulnerability reported to vendor
- 2017-06-15 - Coordinated public release of advisory
