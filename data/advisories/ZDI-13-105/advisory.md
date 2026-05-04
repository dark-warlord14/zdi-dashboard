# ZDI-13-105: Adobe Reader U3D Processing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-105
- **ZDI-CAN:** ZDI-CAN-1667
- **Date:** 2013-05-30
- **CVE:** CVE-2013-2727
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Tobias Klein
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-105/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader 10.1.4 on OSX. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing a U3D file within a PDF. The parsing code fails to validate a value from the file used as size parameter for an allocation routine. This could lead to an integer overflow resulting in an out-of-bound index into a list of objects. This results in an attacker being able to specify an arbitrary value for a function pointer, which leads to the execution of arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb13-15.html

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-30 - Coordinated public release of advisory
