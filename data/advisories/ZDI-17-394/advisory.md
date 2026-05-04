# ZDI-17-394: EMC Data Protection Advisor ImageServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-394
- **ZDI-CAN:** ZDI-CAN-3844
- **Date:** 2017-06-12
- **CVE:** CVE-2016-8211
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Data Protection Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-394/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of EMC Data Protection Advisor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ImageServlet servlet which listens on TCP ports 9002 and 9004. The issue lies in the failure to properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files under the context of SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/bugtraq/2017/Jan/att-87/ESA-2016-133.txt

## Disclosure Timeline

- 2016-07-07 - Vulnerability reported to vendor
- 2017-06-12 - Coordinated public release of advisory
