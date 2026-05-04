# ZDI-11-081: Adobe Flash Player Point Object Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-081
- **ZDI-CAN:** ZDI-CAN-997
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0578
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-081/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within construction of a specific ActionScript3 object. Due to improper type checking in the implementation of the constructor, an alternative type can be provided as an argument to the constructor and stored as a property. When this object is applied to a bitmap copy, the application will corrupt memory. This can lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-02.html

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
