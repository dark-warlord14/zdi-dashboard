# ZDI-19-142: Foxit Reader XFA removeInstance Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-142
- **ZDI-CAN:** ZDI-CAN-7601
- **Date:** 2019-01-25
- **CVE:** CVE-2019-6727
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** juggernaut
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-142/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the removeInstance method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-11-28 - Vulnerability reported to vendor
- 2019-01-25 - Coordinated public release of advisory
