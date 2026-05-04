# ZDI-17-187: Trend Micro InterScan Messaging Security Suite DetailReportAction Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-187
- **ZDI-CAN:** ZDI-CAN-4472
- **Date:** 2017-03-22
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Messaging Security Suite
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-187/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro InterScan Messaging Security Suite. Authentication is required to exploit this vulnerability. The specific flaw exists within the showPicture method of the DetailReportAction class, which listens on TCP port 8445 by default. When parsing the pictureName parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116903

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-03-22 - Coordinated public release of advisory
