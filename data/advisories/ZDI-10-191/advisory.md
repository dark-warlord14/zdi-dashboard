# ZDI-10-191: Adobe Reader ICC Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-191
- **ZDI-CAN:** ZDI-CAN-718
- **Date:** 2010-10-06
- **CVE:** CVE-2010-3621
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required in that a target must be coerced into opening a file or visiting a web page. The specific flaw exists within the ACE.dll module responsible for parsing ICC streams. When processing an ICC stream, the process performs math on two DWORD values from the input file. If these values wrap over the maximum integer value of 0xFFFFFFFF a mis-allocation can occur. Later, the process uses one of the original DWORD values as a size to a copy function. This can be abused by an attacker to overflow a stack buffer and subsequently execute code under the context of the user running the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-21.html

## Disclosure Timeline

- 2010-06-23 - Vulnerability reported to vendor
- 2010-10-06 - Coordinated public release of advisory
