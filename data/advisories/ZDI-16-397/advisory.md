# ZDI-16-397: Foxit Reader ConvertToPDF TIFF Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-397
- **ZDI-CAN:** ZDI-CAN-3698
- **Date:** 2016-06-29
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-397/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ConvertToPDF plugin. A TIFF image can force Foxit Reader to write values past the end of an allocated object. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-06-29 - Coordinated public release of advisory
