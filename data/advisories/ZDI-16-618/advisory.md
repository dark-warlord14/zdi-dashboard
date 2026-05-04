# ZDI-16-618: Attachmate Host Access Management and Security Server PassThru Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-618
- **ZDI-CAN:** ZDI-CAN-4022
- **Date:** 2016-12-13
- **CVE:** CVE-2016-5765
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Attachmate
- **Affected Products:** Host Access Management and Security Server
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-618/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Attachmate Host Access Management and Security Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PassThru resource. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of the current process.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: http://support.attachmate.com/techdocs/1704.html

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
