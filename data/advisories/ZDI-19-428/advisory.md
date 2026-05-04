# ZDI-19-428: Foxit Reader localFileStorage Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-428
- **ZDI-CAN:** ZDI-CAN-7407
- **Date:** 2019-04-29
- **CVE:** CVE-2019-6754
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-428/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the localFileStorage method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-12-27 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
