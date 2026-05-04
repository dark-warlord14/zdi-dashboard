# ZDI-18-773: Foxit Reader PDF Parsing ColorSpace Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-773
- **ZDI-CAN:** ZDI-CAN-6362
- **Date:** 2018-07-19
- **CVE:** CVE-2018-14313
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-773/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-06-12 - Vulnerability reported to vendor
- 2018-07-19 - Coordinated public release of advisory
- 2018-07-19 - Advisory Updated
