# ZDI-18-699: Foxit Reader ConvertToPDF_x86 JPG Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-699
- **ZDI-CAN:** ZDI-CAN-5873
- **Date:** 2018-07-19
- **CVE:** CVE-2018-11622
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** soiax
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-699/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ConvertToPDF_x86.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-03-21 - Vulnerability reported to vendor
- 2018-07-19 - Coordinated public release of advisory
- 2018-07-19 - Advisory Updated
