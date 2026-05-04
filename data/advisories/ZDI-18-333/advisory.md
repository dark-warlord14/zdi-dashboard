# ZDI-18-333: Foxit Reader TIFF Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-333
- **ZDI-CAN:** ZDI-CAN-5473
- **Date:** 2018-04-20
- **CVE:** CVE-2018-9949
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** willJ of Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-333/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIFF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-01-12 - Vulnerability reported to vendor
- 2018-04-20 - Coordinated public release of advisory
- 2018-04-20 - Advisory Updated
