# ZDI-16-028: Foxit Reader XFA FormCalc replace Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-028
- **ZDI-CAN:** ZDI-CAN-3407
- **Date:** 2016-01-25
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XFA FormCalc. A specially crafted replace call can trigger an integer overflow condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2015-12-01 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
