# ZDI-18-355: Foxit Reader ConvertToPDF_x86 JPG Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-355
- **ZDI-CAN:** ZDI-CAN-5754
- **Date:** 2018-04-20
- **CVE:** CVE-2018-9971
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** soiax
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-355/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ConvertToPDF_x86.dll. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2018-03-06 - Vulnerability reported to vendor
- 2018-04-20 - Coordinated public release of advisory
- 2018-04-20 - Advisory Updated
