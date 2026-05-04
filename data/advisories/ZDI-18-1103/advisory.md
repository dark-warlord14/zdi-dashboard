# ZDI-18-1103: Foxit Reader Barcode Calculate Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1103
- **ZDI-CAN:** ZDI-CAN-6354
- **Date:** 2018-09-28
- **CVE:** CVE-2018-17622
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1103/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Calculate events. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-06-28 - Vulnerability reported to vendor
- 2018-09-28 - Coordinated public release of advisory
- 2018-09-28 - Advisory Updated
